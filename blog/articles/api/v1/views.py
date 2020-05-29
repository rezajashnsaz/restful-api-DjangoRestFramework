from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from articles.models import *
from articles.api.v1.serializers import *
from rest_framework.decorators import api_view




########
# articles list with function base views
########
@api_view(['GET'])
def oldest_articles(request):
    articles = Article.objects.order_by('id')
    serializer = ArticleSerializer(articles , many = True)
    return Response({
        "data": serializer.data , 
        "status": 200 
    })





########
# articles list with APIView
########
class Articles(APIView):
    #header :    Api Key
    #key    :    Authorization
    #value  :    Token yourtoken
    # permission_classes = (IsAuthenticated,)
    def get(self , request , format = None):
        articles = Article.objects.order_by('-id')
        serializer = ArticleSerializer(articles , many = True)
        return Response(serializer.data)




########
# single article details with APIView
########
class ArticleDetails(APIView):
    def get(self , request , pk):
        article = Article.objects.get(id = pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)    




########
# articles list with generics
########
class ArticlesGeneric(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




########
# single article details with generics
########
class ArticleDetailsGeneric(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




########
# article create with generics
########
class ArticleCreateGeneric(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




########
# article update with generics
########
class ArticleUpdateGeneric(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




########
# article delete with generics
########
class ArticleDeleteGeneric(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer