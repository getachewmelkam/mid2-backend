from django.shortcuts import render


from rest_framework import generics
from .models import employee
from .serializers import employeeserializer
class employeeList(generics.ListCreateAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeserializer
class employeedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeserializer