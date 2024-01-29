from django.db import models
from django.db import models

from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    role_choices = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]
    role = models.CharField(max_length=10, choices=role_choices)
    def __str__(self):
        return self.username
    

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reason = models.TextField()
    leave_from = models.DateField()
    leave_to = models.DateField()
    status_choices = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    
    def __str__(self):
        return self.employee.username
        
    @property
    def username(self):
        qs=self.employee_set.all()
        return qs
 





