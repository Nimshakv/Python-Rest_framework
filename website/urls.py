from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create_department/', views.create_department, name='create_department'),
    path('delete_department/', views.delete_department, name='delete_department'),
    path('delete_employee/', views.delete_employee, name='delete_employee'),
]