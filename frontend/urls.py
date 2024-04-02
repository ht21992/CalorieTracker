from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_food_info/', views.get_food_info, name='get_food_info'),
]
