from . import views
from django.urls import path


urlpatterns = [
    path('departments/', views.DepartmentsNewList.as_view()),
    path('departments/<int:pk>', views.DepartmentsNewList.as_view()),
    path('employees/', views.EmployeesNewList.as_view()),
    path('employees/<int:pk>', views.EmployeesNewList.as_view()),
]