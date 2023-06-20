from django.contrib import admin
from django.urls import NoReverseMatch

from .models import *
from .models import Companies, State, District, Branch


# Register your models here.

admin.site.register(State)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['CourseName', 'CourseCode', 'Active', 'fees', 'Syllabus']

    def fees(self, obj):
        try:
            url = f"/admin/settings/coursefees/?q={obj.CourseName}"
            link = f'<a href="{url}">Go</a>'
            return format_html(link)
        except NoReverseMatch:
            return None
    fees.short_description = 'Fees'



@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = Batch.DisplayFields


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = District.DisplayFields


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = Branch.DisplayFields


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = Companies.DisplayFields


@admin.register(CourseFees)
class CourseFeesAdmin(admin.ModelAdmin):
    list_display = CourseFees.DisplayFields
    search_fields = CourseFees.SearchFields
    