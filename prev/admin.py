from django.contrib import admin
from .models import Prevencion, Group, AcademicYear


# Register your models here.
admin.site.register(Prevencion)

admin.site.register(Group)
admin.site.register(AcademicYear)