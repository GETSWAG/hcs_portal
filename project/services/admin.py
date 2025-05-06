from django.contrib import admin
from .models import ServiceCategory, Service

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'category')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

# Добавляем метаданные для моделей
ServiceCategory._meta.verbose_name = 'Категория услуг'
ServiceCategory._meta.verbose_name_plural = 'Категории услуг'
Service._meta.verbose_name = 'Услуга'
Service._meta.verbose_name_plural = 'Услуги' 