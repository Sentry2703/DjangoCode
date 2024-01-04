from . import views
from django.urls import path

app_name = 'airport'

urlpatterns = [
    path('', views.home, name = "home"),
    path('create_dep/', views.create_dep, name = "create_dep"),
    path('list_things/', views.list_things, name = "list_things"),
    path('create_emp/', views.create_emp, name = "create_emp"),
    path('create_plane/', views.create_plane, name = "create_plane"),
    path('create_flight/', views.create_flight, name = "create_flight"),
]