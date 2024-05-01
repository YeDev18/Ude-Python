from django.contrib import admin
from .models import Book , BookNumber

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
      fields = ["title", "description"]
      list_display = ["title", "description","price"]
      list_filter= ['is_published']

admin.site.register(BookNumber)
