from django.shortcuts import render
from rest_framework import generics
from .models import student
from .serializers import studentserializer
class studentList(generics.ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializer
class deleteList(generics.RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializer









# Create your views here.
