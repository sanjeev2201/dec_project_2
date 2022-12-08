from django.urls import path
from . import views
urlpatterns = [

    path('list/', views.employees_list, name='employees-list'),
    path('create/', views.create_employee, name='create-employee'),
    path('edit/<int:pk>', views.edit_employee, name='edit-employee'),
    path('delete/<int:pk>', views.delete_employee, name='delete-employee'),
]
