from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('home/', views.home, name = "home"),
    path('form/', views.form, name = "form"),
    path('getform/', views.form_submit, name = "getform")
]