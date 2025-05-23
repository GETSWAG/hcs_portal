from django.urls import path
from . import views
app_name = 'announcements'

urlpatterns = [
    path('', views.announcement_list, name='list'),
    path('<int:announcement_id>/', views.announcement_detail, name='detail'),
] 