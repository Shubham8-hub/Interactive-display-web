"""
This is the url file for the mainpg app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]