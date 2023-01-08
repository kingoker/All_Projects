from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Папки
class Folder(MPTTModel):
    author = models.ForeignKey(User, related_name="Создатель", null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, verbose_name="Slug")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publicated = models.BooleanField(default=True, verbose_name="Опубликован")
    parent = TreeForeignKey(
        'self',
        related_name="Подпапка",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'

    def __str__(self):
        return self.name


# Отделы
class Department(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, verbose_name="Slug")

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title


# Отчёт отделов
class Report(models.Model):
    department = models.ManyToManyField(Department, verbose_name="Отдел")
    title = models.CharField(max_length=100, verbose_name="Название")
    url = models.CharField(max_length=100, verbose_name="Ссылка на файл")
    slug = models.SlugField(max_length=100, verbose_name="Slug")

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'

    def __str__(self):
        return self.title