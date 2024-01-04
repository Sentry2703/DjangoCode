from . import views
from django.urls import path

app_name = 'airport'

urlpatterns = [
    path('', views.home, name = "home"),
    path('create_dep/', views.create_dep, name = "create_dep"),
    path('list_things/', views.list_things, name = "list_things"),
]