from django.contrib import admin
from django.contrib.admin import register

from .models import Reader, Book, Author

# admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Author)


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'quantity')
    search_fields = ('title', 'description')
