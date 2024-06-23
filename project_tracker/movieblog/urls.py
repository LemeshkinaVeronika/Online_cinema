from django.urls import path, re_path
from movieblog import views

from django.contrib.sitemaps.views import sitemap

from movieblog.sitemap import FilmSitemap, CategorySitemap

sitemaps = {
    'FilmSitemap': FilmSitemap,
    'CategorySitemap': CategorySitemap,
}

app_name = 'movieblog'
urlpatterns = [
    path("add_to_wishlist/", views.AddToWhishlist, name="add_to_wishlist"),
    path("rate_movie/", views.RateMovie, name="rate_movie"),
    path('<int:pk>-<str:slug>/', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>-<str:slug>/', views.CategoryPageView.as_view(), name='category_page'),
    path('film/<int:pk>-<str:slug>/', views.FilmPageView.as_view(), name='film_page'),
    re_path(r'(?P<tag_name>[\w-]+)/$', views.TagPageView.as_view(), name='tag_page'),
    path('search/', views.SearchPageView.as_view(), name='search_page'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("comment/add/<int:pk>/", views.AddCommentView.as_view(), name="add_comment"),  
    path("comment/edit/<int:pk>/", views.EditCommentView.as_view(), name="edit_comment"),  
    path("comment/delete/<int:pk>/", views.DeleteCommentView.as_view(), name="delete_comment"),
]
