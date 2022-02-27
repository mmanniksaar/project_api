from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
#    path('', views.getRoutes),
    path('notes/', views.getNotes), # link -näitab kõiki märkmeid
    path('notes/create/', views.createNote),  # link - loob uue märkme
    path('notes/<str:pk>/', views.getNote), # link -näitab ühte märkust
    path('notes/<str:pk>/update/', views.updateNote), # link -uuendab märget
    path('notes/<str:pk>/delete/', views.deleteNote), # link -kustutab märkme
]