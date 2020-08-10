from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'active', 'image', 'thumbs']
    search_fields = ['title', 'sub_title']


admin.site.register(Post, PostAdmin)
admin.site.register(Contact)
