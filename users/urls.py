#django imports
from django.urls import path,include
#rest framework imports
from rest_framework import routers


#local imports 
from .views import UserViewSet

# init our router 

router = routers.DefaultRouter()

router.register(r'users',UserViewSet,basename='users')

urlpatterns = [
    path('',include(router.urls))
]