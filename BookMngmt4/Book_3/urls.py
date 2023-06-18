from django.urls import path
from Book_3 import views

app_name = 'Book_3'

urlpatterns = [
    path('Add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('display/', views.display, name='display'),
    path('', views.display, name='display'),
]
