from . import views
from django.urls import path

app_name = 'airport'

urlpatterns = [
    path('', views.home, name = "home"),
    path('form/', views.form, name = "form"),
    path('create_dep/', views.create_dep, name = "create_dep"),
]