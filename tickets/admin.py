from django.contrib import admin
from .models import Ticket, TicketComment

class TicketCommentInline(admin.TabularInline):
    model = TicketComment
    extra = 0
    readonly_fields = ('user', 'created_at')
    fields = ('user', 'content', 'created_at')
    verbose_name = 'Комментарий'
    verbose_name_plural = 'Комментарии'

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'service', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'service')
    search_fields = ('title', 'description', 'user__username', 'user__email')
    ordering = ('-created_at',)
    inlines = [TicketCommentInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'user', 'service')
        }),
        ('Статус и приоритет', {
            'fields': ('status', 'priority')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')

    def get_list_display(self, request):
        return ('id', 'title', 'user', 'service', 'status', 'priority', 'created_at')

    def get_list_display_links(self, request, list_display):
        return ('id', 'title')

@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'user__username', 'ticket__title')
    readonly_fields = ('created_at',)

# Добавляем метаданные для моделей
Ticket._meta.verbose_name = 'Заявка'
Ticket._meta.verbose_name_plural = 'Заявки'
TicketComment._meta.verbose_name = 'Комментарий'
TicketComment._meta.verbose_name_plural = 'Комментарии' 