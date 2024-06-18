# from django.contrib import admin
# from .models import FilmFilesModel
# from .models import CommentModel
# from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin
from django.contrib import admin
from . import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe

@admin.register(models.FilmFilesModel)
class FilmFilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'download_count', )
    search_fields = ['title', ]
    exclude = ['download_count', ]
    search_fields = ('title', 'description')
    readonly_fields = ('code',)


@admin.register(models.CategoryModel)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('id', 'tree_actions', 'indented_title', 'parent',)
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', ]


@admin.register(models.FilmModel)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_preview', 'director', 'category', 'publish', 'created',
                    'updated', 'views', 'rating', ]
    list_filter = ['category', 'publish', 'director', 'rating',]
    search_fields = ['title', 'body', ]
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['category', 'publish', ]
    exclude = ['director', 'views', ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
        super().save_model(request, obj, form, change)

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="100"/>')
        else:
            return '(No image found)'

    image_preview.short_description = 'Превью'
    
@admin.register(models.CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "film_link", "created_at", "content")
    list_filter = ("user", "film")

    def film_link(self, obj):
        return mark_safe(
            f'<a href="{obj.film.get_absolute_url()}">{obj.film.title}</a>'
        )

    film_link.short_description = "Фильм"

# @admin.register(CommentModel)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("user", "film_link", "created_at", "comment")
#     list_filter = ("user", "film")
#
#     def film_link(self, obj):
#         return mark_safe(
#             f'<a href="{obj.film.get_absolute_url()}">{obj.film.title}</a>'
#         )
#
#     film_link.allow_tags = True