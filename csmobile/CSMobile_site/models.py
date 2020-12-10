from django.db import models

# Create your models here.


class FinalDB(models.Model):
    test = models.IntegerField(verbose_name='Тестовая строка')
