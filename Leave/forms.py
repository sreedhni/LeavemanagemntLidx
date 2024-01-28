from django import forms
from Leave.models import Employee,LeaveRequest
 
from django.contrib.auth.forms import UserCreationForm


class RegstrationForm(forms.ModelForm):
     class Meta:
          model=Employee
          fields=["username","email","password","role"]

class LoginForm(forms.ModelForm):
      class Meta:
          model=Employee
          fields=["username","password"]

    

class EmployeeLeaveForm(forms.ModelForm):
    username=forms.CharField()
    class Meta:
          model=LeaveRequest
          fields="__all__"
          widgets={
            "leave_from":forms.DateInput(attrs={"type":"date"}),
            "leave_to":forms.DateInput(attrs={"type":"date"}),
        }


class UserLeaveUpdateForm(forms.ModelForm):
    class Meta:
          model=LeaveRequest
          exclude=("username",)
          widgets={
            "leave_from":forms.DateInput(attrs={"type":"date"}),
            "leave_to":forms.DateInput(attrs={"type":"date"}),
        }




          
class EmployeeLeaveCreateForm(forms.Form):
    class Meta:
          model=LeaveRequest
          exclude=("username",)

          widgets={
            "leave_from":forms.DateInput(attrs={"type":"date"}),
            "leave_to":forms.DateInput(attrs={"type":"date"}),
        }

class AdminLeaveEditForm(forms.ModelForm):
    class Meta:
          model=LeaveRequest
          exclude=("employee","reason","leave_from","leave_to","username")

