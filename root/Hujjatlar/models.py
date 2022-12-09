from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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
