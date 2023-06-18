from django.contrib import admin

from .models import Employee, Salary_Designation, Atendence, Admin


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['cnic', 'name', 'email', 'city',
                    'address', 'phone', 'designation', 'password']


class SalaryDesignationAdmin(admin.ModelAdmin):
    list_display = ['salary', 'designation']


class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['entry_attendence', 'entry_time',
                    'exit_attendence', 'exit_time', 'employee', 'createdat']

class AdminAdmin(admin.ModelAdmin):
    list_display = ['cnic', 'name', 'email', 'city',
                    'address', 'phone','password']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salary_Designation, SalaryDesignationAdmin)
admin.site.register(Atendence, AttendenceAdmin)
admin.site.register(Admin, AdminAdmin)
