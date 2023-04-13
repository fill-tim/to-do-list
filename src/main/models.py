from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    """
    Модель заметки
    """
    title = models.CharField('Заголовок', max_length=255, )
    description = models.CharField('Текст заметки', max_length=255, )
    importance = models.BooleanField('Важность', default=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f'{self.title} - {self.description} - {self.autor}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
