from . import views
from django.urls import path


urlpatterns = [
    path('', views.GigList.as_view(), name='home'),
    path('reservations/', views.ReservationList.as_view(), name='reservations')
]
