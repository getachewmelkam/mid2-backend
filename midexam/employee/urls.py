from django.urls import path
from . import views
urlpatterns = [
  
    path('list' , views.employeeList.as_view()),
    path('delete/<int:pk>' , views.employeedelete.as_view()),
]