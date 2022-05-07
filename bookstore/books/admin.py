from django.contrib import admin

from .models import Author
from .models import Book

admin.site.register(Book)
admin.site.register(Author)
