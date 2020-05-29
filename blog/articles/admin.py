from django.contrib import admin
from articles.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','body')
    search_fields = ('title','body')
    list_filter = ('created_at',)
    ordering = ['-id']


admin.site.register(Article, ArticleAdmin)