from django.contrib import admin
from comments.models import Comment

# Register your models here.

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('publishing', 'user', 'text')
