from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from announcements.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('',home, name='home'),
    path('users/', include('users.urls')),
    path('services/', include('services.urls')),
    path('tickets/', include('tickets.urls')),
    path('announcements/', include('announcements.urls')),
] 