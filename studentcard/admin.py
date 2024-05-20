from django.contrib import admin

# Register your models here.
#For StudentRegistrations
from .models import StudentRegistration

admin.site.register(StudentRegistration)

# for Student cards
from .models import StudentCard
admin.site.register(StudentCard)
