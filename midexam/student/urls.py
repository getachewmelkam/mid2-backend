from django.urls import path
from . import views
urlpatterns = [
    path('list' , views.studentList.as_view()),

    path('delete/<int:pk>' , views.deleteList.as_view()),
    
]