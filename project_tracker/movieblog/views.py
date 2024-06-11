from django.shortcuts import render
from .models import CategoryModel, FilmModel
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from movieblog import models, forms
from django.db.models import Q

def index(request, pk, slug):
    category = CategoryModel.objects.get(pk=pk)
    descendant_categories = category.get_descendants(include_self=True)
    films = FilmModel.objects.filter(category__in=descendant_categories)


    context = {
        'category': category,
        'films': films,
    }
    return render(request,
                  'movieblog/index.html',
                  context)

def category_page(request, pk, slug):
    category = CategoryModel.objects.get(pk=pk)
    films = FilmModel.objects.filter(category=category)

    context = {
        'category': category,
        'films': films,
    }

    return render(request,
                  'movieblog/category_page.html',
                  context)
def film_page(request, pk, slug):
    film = FilmModel.objects.get(pk=pk)
    film.views += 1
    film.save()

    context = {
        'film': film,
    }

    return render(request,
                  'movieblog/film_page.html',
                  context)

def category_page(request, pk, slug):
    category = CategoryModel.objects.get(pk=pk)
    films = FilmModel.objects.filter(category=category)

    context = {
        'category': category,
        'films': films,
    }

    return render(request,
                      'movieblog/category_page.html',
                      context)

def tag_page(request, tag_name):
    films_list = FilmModel.objects.filter(tags__slug=tag_name).distinct()

    paginator = Paginator(films_list, 10)
    page_number = request.GET.get('page', 1)
    films = paginator.page(page_number)

    context = {
        'tag_name': tag_name,
        'films': films
    }

    return render(request,
                  'movieblog/tag_page.html',
                  context)


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
