from django.urls import path
from . import views

urlpatterns = [
    path('fb/',views.fn_facebook),
    path('loginpage/',views.fn_fb),
]