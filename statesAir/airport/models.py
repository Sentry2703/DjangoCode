from django.db import models

# Create your models here.
class Plane(models.Model):
    plane_id = models.IntegerField(primary_key=True)
    plane_type = models.TextChoices('PlaneType', 'Cargo Passenger Private')
    capacity = models.IntegerField()
    plane_status = models.CharField(max_length=50)
    plane_airline = models.CharField(max_length=50)
    commission_date = models.DateField()

    def __str__(self):
        return f"This {self.plane_type} is owned by {self.plane_airline} and has a capacity of {self.capacity}."
    
class Flight(models.Model):
    flight_id = models.IntegerField(primary_key=True)
    flight_status = models.TextChoices('FlightStatus', 'OnTime Delayed Cancelled')
    flight_origin = models.CharField(max_length=50)
    flight_destination = models.CharField(max_length=50)
    flight_departure = models.DateTimeField()
    flight_arrival = models.DateTimeField()
    flight_plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return f"Flight {self.flight_id} is a {self.flight_plane} from {self.flight_origin} to {self.flight_destination}."
    
class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.TextChoices('DepartmentName', 'Pilot FlightAttendant Mechanic GroundCrew Concessions Janitor Security Admin')
    department_location = models.CharField(max_length=50)

    def __str__(self):
        return f"Department {self.department_id} is the {self.department_name} department."
    
class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_fname = models.CharField(max_length=20)
    employee_lname = models.CharField(max_length=20)
    employment_date = models.DateField()
    employee_role = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return f"Employee {self.employee_id} is a {self.employee_role} and makes ${self.salary} a year."
    
class Crew(models.Model):
    crew_id = models.IntegerField(primary_key=True)
    employees = models.ManyToManyField(Employee) 

    def __str__(self):
        return f"Crew {self.crew_id} is made up of {', '.join(str(employee.employee_fname, employee.employee_lname) for employee in self.employees.all())}."