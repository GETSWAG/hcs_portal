from django.db import models
from django.conf import settings

class Announcement(models.Model):
    TYPE_CHOICES = [
        ('новости', 'Новости'),
        ('объявления', 'Объявления'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название")
    content = models.TextField(verbose_name="Содержание")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='объявления', verbose_name="Тип")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='announcements', verbose_name="Автор")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата окончания")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    def __str__(self):
        return self.title 