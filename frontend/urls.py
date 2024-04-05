from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_food_info/', views.get_food_info, name='get_food_info'),
    path('get_partial_view/', views.get_partial_view, name='get_partial_view'),
    path('predict_status/', views.predict_status, name='predict_status'),
]
