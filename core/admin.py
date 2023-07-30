from django.contrib import admin
from django.contrib.admin import register
from django.db import transaction
from django.urls import reverse
from django.db.models import QuerySet
from django.utils.safestring import mark_safe

from .models import Reader, Book, Author


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_to_author', 'quantity')
    # list_display = ('inv_number', 'title', 'link_to_author', 'quantity')
    search_fields = ('title', 'description')
    list_filter = ('author', )
    actions = ['set_zero_quantity']

    def link_to_author(self, obj):
        url = reverse("admin:core_author_change", args=[obj.author.id])
        link = f'<a href="{url}">{obj.author}</a>'
        return mark_safe(link)
    link_to_author.short_description = 'Автор'

    @admin.action(description='Установить 0 наличие')
    def set_zero_quantity(self, request, queryset):
        queryset.update(quantity=0)
        self.message_user(request, f' Наличие книг 0')


@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'photo')
    search_fields = ('name', 'surname')


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'phone', 'is_active')
    # list_display = ('surname', 'name', 'phone', 'is_active', 'active_books')
    search_fields = ('name', 'surname')
    list_filter = ('is_active', )
    actions = ['change_status', 'remove_active_books']

    @admin.action(description='Сменить статус')
    def change_status(self, request, queryset: QuerySet):
        for el in queryset:
            if el.is_active:
                el.is_active = False
                el.save()
            else:
                el.is_active = True
                el.save()
            self.message_user(request, f'Cтатус {el.is_active} изменен)) ')

    # @admin.action(description='Удалить все активные книги')
    # def remove_active_books(self, request, queryset: QuerySet):
    #     queryset = queryset.prefetch_related('active_books')
    #     with transaction.atomic():
    #         for reader in queryset:
    #             for book in reader.active_books:
    #                 book.quantity += 1
    #                 book.save()
    #         [reader.active_books.clear() for reader in queryset]

