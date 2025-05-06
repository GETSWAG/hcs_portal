from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory

def service_list(request, category_id=None):
    categories = ServiceCategory.objects.all()
    
    if category_id:
        category = get_object_or_404(ServiceCategory, id=category_id)
        services = Service.objects.filter(category=category, status='active')
    else:
        category = None
        services = Service.objects.filter(status='active')
    
    context = {
        'services': services,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'services/list.html', context)

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    context = {
        'service': service,
    }
    return render(request, 'services/detail.html', context) 