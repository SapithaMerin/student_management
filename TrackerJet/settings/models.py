from django.core.validators import RegexValidator
from django.db import models
from django.utils.html import format_html


# Create your models here.


class Companies(models.Model):
    Companies = models.CharField(max_length=200, blank=False, null=False)
    Address1 = models.CharField(max_length=200, blank=True, )
    Address2 = models.CharField(max_length=200, blank=True)
    Address3 = models.CharField(max_length=200, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone = models.CharField(validators=[phone_regex], max_length=12, blank=False, null=True)
    Email = models.EmailField(max_length=200, null=False, blank=True)
    Website = models.CharField(max_length=200, blank=True, null=False)
    Logo = models.ImageField(upload_to="image", null=True)
    Active = models.BooleanField(default=False)
    DisplayFields = ['Companies', 'Address1', 'Phone', 'Email', 'Website', 'Active']

    class Meta:
        verbose_name = "Companies"
        ordering = ['Companies']

    def __str__(self):
        return self.Companies


class State(models.Model):
    StateName = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "states"
        ordering = ['StateName']

    def __str__(self):
        return self.StateName


class District(models.Model):
    DistrictName = models.CharField(max_length=50, null=True, verbose_name="DistrictName", blank=True)
    StateName = models.ForeignKey(State, on_delete=models.CASCADE, null=True, verbose_name="StateName")
    DisplayFields = ['DistrictName', 'StateName']

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"
        ordering = ['DistrictName']

    def __str__(self):
        return self.DistrictName


class Branch(models.Model):
    Branch = models.CharField(max_length=100, null=True)
    Address = models.CharField(max_length=200, blank=True)
    Street = models.CharField(max_length=100, null=True, blank=True)
    State = models.ForeignKey(State, on_delete=models.CASCADE, null=False, blank=False)
    District = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    Pincode = models.PositiveIntegerField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone = models.CharField(validators=[phone_regex], max_length=12, blank=False, null=True)
    Email = models.EmailField(max_length=200, null=False, blank=True)
    DisplayFields = ['Branch', 'Address', 'Street', 'State', 'District', 'Pincode', 'Phone', 'Email']

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
        ordering = ['Branch']

    def __str__(self):
        return self.Branch


class Course(models.Model):
    CourseName = models.CharField(max_length=100, blank=True, null=True)
    CourseCode = models.CharField(max_length=100, blank=True, null=True)
    Active = models.BooleanField(default=False)
    Fees = models.CharField(max_length=20, blank=True, null=True)
    Syllabus = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.CourseName


class Batch(models.Model):
    trainer_choice = {
        ('Neethu', 'Neethu'),
        ('Gopika', 'Gopika'),
        ('Anagha', 'Anagha')
    }

    CourseName = models.CharField(max_length=100, null=True, verbose_name="CourseName")
    BatchName = models.CharField(max_length=200, null=True)
    Trainer = models.CharField(max_length=6, null=True, choices=trainer_choice)
    StartDate = models.DateField(null=True)
    EndDate = models.DateField(null=True)
    Closed = models.BooleanField(default=False)
    Active = models.BooleanField(default=False)
    DisplayFields = ['CourseName', 'BatchName', 'Trainer', 'StartDate', 'EndDate', 'Closed', 'Active']

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"

    def __str__(self):
        return self.CourseName


class CourseFees(models.Model):
    fees_type_choice = {
        ('Three Time', 'Three Time'),
        ('Two Time', 'Two Time'),
        ('One Time', 'One Time'),
        ('Registration', 'Registration')
    }

    course_choice = {
        ('Python', 'Python'),
        ('DM', 'DM'),
        ('Testing', 'Testing')
    }
    CourseName = models.CharField(max_length=100, null=True, verbose_name="CourseName")
    FeesType = models.CharField(max_length=100, null=True, verbose_name="FeesType", choices=fees_type_choice)
    Amount = models.CharField(max_length=10, null=True, verbose_name="Amount")
    Tax = models.CharField(max_length=10, null=True, verbose_name="Tax")
    InstallmentPeriod = models.CharField(max_length=10, null=True, verbose_name="Installment Period")
    DisplayFields = ['FeesType', 'Amount', 'Tax', 'InstallmentPeriod']
    SearchFields = ['CourseName']

    def __str__(self):
        return f"Course Fees of {self.CourseName}"

