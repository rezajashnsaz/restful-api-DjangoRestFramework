from django.urls import path,include
from accounts.api.v1.views import *


urlpatterns = [

    #use function base views
    path('register/', register ),

    
]
