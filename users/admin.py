from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    
    fieldsets = (
        ('Учетная запись', {
            'fields': ('username', 'password')
        }),
        ('Личная информация', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'apartment', 'floor', 'entrance')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone', 'apartment', 'floor', 'entrance'),
        }),
    )

# Добавляем метаданные для модели
CustomUser._meta.verbose_name = 'Пользователь'
CustomUser._meta.verbose_name_plural = 'Пользователи' 