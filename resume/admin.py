from django.contrib import admin
from .models import Emp_resume
# Register your models here.
@admin.register(Emp_resume)


class resumeadmin(admin.ModelAdmin):
    list_display = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_img','my_file']