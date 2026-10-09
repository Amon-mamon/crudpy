from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "member_id", "first_name" , "last_name")
    
admin.site.register(Student, StudentAdmin)