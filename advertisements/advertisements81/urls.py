from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path("top-sellers/",top_sellers),
]