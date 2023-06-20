from django.core.validators import RegexValidator
from django.db import models


# Create your models here.


class Students(models.Model):
    Name = models.CharField(max_length=100, null=False, blank=False)
    Email = models.EmailField(max_length=200, null=False, blank=True)
    Address = models.CharField(max_length=200, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True, default="")
    DistrictName = models.CharField(max_length=100, null=True, verbose_name="DistrictName", blank=True)
    Course = models.CharField(max_length=100, verbose_name="Course", null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Mobile = models.CharField(validators=[phone_regex], max_length=12, blank=False, null=True)
    trainer_choice = {
        ('Neethu', 'Neethu'),
        ('Gopika', 'Gopika'),
        ('Anagha', 'Anagha')
    }
    Trainer = models.CharField(max_length=6, null=True, choices=trainer_choice)
    StartDate = models.DateField(null=True)
    EndDate = models.DateField(null=True)
    City = models.CharField(max_length=50, null=True, verbose_name="City")
    Batch = models.CharField(max_length=200, null=True)
    DOB = models.DateField(verbose_name="Date of Birth", null=True)
    PIN = models.PositiveIntegerField(null=True, blank=True)
    Active = models.BooleanField(default=False)
    Registered = models.BooleanField(default=False)
    Fees = models.CharField(max_length=100, null=True, verbose_name="Fees")
    SearchFields = ['Name']

    def __str__(self):
        return self.Name

    # def __str__(self):
    #     return f" {self.Name} with course {self.Course}"


class FeesReceipt(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('cheque', 'Cheque'),
    ]

    COLLECTED_TO_ACCOUNT_CHOICES = [
        ('oneteam ac 1', 'Oneteam ac 1'),
        ('oneteam ac 2', 'Oneteam ac 2'),
        ('oneteam ac 3', 'Oneteam ac 3'),
    ]
    Name = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
    payment_date = models.DateField()
    receipt_number = models.CharField(max_length=50)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    collected_to_account = models.CharField(max_length=100, choices=COLLECTED_TO_ACCOUNT_CHOICES)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    description = models.TextField(null=True)
    receipt_image = models.ImageField(upload_to='receipts/', null=True)

    def __str__(self):
        return self.receipt_number


class FeeDetails(models.Model):
    CHOICES = (
        ('one_times', 'One Time'),
        ('two_times', 'Two Times'),
        ('three_times', 'Three Times')
    )
    Name = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
    selection_type = models.CharField(null=True, max_length=20, choices=CHOICES)
    first_pay = models.DateField(null=True, blank=True)
    first_pay_amount = models.IntegerField(null=True, blank=True)
    second_pay = models.DateField(null=True, blank=True)
    second_pay_amount = models.IntegerField(null=True, blank=True)
    third_pay = models.DateField(null=True, blank=True)
    third_pay_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Fee Details of {self.Name}"

    def save(self, *args, **kwargs):
        if self.selection_type == 'one_times':
            self.second_pay = None
            self.second_pay_amount = None
            self.third_pay = None
            self.third_pay_amount = None
        elif self.selection_type == 'two_times':
            self.third_pay = None
            self.third_pay_amount = None

        super().save(*args, **kwargs)
