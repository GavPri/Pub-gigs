from . import views
from django.urls import path


urlpatterns = [
    path('', views.GigList.as_view(), name='home')
]
