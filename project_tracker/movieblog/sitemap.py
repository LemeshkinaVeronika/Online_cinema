from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from . import models


class FilmSitemap(Sitemap):
    def items(self):
        return models.FilmModel.objects

    def lastmod(self, obj):
        return obj.updated

    def priority(self, obj):
        return 0.8

    def changefreq(self, obj):
        return "weekly"

    def location(self, obj):
        return reverse('movieblog:film_page', args=[obj.pk, obj.slug])


class CategorySitemap(Sitemap):
    def items(self):
        return models.CategoryModel.objects

    def lastmod(self, obj):
        return obj.updated

    def priority(self, obj):
        return 0.8

    def changefreq(self, obj):
        return "weekly"

    def location(self, obj):
        return reverse('movieblog:category_page', args=[obj.pk, obj.slug])

