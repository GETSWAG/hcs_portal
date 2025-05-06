from django.shortcuts import render, get_object_or_404
from .models import Announcement
from services.models import Service


def announcement_list(request):
    announcements = Announcement.objects.filter(
        is_published=True
    ).order_by('-created_at')
    return render(request, 'announcements/list.html', {'announcements': announcements})

def announcement_detail(request, announcement_id):
    announcement = get_object_or_404(
        Announcement,
        id=announcement_id,
        is_published=True
    )
    
    context = {
        'announcement': announcement,
    }
    return render(request, 'announcements/detail.html', context)

def get_latest_announcements(limit=5):
    """Получение последних новостей для главной страницы"""
    return Announcement.objects.filter(
        is_published=True
    ).order_by('-created_at')[:limit]

def home(request):
    """Представление главной страницы"""
    # Получаем активные услуги
    services = Service.objects.filter(status='active')
    
    # Получаем последние новости
    latest_announcements = get_latest_announcements()
    
    context = {
        'services': services,
        'latest_announcements': latest_announcements,
    }
    return render(request, 'home.html', context) 