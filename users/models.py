from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, verbose_name="Телефон")
    apartment = models.CharField(blank=True, verbose_name="Адрес")
    floor = models.IntegerField(null=True, blank=True, verbose_name="Этаж")
    entrance = models.IntegerField(null=True, blank=True, verbose_name="Подъезд")
    
    # Fix related name conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    def __str__(self):
        return self.username 