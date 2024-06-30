from django.shortcuts import render, redirect, get_object_or_404
from .models import CategoryModel, FilmModel, CommentModel, UserFilmList
from django.views.generic import TemplateView
from django.views import View
from django.core.paginator import Paginator
from movieblog import models, forms
from django.db.models import Q
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .forms import CommentForm, UserFilmListForm
from django.urls import reverse, reverse_lazy


class IndexView(View):
    template_name = 'movieblog/index.html'

    def get(self, request, pk, slug):
        category = CategoryModel.objects.get(pk=pk)
        descendant_categories = category.get_descendants(include_self=True)
        films = FilmModel.objects.filter(category__in=descendant_categories)

        context = {
            'category': category,
            'films': films,
        }
        return render(request, self.template_name, context)

class CategoryPageView(View):
    template_name = 'movieblog/category_page.html'

    def get(self, request, pk, slug):
        if not request.user.is_authenticated:
            return redirect(reverse('user_app:login'))
        category = CategoryModel.objects.get(pk=pk)
        
        user_film_lists = UserFilmList.objects.filter(user=request.user, list_type=slug)
        films = [user_film_list.film for user_film_list in user_film_lists]

        context = {
            'category': category,
            'films': films,
        }
        return render(request, self.template_name, context)


    
class FilmPageView(DetailView):
    model = FilmModel
    template_name = 'movieblog/film_page.html'
    context_object_name = 'film'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = CommentModel.objects.filter(film=self.object)
        return context
    
class TagPageView(View):
    template_name = 'movieblog/tag_page.html'

    def get(self, request, tag_name):
        films_list = FilmModel.objects.filter(tags__slug=tag_name).distinct()

        paginator = Paginator(films_list, 10)
        page_number = request.GET.get('page', 1)
        films = paginator.page(page_number)

        context = {
            'tag_name': tag_name,
            'films': films
        }
        return render(request, self.template_name, context)
       
class SearchPageView(TemplateView):
    template_name = 'movieblog/search_page.html'

    def get(self, request, *args, **kwargs):
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            results = models.FilmModel.film_manager.filter(Q(full_body__icontains=query) | Q(title__icontains=query))


            paginator = Paginator(results, 10)
            page_number = request.GET.get('page', 1)
            results = paginator.get_page(page_number)

            context = {"query": query,
                       "results": results}

            return render(request,
                          self.template_name,
                          context)

        return render(request,
                      self.template_name,
                      {"query": request.GET['query']})

class BaseCommentView:  
    model = CommentModel  

    def get_success_url(self):  
        film = FilmModel.objects.get(pk=self.object.film.pk)  
        return reverse(  
            "movieblog:film_page",  
            kwargs={"pk": film.pk, "slug": film.slug},  
        )
    
class AddCommentView(BaseCommentView, CreateView):  
    form_class = CommentForm  
    template_name = "movieblog/comments.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.film = FilmModel.objects.get(pk=self.kwargs.get("pk"))
        return super().form_valid(form) 
    
class EditCommentView(BaseCommentView, UpdateView):  
    form_class = CommentForm  
    model = CommentModel 
    template_name = 'movieblog/comment_edit.html'
    context_object_name = 'comment'

    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('movieblog:film_page', kwargs={'pk': comment.film.pk, 'slug': comment.film.slug})

class DeleteCommentView(BaseCommentView, DeleteView):  
    template_name = "movieblog/comment_delete.html"
    def get_success_url(self):
        comment = self.get_object()
        return reverse_lazy('movieblog:film_page', kwargs={'pk': comment.film.pk, 'slug': comment.film.slug})

class AddToListView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        form = UserFilmListForm(request.POST)
        if form.is_valid():
            user_film_list = form.save(commit=False)
            user_film_list.user = request.user
            try:
                user_film_list.save()
                return redirect('movieblog:film_page', pk=user_film_list.film.pk, slug=user_film_list.film.slug)
            except:
                form.add_error(None, "Этот фильм уже добавлен в этот список.")
        
        return render(request, 'movieblog/add_to_list.html', {'form': form})
    
class RemoveFromListView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('user_app:login')

        film_id = request.POST.get('film_id')
        list_type = request.POST.get('list_type')

        user_film_list = get_object_or_404(UserFilmList, user=request.user, film_id=film_id, list_type=list_type)
        user_film_list.delete()

        return redirect('movieblog:category_page', pk=user_film_list.film.category.pk, slug=list_type)