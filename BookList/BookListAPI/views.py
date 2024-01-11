from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Books

# Create your views here.

@api_view(['GET', 'POST'])
def books(request):
    return Response('list of books', status = status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if author:
            return Response({'message': f"List of the books by {author}"}, status = status.HTTP_200_OK)
        
        return Response({'message': "List of the books"}, status = status.HTTP_200_OK)
    
    def post(self, request):
        author = request.data.get('author')
        title = request.data.get('title')
        description = request.data.get('description')
        if author and title and description:
            a = Books(author = author, title = title, description = description)
            a.save()
            return Response({'message': f"Book {title} created"}, status = status.HTTP_201_CREATED)
    
class Book(APIView):
    def get(self, request, pk):
        return Response({'message': f"Book {pk}, {Books.objects.get(pk = pk)}"}, status = status.HTTP_200_OK)
    
    def put(self, request, id):
        return Response({"Title": request.data.get('title')}, status = status.HTTP_200_OK)