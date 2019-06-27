from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/<int:id>', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('abc/<int:id>', views.abc, name='abc'),
    path('add_quot/<int:id>', views.add_quot, name='add_quot'),
]