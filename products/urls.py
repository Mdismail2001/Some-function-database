from django.urls import path
from . import views

urlpatterns = [
    path('', views.view, name='view_all_products'),
]
