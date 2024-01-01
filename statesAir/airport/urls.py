from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = "airport-home"),
    path('form/', views.form, name = "airport-form"),
    path('create_dep/', views.create_dep, name = "airport-create_dep"),
]