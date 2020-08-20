from django.urls import path, include
from Biblioteca_3.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='home')
]
