from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
# Create your views here.
from django.contrib.auth.models import User
from .serializer import ProductSerializer,productColourModelSerailizer,productImageModelserializer
from .models import productMainModel,productColourModel,productImageModel
from rest_framework import generics
from rest_framework.views import APIView

from django.http import HttpResponse, JsonResponse

class ProductList(generics.ListCreateAPIView):
    queryset = productMainModel.objects.select_related()
    print(queryset)
    serializer_class = ProductSerializer
    
    
def prodProductDetailWithId(request, pk):
    try:
        transformer = productMainModel.objects.get(pk=pk)
        print(transformer)
    except productMainModel.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = ProductSerializer(transformer)
        print(serializer)
        print(serializer.data)
        return JsonResponse(serializer.data)
    
# class ProductColor(generics.ListCreateAPIView):
#     queryset = productColourModel.objects.all()
#     print(queryset)
#     serializer_class = productColourModelSerailizer
  
# class ProductImage(generics.ListCreateAPIView):
#     queryset = productImageModel.objects.all()
#     print(queryset)
#     serializer_class = productImageModelserializer