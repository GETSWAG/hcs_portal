from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket, TicketComment
from .forms import TicketForm, CommentForm
from services.models import Service

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tickets/list.html', {'tickets': tickets})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Заявка успешно создана!')
            return redirect('tickets:detail', ticket.id)
    else:
        initial = {}
        service_id = request.GET.get('service')
        if service_id:
            try:
                service = Service.objects.get(id=service_id)
                initial['service'] = service
            except Service.DoesNotExist:
                pass
        form = TicketForm(initial=initial)
    
    return render(request, 'tickets/create.html', {'form': form})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    comments = ticket.comments.all().order_by('created_at')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.user = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен!')
            return redirect('tickets:detail', ticket.id)
    else:
        form = CommentForm()
    
    return render(request, 'tickets/detail.html', {
        'ticket': ticket,
        'comments': comments,
        'form': form
    })

@login_required
def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.user = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен!')
    
    return redirect('tickets:detail', ticket_id=ticket.id) 