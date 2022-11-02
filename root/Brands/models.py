from django.db import models


class Certificate(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='Brands/certificates', verbose_name='Эмблема сертификата', max_length=255)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.title


class Manufacture(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='Brands/fabric', verbose_name='Логотип', max_length=255)
    certificates = models.ManyToManyField(Certificate, verbose_name='Сертификаты')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.title

