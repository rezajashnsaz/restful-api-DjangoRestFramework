from django.contrib import admin
from comments.models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','name','matn')
    search_fields = ('name','matn')
    list_filter = ('created_at',)
    ordering = ['-id']


admin.site.register(Comment, CommentAdmin)