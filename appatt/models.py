from django.db import model
from django.contrib.auth.models import User



class Profile(models.Model):  #attendence app
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=False, blank=False)
    signin_time = models.DateTimeField()
    signout_time=models.DateTimeField()

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.designation)



class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(profile__designation="Employee")

class Employee(User):

    objects = EmployeeManager()
    
    def full_name(self):
        return self.first_name + " - " + self.last_name

