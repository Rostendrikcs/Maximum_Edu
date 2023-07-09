from django.urls import path
from .views import rep

urlpatterns = [
    path('', rep)

]