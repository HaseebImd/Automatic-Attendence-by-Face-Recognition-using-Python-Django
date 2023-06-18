from re import M
from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

from django.views import View
from .models import Employee, Atendence, Admin,Salary_Designation
from django.contrib.auth.models import User
import datetime
from datetime import date
from datetime import datetime
import cv2
from django.contrib.auth import authenticate

#Admin Area
from imgProcessing.process import proc

class GetLoginforAdminPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'admintemplate/login.html')

    def post(self, request, *args, **kwargs):
        # print('ps')
        # print(proc())
        return render(request, 'admintemplate/login.html')


class AdminLoginIn(View):
    return_url = None
    def get(self, request, *args, **kwargs):
        # if request.session.has_key('user'):
        #     totalEmployees = Employee.objects.all().count()
        #     return render(request, 'admintemplate/dashboard.html',{'totalEmployees': totalEmployees})
        return render(request, 'admintemplate/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        #print(email, password)
        user = Admin.get_admin_by_email_password(email=email, password=password)
        totalEmployees = Employee.objects.all().count()
        error_message = None
        #username = User.objects.get(email=email.lower()).username
        #Main_user = User.objects.get(email=email, password=password)
        if user is not None:
            #request.session['user'] = user.name
            return render(request, 'admintemplate/dashboard.html', {'totalEmployees': totalEmployees})
        # elif Main_user is not None:
        #     return render(request, 'admintemplate/dashboard.html', {'totalEmployees': totalEmployees})
        else:
            error_message = 'Email or Password Invalid!!!'
            return render(request, 'admintemplate/login.html', {'error': error_message})


# class SignUp(View):

#     def get(self, request, *args, **kwargs):
#         print("Get Called sin")
#         return render(request, 'app/signup.html')

#     def post(self, request, *args, **kwargs):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         name = request.POST.get('name')
#         print("Email : ", email)
#         print("Password : ", password)
#         print("Name : ", name)
#         message = "Your Account Created"
#         return render(request, 'app/signup.html', {"message": message})


class EmployeeDetails(View):

    def post(self, request, *args, **kwargs):
        employee = request.POST.get('cnic')
        #print(employee)
        EmployeeAttendence = Atendence.objects.filter(employee=employee)
        Employeedata = Employee.objects.get(id=employee)
        # print("Employeedata", EmployeeDetails)
        # for emp in EmployeeDetails:
        #     print("using lpp",emp.employee)
        #print("Name",Employeedata.name)
        employeData, presents , absents=  calculateEmployeeDuty(EmployeeAttendence)
        #print("Employe Data",employeData)
        context={
            'Employeedata': employeData,
            'name': Employeedata.name,
            'cnic': Employeedata.cnic,
            'designation': Employeedata.designation,
            'image': Employeedata.image,

        }
        #print("context",context)
        return render(request, 'admintemplate/employeeDetails.html', {'context': context})


class AdminDashBoard(View):
    def get(self, request, *args, **kwargs):
        totalEmployees = Employee.objects.all().count()
        return render(request, 'admintemplate/dashboard.html', {'totalEmployees': totalEmployees})

    # def post(self, request, *args, **kwargs):
    #     return render(request, 'admin/dashboard.html', {'totalEmployees': 1})


class AdminForgetPassword(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admintemplate/forgetPassword.html')

    def post(self, request, *args, **kwargs):
        cnic = request.POST.get('cnic')
        email = request.POST.get('email')
        #print(cnic,email)
        admin = Admin.get_admin_by_cnic_email(cnic=cnic, email=email)

        if admin:
            #print(admin.password)
            error_message = 'Your Password is ' + admin.password
            return render(request, 'admintemplate/forgetPassword.html', {'error': error_message})
            pass
        else:
            error_message = 'Invalid Credentials'
        return render(request, 'admintemplate/forgetPassword.html', {'error': error_message})




class AllEmployees(View):

    def get(self, request, *args, **kwargs):
        AllEmployees = Employee.objects.all()
        return render(request, 'admintemplate/allEmployees.html', {'AllEmployees': AllEmployees})


class Main(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')




class GetEployeeLoginPage(View):
    return_url = None

    def get(self, request, *args, **kwargs):
        return render(request, 'employee/login.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'employee/login.html')


class EmployeeForgetPassword(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'employee/forgetPassword.html')

    def post(self, request, *args, **kwargs):
        cnic = request.POST.get('cnic')
        email = request.POST.get('email')
        user = Employee.get_employee_by_cnic_email(cnic=cnic, email=email)

        if user:
            #print(user.password)
            error_message = 'Your Password is ' + user.password
            return render(request, 'employee/forgetPassword.html', {'error': error_message})
            pass
        else:
            error_message = 'Invalid Credentials'
        return render(request, 'employee/forgetPassword.html', {'error': error_message})



class EployeeLogin(View):
    return_url = None
    def get(self, request, *args, **kwargs):
        return render(request, 'employee/login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        #print(email, password)
        user = Employee.get_employee_by_email_password(email=email, password=password)
        print("User",user)
        if user:
            #request.session['employee'] = user.id
            EmployeeAttendence = Atendence.objects.filter(employee=user.id)
            #print("EmployeeAttendence", EmployeeAttendence)
            Employeedata = Employee.objects.get(id=user.id)
            #print("Employeedata",Employeedata)
            employeData, presents , absents=calculateEmployeeDuty(EmployeeAttendence)
            #print("employeData",employeData)
            context = {
                'Employeedata': employeData,
                'name': Employeedata.name,
                'cnic': Employeedata.cnic,
                'designation': Employeedata.designation,
                'image': Employeedata.image,

            }
            #print("context", context)
            return render(request, 'employee/employeeDetails.html', {'context': context})

        else:
            error_message = 'Email or Password Invalid!!!'

        return render(request, 'employee/login.html', {'error': error_message})


class SearchEmployee(View):
    return_url = None

    def get(self, request, *args, **kwargs):
        return render(request, 'admintemplate/searchEmployee.html')


class Search(View):
    return_url = None

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        #("name",name)
        AllEmployees = Employee.objects.filter(name__contains=name)
        return render(request, 'admintemplate/searchEmployee.html', {'AllEmployees': AllEmployees})


class CalculateSalary(View):
    return_url = None

    def get(self, request, *args, **kwargs):
        AllEmployees = Employee.objects.all()
        return render(request, 'admintemplate/calculateSalary.html', {'AllEmployees': AllEmployees})

def getStatus(duty_hours):
    status=False
    if duty_hours >= 5.8:
        status = True
    else:
        status = False
    return status

def calculateEmployeeDuty(EmployeeAttendence):

    employeData=[]
    oneTimeData=[]
    presents=0
    absents=0
    #print("Control in Calculate ")
    #print("EmployeeAttendence",EmployeeAttendence)
    dutyStartTime='empty'
    dutyExitTime=''
    dutyHours=0
    previousDay=''
    prevousMonth=''
    currentDay=''
    currentMonth=''
    arrayLength= len(EmployeeAttendence)
    counter=0
    # for attendence in EmployeeAttendence:
    #     if attendence.entry_attendence == True and attendence.exit_attendence == True:
    #         entry_time=attendence.entry_time.time().strftime("%H")
    #         exit_time  = attendence.exit_time.time().strftime("%H")
    #         duty_hours = int(exit_time) - int(entry_time)
    #         status=False
    #         if duty_hours >= 5.8:
    #             status = True
    #         else:
    #             status = False
    #         if status==True:
    #             presents = presents+1
    #         else:
    #             absents=absents+1

    #         employeData.append({'entry_time': attendence.entry_time, 'entry_attendence': attendence.entry_attendence, 'exit_time': attendence.exit_time, 'exit_attendence': attendence.exit_attendence, 'total_time': int(duty_hours), 'status': status})
    #     elif attendence.entry_attendence == True and attendence.exit_attendence == False:
    #         employeData.append({'entry_time': attendence.entry_time, 'entry_attendence': attendence.entry_attendence, 'exit_time': attendence.exit_time, 'exit_attendence': attendence.exit_attendence, 'total_time': 0, 'status': False})
    #print("employeData in functiion", employeData)
    #print("lenght",len(EmployeeAttendence))
    for attendence in EmployeeAttendence:
        counter=counter+1
        mydate = attendence.createdat
        currentMonth=mydate.month
        currentDay=mydate.day
        #print("createdat",attendence.createdat)
        # print("Inside Function")
        # print("currentMonth",currentMonth)
        # print("currentDay",currentDay)
        if dutyStartTime=='empty':
            #print("Inside First If")
            if attendence.entry_attendence == True and attendence.exit_attendence == True:
                dutyStartTime=attendence.entry_time
                dutyExitTime=attendence.exit_time
                entry_time=attendence.entry_time.time().strftime("%H")
                exit_time  = attendence.exit_time.time().strftime("%H")
                dutyHours = int(exit_time) - int(entry_time)
                mydate = attendence.createdat
                prevousMonth=mydate.month
                previousDay=mydate.day
                if counter==arrayLength:
                    status=getStatus(dutyHours)
                    employeData.append({'entry_time': dutyStartTime, 'entry_attendence': True, 'exit_time': dutyExitTime, 'exit_attendence': True, 'total_time': dutyHours, 'status': status})
                    if status==True:
                        presents=presents+1
                    else:
                        absents=absents+1
            elif attendence.entry_attendence == True and attendence.exit_attendence == False:
                absents=absents+1
                employeData.append({'entry_time': attendence.entry_time, 'entry_attendence': attendence.entry_attendence, 'exit_time': attendence.exit_time, 'exit_attendence': attendence.exit_attendence, 'total_time': 0, 'status': False})


        elif currentMonth==prevousMonth and currentDay==previousDay:
            #print("Haseeb Condition")
            if attendence.entry_attendence == True and attendence.exit_attendence == True:
                dutyExitTime=attendence.exit_time
                entry_time=attendence.entry_time.time().strftime("%H")
                exit_time  = attendence.exit_time.time().strftime("%H")
                #print("dutyHours",dutyHours)
                time = int(exit_time) - int(entry_time)
                #print("time",time)
                dutyHours= int(dutyHours)+int(time)
                #print("dutyHours",dutyHours)
                status=getStatus(dutyHours)
                if counter==arrayLength:
                    employeData.append({'entry_time': dutyStartTime, 'entry_attendence': True, 'exit_time': dutyExitTime, 'exit_attendence': True, 'total_time': dutyHours, 'status': status})
                    if status==True:
                        presents=presents+1
                    else:
                        absents=absents+1
            elif attendence.entry_attendence == True and attendence.exit_attendence == False:
                status=getStatus(dutyHours)
                if status==True:
                        presents=presents+1
                else:
                    absents=absents+1
                employeData.append({'entry_time': dutyStartTime, 'entry_attendence': True, 'exit_time': dutyExitTime, 'exit_attendence': True, 'total_time': dutyHours, 'status': status})
        else:
            #print("Ladt else")
            status=getStatus(dutyHours)
            if status==True:
                        presents=presents+1
            else:
                absents=absents+1
            employeData.append({'entry_time': dutyStartTime, 'entry_attendence': True, 'exit_time': dutyExitTime, 'exit_attendence': True, 'total_time': dutyHours, 'status': status})
            dutyStartTime=attendence.entry_time
            dutyExitTime=attendence.exit_time
            mydate = attendence.createdat
            prevousMonth=mydate.month
            previousDay=mydate.day
            entry_time=attendence.entry_time.time().strftime("%H")
            exit_time  = attendence.exit_time.time().strftime("%H")
            dutyHours = int(exit_time) - int(entry_time)
            #print("employeData",employeData)
            #print("dutyStartTime",dutyStartTime)
            status=getStatus(dutyHours)
            if counter==arrayLength:
                employeData.append({'entry_time': dutyStartTime, 'entry_attendence': True, 'exit_time': dutyExitTime, 'exit_attendence': True, 'total_time': dutyHours, 'status': status})
                if status==True:
                        presents=presents+1
                else:
                    absents=absents+1

    result=list(reversed(employeData))
    return result, presents, absents

class Calculate(View):
    def post(self, request, *args, **kwargs):
        cnic = request.POST.get('cnic')
        if cnic=='':
            AllEmployees = Employee.objects.all()
            return render(request, 'admintemplate/calculateSalary.html', {'AllEmployees': AllEmployees})
        print("name", cnic)
        try:
            EmployeeOne = Employee.objects.get(cnic=cnic)
            if EmployeeOne:
                attendence = Atendence.objects.all()
                month=''
                salaryObject = Salary_Designation.objects.get(designation=EmployeeOne.designation)
                designationSalary=salaryObject.salary
                perDaySalary=int(designationSalary/30)

                #print("Salary", designationSalary)
                # for a in attendence:
                #     if a.employee == EmployeeOne:
                #         date = a.createdat
                #         month = datetime.date(1900, date.month, 1).strftime('%B')
                #         print("a",a,"\n")
                #         if a.attendence == True:
                #             presents = presents+1
                #         else:
                #             absents=absents+1
                # #print("presents", presents)
                #print("absents", absents)
                EmployeeAttendence = Atendence.objects.filter(employee=EmployeeOne)
                print("EmployeeAttendence", EmployeeAttendence)
                employeData, presents , absents= calculateEmployeeDuty(EmployeeAttendence)
                Employeedata = Employee.objects.get(id=EmployeeOne.id)
                print("employeData",employeData)
                # print("Employeedata", EmployeeDetails)
                # for emp in EmployeeDetails:
                #     print("using lpp",emp.employee)
                # print("Name", Employeedata.name)
                # print("total sALARY", designationSalary)
                # print("Per day Salary",perDaySalary)
                # print("TOTAL SASLARY",(int(perDaySalary*presents)))
                thisEmployeeSalary = (int(perDaySalary*presents))
                context = {
                    'Employeedata': employeData,
                    'name': Employeedata.name,
                    'cnic': Employeedata.cnic,
                    'designation': Employeedata.designation,
                    'month':month,
                    'salary': thisEmployeeSalary,
                    'absents':absents,
                    'presents':presents,
                    'perDaySalary':perDaySalary,
                    'image': Employeedata.image,

                }
                return render(request, 'admintemplate/employeeSalary.html', {'context': context})
        except:
            AllEmployees = Employee.objects.all()
            return render(request, 'admintemplate/calculateSalary.html', {'AllEmployees': AllEmployees})


class markAttendence(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')

    def post(self, request, *args, **kwargs):
        imgURL = request.POST.get('link')
        import urllib.request
        urllib.request.urlretrieve(imgURL, "D:/Afghani Project/Afghani Project/Afghani Project/kankor/imgProcessing/user.jpg")
        import datetime
        dt = datetime.datetime.today()
        currentDay=dt.day
        currentMonth=dt.month
        result = proc()
        if result:
            employee = Employee.objects.get(cnic=result)
            cnic = employee.cnic
            name = employee.name
            attendence = Atendence.objects.filter(employee=employee,createdat__day=currentDay).order_by('-id')
            print(attendence)
            if attendence:
                for a in attendence:
                    # mydate = a.createdat
                    # month=mydate.month
                    # day=mydate.day
                    # print(a)
                    # print("Day",a.entry_attendence)
                    # if currentMonth == month and currentDay == day:
                    if a.entry_attendence==True and a.exit_attendence==True:
                        print("First If Executed")
                        attendnece = Atendence(entry_attendence=True,entry_time=dt,exit_attendence=False, employee=employee)
                        attendnece.save()
                        error_message = name
                        return render(request, 'main.html', {'welcome': error_message})
                        error_message = name
                        return render(request, 'main.html', {'alreadymarked': error_message})
                    elif a.entry_attendence == True and a.exit_attendence == False:
                        print("elIf Executed")
                        a.exit_attendence=True
                        a.exit_time=dt
                        a.save()
                        error_message = name
                        return render(request, 'main.html', {'exit': error_message})
                    else:
                        print("First Else Executed")
                        attendnece = Atendence(entry_attendence=True,entry_time=dt,exit_attendence=False, employee=employee)
                        attendnece.save()
                        error_message = name
                        return render(request, 'main.html', {'welcome': error_message})
            else:
                print("2nd Else executed")
                attendnece = Atendence(entry_attendence=True,entry_time=dt,exit_attendence=False, employee=employee)
                attendnece.save()
                error_message = name
                return render(request, 'main.html', {'welcome': error_message})
        else:
            error_message="Could Not Recognize You"
            return render(request, 'main.html', {'error': error_message})



class Salaries(View):
    
    def get(self, request, *args, **kwargs):
        employeesFinalaDta=[]
        employees=Employee.objects.all()
        totalSalary=0
        for employee in employees:
            EmployeeAttendence = Atendence.objects.filter(employee=employee)
            employeData, presents , absents=  calculateEmployeeDuty(EmployeeAttendence)
            salaryObject = Salary_Designation.objects.get(designation=employee.designation)
            designationSalary=salaryObject.salary
            perDaySalary=int(designationSalary/30)
            thisEmployeeSalary = (int(perDaySalary*presents))
            totalSalary=totalSalary+thisEmployeeSalary
            employeesFinalaDta.append({
                    'id':employee.id,
                    'name': employee.name,
                    'cnic': employee.cnic,
                    'designation': employee.designation,
                    'salary': thisEmployeeSalary,
                    'image': employee.image,
                    'email': employee.email,
                    'city': employee.city,
                    'address': employee.address,
                    'phone': employee.phone,
                    'presents':presents,
                    'absents':absents
                    
                })
            
        context={
            'employeesFinalaDta':employeesFinalaDta,
            'totalSalary':totalSalary

        }
        return render(request, 'admintemplate/emplpyeeSalaries.html', {'context': context})
