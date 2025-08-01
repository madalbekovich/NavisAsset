from ckeditor.fields import RichTextField
from django.db import models

class Partners(models.Model):
    img = models.ImageField(upload_to='partners/img')

    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    answer = models.TextField(max_length=255, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Вопросы и ответы'
        verbose_name_plural = 'Вопросы и ответы'
        ordering = ['id']

    def __str__(self):
        return str(self.question)

class Review(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    username = models.CharField(max_length=50, verbose_name='Имя заказчика/клиента')
    number_of_review = models.IntegerField(verbose_name='Кл-во оценок')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзывы и оценки'
        verbose_name_plural = 'Отзывы и оценки'
        ordering = ['id']

    def __str__(self):
        return str(self.text)

class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    description = RichTextField(verbose_name="Описание")
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)


    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['id']

    def __str__(self):
        return str(self.title)