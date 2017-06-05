from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Post Details', {
            'fields': ('title', 'slug', 'category', 'date_published', 'publish')
        }),
        ('Post Content', {
            'fields': ('post_filename',)
        }),
    )
    prepopulated_fields = {'slug': ("title",)}
    search_fields = ['title',]
    list_display = ['title', 'category', 'publish', 'date_published']
    list_filter = ('category', 'publish')
    list_editable = ['category', 'publish', 'date_published']
    ordering = ['-date_published']

admin.site.register(Post, PostAdmin)
