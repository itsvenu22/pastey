from django.contrib import admin
from .models import Snippet

@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('slug', 'created_at')  # You can customize which fields to show in the admin panel
    search_fields = ('slug', 'content')  # Allow searching by slug and content
