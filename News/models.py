from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    datetime = models.DateTimeField('Дата публикации', auto_now_add=True)
    content = models.TextField('Содержание')

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'News'
    verbose_name_plural = 'News'
