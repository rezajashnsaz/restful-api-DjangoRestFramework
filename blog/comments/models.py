from django.db import models
from articles.models import Article
# Create your models here.


class Comment(models.Model):
    email = models.CharField(max_length = 200,verbose_name = 'ایمیل')
    name = models.CharField(max_length = 200,verbose_name = 'نام')
    matn = models.TextField(verbose_name = 'متن نظر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null = True,verbose_name = 'مقاله',related_name = 'artcomments')
    created_at = models.DateTimeField(auto_now_add = True,verbose_name = 'تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now = True,verbose_name = 'تاریخ اخرین تغییر')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.matn[:20]

