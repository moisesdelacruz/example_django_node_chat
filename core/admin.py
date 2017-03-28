from django.contrib import admin
from core.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('theme', 'user', 'text')
