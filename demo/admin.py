from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
      fields = ["title", "description"]
      list_display = ["title", "description","price"]
      list_filter= ['is_published']

