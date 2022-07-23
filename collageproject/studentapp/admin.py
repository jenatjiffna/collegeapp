from django.contrib import admin
from .models import Student1, Center, Subcenter, Course1, Total_fees

# Register your models here.

admin.site.register(Student1)
admin.site.register(Center)
admin.site.register(Subcenter)
admin.site.register(Course1)
admin.site.register(Total_fees)