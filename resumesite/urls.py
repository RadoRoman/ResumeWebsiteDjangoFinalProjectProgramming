from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # setting our site's url
]
