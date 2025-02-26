from django.urls import path
from .views import *

urlpatterns = [
    path('',Login.as_view(), name="login"),
    path('logout/',Logout.as_view(), name="logout"),
]