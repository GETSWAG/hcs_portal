from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'author', 'is_published', 'start_date', 'end_date')
    list_filter = ('type', 'is_published')
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'type', 'author')
        }),
        ('Публикация', {
            'fields': ('is_published', 'start_date', 'end_date')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')

# Добавляем метаданные для модели
Announcement._meta.verbose_name = 'Новость/Объявление'
Announcement._meta.verbose_name_plural = 'Новости и объявления' 