"""
URL configuration for EmployeeLeave project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Leave import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('ad/register/',views.AdSignUpView.as_view(),name="ad-signup"),
        path('ad/login/',views.AdSignInView.as_view(),name="signin-admin"),

        path('usr/register/',views.USignUpView.as_view(),name="u-signup"),
        path("usr/login",views.USignInView.as_view(),name="signin-usr"),

        path('leave/add/',views.EmployeeLeaveCreateView.as_view(),name="leave-add"),
        path('leave/<int:pk>/edit/',views.EmployeeLeaveUpdateView.as_view(),name="leave-edit"),
        path('leave/<int:pk>/delete/',views.remove_leaveview,name="leave-remove"),
   
        path('ad/leave/<int:pk>/edit/',views.ALeaveUpdateView.as_view(),name="aleave-edit"),


        path('uleave/all/',views.ULeaveListView.as_view(),name="user"),
        path('aleave/all/',views.ALeaveListView.as_view(),name="admin"),
        path('logout',views.sign_outview,name="log-out")

   


]

