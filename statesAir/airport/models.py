from django.db import models

# Create your models here.
class Plane(models.Model):
    class PlaneType(models.TextChoices):
        CARGO = 'Cargo',
        PASSENGER = 'Passenger',
        PRIVATE = 'Private'
    class PlaneStatus(models.TextChoices):
        ACTIVE = 'Active',
        INACTIVE = 'Inactive',
        DECOMMISSIONED = 'Decommissioned',
        REPAIR = 'Repair',
    plane_id = models.IntegerField(primary_key=True)
    plane_type = models.TextField(choices = PlaneType.choices, default='Passenger')
    capacity = models.IntegerField()
    plane_status = models.TextField(choices = PlaneStatus.choices, default='Active')
    plane_airline = models.CharField(max_length=50)
    commission_date = models.DateField()

    def __str__(self):
        return f"{self.plane_id} - {self.plane_airline} - {self.capacity}."
    
class Flight(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    flight_status = models.TextChoices('FlightStatus', 'OnTime Delayed Cancelled')
    flight_origin = models.CharField(max_length=50)
    flight_destination = models.CharField(max_length=50)
    flight_departure = models.DateTimeField()
    flight_arrival = models.DateTimeField()
    flight_plane = models.ForeignKey(Plane, on_delete=models.CASCADE, )

    def __str__(self):
        return f"Flight {self.flight_id} is a {self.flight_plane} from {self.flight_origin} to {self.flight_destination}."
    
class Department(models.Model):
    class DepartmentName(models.TextChoices):
        PILOT = 'Pilot', 'Pilot'
        FLIGHT_ATTENDANT = 'Flight Attendant', 'Flight Attendant'
        MECHANIC = 'Mechanic', 'Mechanic'
        GROUND_CREW = 'Ground Crew', 'Ground Crew'
        CONCESSIONS = 'Concessions', 'Concessions'
        JANITOR = 'Janitor', 'Janitor'
        SECURITY = 'Security', 'Security'
        ADMIN = 'Admin', 'Admin'
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.TextField(choices=DepartmentName.choices, default='Admin', unique=True)
    dept_location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.dept_name}"
    
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_fname = models.CharField(max_length=20)
    emp_lname = models.CharField(max_length=20)
    emp_date = models.DateField()
    emp_role = models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_sal = models.IntegerField()

    def __str__(self):
        return f"Employee {self.emp_id} - {self.emp_fname} {self.emp_lname}: {self.emp_role}."
    
class Crew(models.Model):
    crew_id = models.IntegerField(primary_key=True)
    crew_staff = models.ManyToManyField(Employee, limit_choices_to={'emp_role__dept_name': 'Pilot', 'emp_role__dept_name': 'FlightAttendant'}) 

    def __str__(self):
        return f"Crew {self.crew_id} is made up of {', '.join(str(employee.emp_fname + ' ' +  employee.emp_lname) for employee in self.crew_staff.all())}."