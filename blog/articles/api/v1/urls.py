"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from articles.api.v1.views import *


urlpatterns = [

    #use function base views
    path('oldest-articles/', oldest_articles ),

    #use api view - class base views
    path('articles/', Articles.as_view() ),
    path('articles/<int:pk>/', ArticleDetails.as_view() ),
    
    #use generic view - class base views
    path('articles-generics/', ArticlesGeneric.as_view() ),
    path('articles-generics/<int:pk>/',ArticleDetailsGeneric.as_view() ),
    path('articles-generics/create/', ArticleCreateGeneric.as_view() ),
    path('articles-generics/update/<int:pk>/', ArticleUpdateGeneric.as_view() ),
    path('articles-generics/delete/<int:pk>/', ArticleDeleteGeneric.as_view() ),

]
