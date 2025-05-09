from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_login, name='vendor_login'),
    path('services/', views.services_view, name='services'),
]