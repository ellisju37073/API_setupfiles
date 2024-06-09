from django.db import models

# Create your models here.

# Define a Students model representing student information
class Students(models.Model):
    # Field to store the first name of the student, with a maximum length of 200 characters
    first_name = models.CharField(max_length=200)
    
    # Field to store the last name of the student, with a maximum length of 200 characters
    last_name = models.CharField(max_length=200)
    
    # Field to store the address of the student, with a maximum length of 200 characters
    address = models.CharField(max_length=200)
    
    # Field to store the roll number of the student, as an integer
    roll_number = models.IntegerField()
    
    # Field to store the mobile number of the student, with a maximum length of 10 characters
    mobile = models.CharField(max_length=10)

    # Method to return a string representation of the student, combining first and last names
    def __str__(self):
        return self.first_name + " " + self.last_name
