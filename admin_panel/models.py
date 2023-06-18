from django.db import models


class Salary_Designation(models.Model):
    salary = models.IntegerField()
    designation = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Salary_Designation.objects.all()

    def __str__(self):
        return self.designation


class Employee(models.Model):
    cnic = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    designation = models.ForeignKey(
        Salary_Designation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/employee/')

    def __str__(self):
        return self.cnic

    def register(self):
        self.save()

    def isExists(self):
        if Employee.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_employee_by_email_password(email, password):
        try:
            return Employee.objects.get(email=email, password=password)
        except:
            return False

    @staticmethod
    def get_employee_by_cnic_email(cnic, email):
        try:
            return Employee.objects.get(cnic=cnic, email=email)
        except:
            return False


class Meta:
    verbose_name_plural = "1.Employee"


class Atendence(models.Model):
    entry_attendence    = models.BooleanField(default=True)
    entry_time          = models.DateTimeField(blank=True, null=True,)
    exit_attendence     = models.BooleanField(default=True)
    exit_time           = models.DateTimeField(blank=True, null=True,)
    employee            = models.ForeignKey(Employee, on_delete=models.CASCADE)
    createdat           = models.DateTimeField(db_column='createdAt', blank=True, null=True, auto_now_add=True)
    updatedat           = models.DateTimeField(db_column='updatedAt', blank=True, null=True, auto_now=True)


class Admin(models.Model):
    cnic = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    @staticmethod
    def get_admin_by_email_password(email, password):
        try:
            return Admin.objects.get(email=email, password=password)
        except:
            return False

    @staticmethod
    def get_admin_by_cnic_email(cnic, email):
        try:
            return Admin.objects.get(cnic=cnic, email=email)
        except:
            return False
