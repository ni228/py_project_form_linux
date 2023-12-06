from django.contrib import admin
from django.urls import path, include

from blog.views import Main, BlogDetailView

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
]
