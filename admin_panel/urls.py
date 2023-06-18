"""kankor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import AdminDashBoard, AdminLoginIn, EmployeeDetails, AllEmployees, EployeeLogin, Main, GetEployeeLoginPage, GetLoginforAdminPage, SearchEmployee, Search, CalculateSalary, Calculate, EmployeeForgetPassword, AdminForgetPassword, markAttendence,Salaries
urlpatterns = [

    path('', Main.as_view()),

    path('AdminLogin', GetLoginforAdminPage.as_view()),

    path('Admin', AdminLoginIn.as_view()),
    path('AdminForgetPassword', AdminForgetPassword.as_view()),

    path('details', EmployeeDetails.as_view()),

    path('dashboard', AdminDashBoard.as_view()),
    path('allEmployees', AllEmployees.as_view()),

    path('EmployeeLogin', GetEployeeLoginPage.as_view()),

    path('Employee', EployeeLogin.as_view()),
    path('EmployeeForgetPassword',EmployeeForgetPassword.as_view()),

    path('searchEmployee', SearchEmployee.as_view()),
    path('search', Search.as_view()),

    path('CalculateSalary', CalculateSalary.as_view()),
    path('calculate', Calculate.as_view()),

    path('salaries', Salaries.as_view()),

    path('markAttendence', markAttendence.as_view())

    




]
