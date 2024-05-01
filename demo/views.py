
# from django.http import HttpResponse
# from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication


# def first(request):
#       books = Book.objects.all()
#       # return render(request, 'first_temp.html', {"data":"This a data from Views"})
#       return render(request, 'first_temp.html', {"books":books})

class BookViewSet(viewsets.ModelViewSet):
      serializer_class= BookSerializer
      queryset=Book.objects.all()
      authentication_classes= (TokenAuthentication)