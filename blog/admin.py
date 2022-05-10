from blog.models import Post
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class PostAdmin(admin.ModelAdmin):
    list_filter = ['active', 'date_posted']
    list_display = ['title', 'date_posted', 'active']
    search_fields = ['title', 'content', 'author']

admin.site.register(Post, PostAdmin)
