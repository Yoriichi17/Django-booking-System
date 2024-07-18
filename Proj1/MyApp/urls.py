# MyApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_ticket/<int:event_id>/', views.book_ticket, name='book_ticket'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),  # Ensure this line is correct
]
