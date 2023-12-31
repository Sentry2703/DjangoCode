from . import views
from django.urls import path

app_name = 'airport'

urlpatterns = [
    path('', views.home, name = "home"),
    path('create_emp/', views.create_emp, name = "create_emp"),
    path('create_plane/', views.create_plane, name = "create_plane"),
    path('create_flight/', views.create_flight, name = "create_flight"),
    path('list_deps/', views.list_deps, name = "list_deps"),
    path('list_emps/', views.list_emps, name = "list_emps"),
    path('list_planes/', views.list_planes, name = "list_planes"),
    path('list_flights/', views.list_flights, name = "list_flights"),
    path('list_crews/', views.list_crews, name = "list_crews"),
    path('edit_emp/', views.edit_emp, name = "edit_emp"),
    path('edit_plane/', views.edit_plane, name = "edit_plane"),
    path('edit_crew/', views.edit_crew, name = "edit_crew"),
]