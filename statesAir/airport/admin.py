from django.contrib import admin
from .models import Plane, Flight, Department, Employee, Crew

# Register your models here.
admin.site.site_header = "StatesAir Administration"
admin.site.register(Plane)
admin.site.register(Flight)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Crew)