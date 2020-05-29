from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True,verbose_name = 'کاربر',related_name = 'articles')    
    title = models.CharField(max_length = 250,verbose_name = 'عنوان')
    body = models.TextField(verbose_name = 'متن')
    sort = models.IntegerField(default = 0,verbose_name = 'شماره مرتب سازی')    
    publish = models.BooleanField(default = 0 , verbose_name = "انتشار")    
    created_at = models.DateTimeField(auto_now_add = True,verbose_name = 'تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now = True,verbose_name = 'تاریخ اخرین تغییر')
    tags = models.TextField(null = True,blank = True ,verbose_name = 'تگ ها')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

