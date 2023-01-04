from django.urls import path
from . import views
urlpatterns = [
    
    path('list' , views.teacherList.as_view()),
    
    path('delete/<int:pk>' , views.teacherdelete.as_view()),
  
]