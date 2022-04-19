from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from shop.views import *



urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),  
    path('user_signup/', user_signup, name='user_signup'),
    path('login/', login, name='login'),
] 