from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import NoReverseMatch
from django.utils.html import format_html
from django.urls import reverse

from .models import *
# Register your models here.


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    search_fields = Students.SearchFields
    list_display = ['Name', 'Trainer', 'Mobile', 'display_course', 'fees', 'Registered', 'Active']
    fieldsets = ('Personal Details', {'fields': (('Name', 'Gender'), ('Email', 'DOB'), 'Mobile', ('State', 'City', ('DistrictName'), 'PIN'))}), ('Course Details', {'fields': (('Course', 'Batch', 'Trainer'), ('StartDate', 'EndDate'), ('Fees', 'Active', 'Registered'))})

    def display_course(self, obj):
        try:
            url = f"/admin/students/students/{obj.id}/change/?_changelist_filters={obj.Name}"
            link = f'<a href="{url}">{obj.Course}</a>'
            return format_html(link)
        except NoReverseMatch:
            return None

    display_course.short_description = 'Course'

    # return format_html("<a href='{url}'>{url}</a>", url=obj.Course)

    def fees(self, obj):
        try:
            url = f"/admin/students/feedetails/?Name__id__exact={obj.Name}"
            link = f'<a href="{url}">Go</a>'
            return format_html(link)
        except NoReverseMatch:
            return None
    fees.short_description = 'Fees'


@admin.register(FeeDetails)
class FeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('first_pay', 'first_pay_amount', 'payment', 'second_pay', 'second_pay_amount', 'payment',
                    'third_pay', 'third_pay_amount', 'payment')
    list_filter = ('Name',)

    def payment(self, obj):
        url = reverse('admin:students_feesreceipt_add')  # Replace 'yourapp' with the actual name of your app
        link = f'<a href="{url}?student_id={obj.Name}">Pay</a>'
        return format_html(link)

    payment.short_description = 'Payment'


@admin.register(FeesReceipt)
class FeesReceiptAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'paid_amount', 'receipt_number', 'payment_mode', 'description',
                    'collected_to_account')
