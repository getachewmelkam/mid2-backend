from django.shortcuts import render

from rest_framework import generics
from .models import teacher
from .serializers import teacherserializer
class teacherList(generics.ListCreateAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializer
class teacherdelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializer
