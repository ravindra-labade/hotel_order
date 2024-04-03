from django.urls import path
from .views import add_hotel, show_hotel, update_hotel, cancel_hotel


urlpatterns = [
    path('add/', add_hotel, name='add_url'),
    path('show/', show_hotel, name='show_url'),
    path('update/<int:pk>/', update_hotel, name='update_url'),
    path('cancel/<int:pk>/', cancel_hotel, name='cancel_url'),
]