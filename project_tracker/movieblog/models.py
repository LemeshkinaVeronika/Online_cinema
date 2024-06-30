from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager
import random


class FilmManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class FilmFilesModel(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Имя файла')
    file = models.FileField(upload_to='film_files/')
    code = models.IntegerField(default=0,
                               verbose_name='Код файла',
                               unique=True)
    download_count = models.IntegerField(default=0,
                                         verbose_name='Скачиваний')

    class Meta:
        verbose_name = 'Файл фильма'
        verbose_name_plural = 'Файлы фильмов'

    def increment_download_count(self):
        self.download_count += 1
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_code():
        code = random.randint(100000, 999999)
        while FilmFilesModel.objects.filter(code=code).exists():
            code = random.randint(100000, 999999)
        return code

class CategoryModel(MPTTModel):
    title = models.CharField(max_length=100,
                             verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Альт. заголовок")
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children',
                            db_index=True,
                            verbose_name='Родительская категория')
    description = models.CharField(max_length=350,
                                   verbose_name="Описание",
                                   blank=True)

    objects = TreeManager()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = 'parent', 'slug'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('movieblog:category_page', args=[int(self.pk), str(self.slug)])

    def __str__(self):
        return self.title


class FilmModel(models.Model):
    """Модель поста"""

    title = models.CharField(max_length=200,
                             verbose_name="Название")
    slug = models.SlugField(verbose_name="Альт. название")
    image = models.ImageField(upload_to='film/%Y/%m/%d',
                              default='default/not_found.png',
                              verbose_name='Постер')
    director = models.CharField(max_length=200,
                             verbose_name="Режиссер")
    category = TreeForeignKey('CategoryModel',
                              on_delete=models.PROTECT,
                              related_name='film',
                              verbose_name='Категория')
    RATING_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    rating = models.CharField(
        max_length=100,
        choices=RATING_CHOICES,
        default='0',
        verbose_name='Рейтинг',
    )
    full_body = CKEditor5Field(verbose_name='Основная информация')
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name="Опубликовано")
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Создано")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Обновлено")
    film_manager = FilmManager()

    views = models.IntegerField(default=0,
                                verbose_name="Количество просмотров")

    tags = TaggableManager(blank=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def get_absolute_url(self):
        """Метод получения URL-адреса объекта"""
        return reverse('movieblog:film_page', args=[int(self.pk), str(self.slug)])

    def get_next_film(self):
        """Метод получения следующего поста"""
        try:
            return self.get_next_by_publish(category=self.category)
        except FilmModel.DoesNotExist:
            return None

    def get_previous_film(self):
        """Метод получения предыдущего поста"""
        try:
            return self.get_previous_by_publish(category=self.category)
        except FilmModel.DoesNotExist:
            return None

    def __str__(self):
        return self.title

    file = models.OneToOneField(FilmFilesModel,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True,
                             verbose_name="Файл",
                             related_name="film")
# class FilmModel(models.Model):
#     """Модель поста"""

#     title = models.CharField(max_length=200,
#                              verbose_name="Название")
#     slug = models.SlugField(verbose_name="Альт. название")
#     image = models.ImageField(upload_to='film/%Y/%m/%d',
#                               default='default/not_found.png',
#                               verbose_name='Постер')
#     director = models.CharField(max_length=200,
#                                 verbose_name="Режиссер")
#     category = TreeForeignKey('CategoryModel',
#                               on_delete=models.PROTECT,
#                               related_name='film',
#                               verbose_name='Категория')
#     RATING_CHOICES = [
#         ('0', '0'),
#         ('1', '1'),
#         ('2', '2'),
#         ('3', '3'),
#         ('4', '4'),
#         ('5', '5'),
#     ]
#     rating = models.CharField(
#         max_length=100,
#         choices=RATING_CHOICES,
#         default='0',
#         verbose_name='Рейтинг',
#     )
#     full_body = CKEditor5Field(verbose_name='Основная информация')
#     publish = models.DateTimeField(default=timezone.now,
#                                    verbose_name="Опубликовано")
#     created = models.DateTimeField(auto_now_add=True,
#                                    verbose_name="Создано")
#     views = models.IntegerField(default=0, verbose_name="Просмотры") 
#     updated = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
#     objects = FilmManager()
    
                                   
class CommentModel(MPTTModel):
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='comments', verbose_name="Фильм")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="Пользователь")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительский комментарий')
    content = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    

    objects = TreeManager()

    class MPTTMeta:
        order_insertion_by = ['created_at']

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def str(self):
        return f'Комментарий от {self.user.username} на {self.film.title}'
    
class UserFilmList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='film_lists')
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='user_lists')
    list_type = models.CharField(max_length=20, choices=[('izbrannoe', 'Избранное'), ('posmotreno', 'Просмотренное'), ('budu-smotret', 'Буду смотреть')])

    class Meta:
        unique_together = ('user', 'film', 'list_type')

    def __str__(self):
        return f"{self.user.username} - {self.film.title} ({self.list_type})"