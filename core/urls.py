from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('book/', views.BookListView.as_view()),
    # path('book/<int:pk>/', views.BookDetailView.as_view()),
    # path('book/create/', views.BookCreateView.as_view()),
    # path('book/<int:pk>/update/', views.BookUpdateView.as_view()),
    # path('book/<int:pk>/delete/', views.BookDeleteView.as_view()),

    # path('reader/', views.ReaderListSet.as_view()),
    # path('reader/<int:pk>/', views.ReaderDetailView.as_view()),
    #
    # path('author/', views.AuthorView.as_view()),
    # path('author/<int:pk>/', views.AuthorDetailView.as_view()),

]
