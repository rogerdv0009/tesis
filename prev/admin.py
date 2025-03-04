from django.contrib import admin
from .models import Prevencion, Group, AcademicYear, Reporte


# Register your models here.
admin.site.register(Prevencion)

admin.site.register(Group)
admin.site.register(AcademicYear)
admin.site.register(Reporte)