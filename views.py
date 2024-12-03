from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FavoriteQuote
from .serializers import Favouritequoteserializer
# Create your views here.

class RandomQuoteView(APIView):
    def get(self,request):
        url="https://api.quotable.io/random"
        response=requests.get(url).json()
        return Response(response)
class FavoriteQuoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        favorites=FavoriteQuote.objects.filter(user=request.user)
        serializer=Favouritequoteserializer(favorites,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Favouritequoteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
