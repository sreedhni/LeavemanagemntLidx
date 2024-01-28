from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

from Leave.models import LeaveRequest,Employee
from Leave.forms import RegstrationForm,LoginForm,EmployeeLeaveForm,AdminLeaveEditForm,UserLeaveUpdateForm

from django.contrib.auth import login
from django.shortcuts import render, redirect



class AdSignUpView(CreateView):
    template_name="adregister.html"
    model=Employee
    form_class=RegstrationForm
    success_url=reverse_lazy("signin-admin")

    def form_valid(self, form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"account creation failed")
        return super().form_invalid(form)
    
class AdSignInView(FormView):
    template_name="signinadmin.html"
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
         
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login succesfully")
                return redirect("admin")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"admin.html",{"form":form})
            



class USignUpView(CreateView):
    template_name="uregister.html"
    model=Employee
    form_class=RegstrationForm
    success_url=reverse_lazy("signin-usr")

    def form_valid(self, form):#for sendng succs msg
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self, form): #for sndng error msg
        messages.error(self.request,"account creation failed")
        return super().form_invalid(form)


class USignInView(FormView):
    template_name="signinuser.html"
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login succesfully")
                return redirect("user")
            else:
                messages.error(request,"invalid credentials")
                return redirect("user")
           




class EmployeeLeaveCreateView(CreateView):
    template_name="uleave_add.html"
    model=LeaveRequest
    form_class=UserLeaveUpdateForm
    success_url=reverse_lazy("user")

# ecs=[signin_required,is_user]

class EmployeeLeaveUpdateView(UpdateView):
    template_name="uleave_edit.html"
    model=LeaveRequest
    form_class=UserLeaveUpdateForm
    success_url=reverse_lazy("user")

# ecs=[signin_required,is_user]

def remove_leaveview(request,*args,**kwargs):
    id=kwargs.get("pk")
    LeaveRequest.objects.filter(id=id).delete()
    return redirect("user")

# ecs=[signin_required,is_user]

class ULeaveListView(ListView):
    template_name="user.html"
    model=LeaveRequest
    context_object_name="leaves"
    success_url=reverse_lazy("user")


# decs=[signin_required,is_admin]

class ALeaveListView(ListView):
    template_name="admin.html"
    model=LeaveRequest
    context_object_name="leaves"
    success_url=reverse_lazy("admin")


# decs=[signin_required,is_admin]

class ALeaveUpdateView(UpdateView):
    template_name="aleave_edit.html"
    model=LeaveRequest
    form_class=AdminLeaveEditForm
    success_url=reverse_lazy("admin")

# @signin_required
def sign_outview(request,*args,**kwargs):
    logout(request)
    return redirect("signin-admin")
