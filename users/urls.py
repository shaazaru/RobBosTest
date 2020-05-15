from django.urls import path
from users import views
from .views import RegistrationAPI
from django.views.generic import View

urlpatterns = [
    path('register/', views.RegistrationAPI.as_view()),
]
