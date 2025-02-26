from django.contrib import admin
from .models import Prevencion, Group, AcademicYear

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
# Register your models here.
admin.site.register(Prevencion)

admin.site.register(Group)
admin.site.register(AcademicYear)