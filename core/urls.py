from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book', views.book),
    path('reader', views.reader),
    path('author', views.author),
]
