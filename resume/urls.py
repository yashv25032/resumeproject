from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.Myresume,name='resume'),
    path('<int:pk>',views.candilist,name='candi'),
]