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
    path('<int:pk>-<str:slug>/', views.index, name='index'),
    path('category/<int:pk>-<str:slug>/', views.category_page, name='category_page'),
    path('film/<int:pk>-<str:slug>/', views.film_page, name='film_page'),
    re_path(r'(?P<tag_name>[\w-]+)/$', views.tag_page, name='tag_page'),
    path('search/', views.SearchPageView.as_view(), name='search_page'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]
