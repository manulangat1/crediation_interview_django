
#django imports 
from django.shortcuts import render # noqa

import json
from rest_framework import viewsets


#rest framework imports 
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status,filters

#local imports

from .serializers import UserSerializer


# Create your views here.


"""
  This is a function that reads a json file recursively, closes the file  and returns the content  
"""
import os 
import pathlib
print(pathlib.Path().resolve())

def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

""" 

"""
def read_json():
    return json.loads(read_file('/home/manulangat/Desktop/interviews/cred/crediation/users/data/users.json'))


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'email']
    """
     This is a custom get queryset method that loads our content from the json file
    """
    def get_queryset(self,*args,**kwargs):
       
        params = self.request.query_params.get('search')
        
        if params:
            
            res = [ i for i in read_json() if i['email'] == params ]
           
            return res
        return read_json()
    def list(self,request):
        if(len(self.get_queryset()) > 0):
            serializer = self.get_serializer(self.get_queryset(),many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return  Response(
            {"Not Found": "Content Not Found, kindly try with a different search term "},
            status=status.HTTP_404_NOT_FOUND
        )