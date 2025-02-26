from django.db import models
from django.contrib.auth.models import User,AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
# prev/models.py


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email_verified = models.BooleanField(default=False)

class CustomUser(AbstractUser):
       profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

       groups = models.ManyToManyField(
           Group,
           related_name='customuser_set',  # Cambia el nombre aquí para evitar conflictos
           blank=True,
           help_text='The groups this user belongs to.',
           verbose_name='groups'
       )

       user_permissions = models.ManyToManyField(
           Permission,
           related_name='customuser_set',  # Cambia el nombre aquí para evitar conflictos
           blank=True,
           help_text='Specific permissions for this user.',
           verbose_name='user permissions'
       )

class reporte(models.Model):
    nombre_de_usario =  models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True, max_length=255)


#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    phone_number = models.CharField(max_length=15, blank=True)
#    address = models.CharField(max_length=255, blank=True)
#
#    def __str__(self):
#        return self.user.username

# Create your models here.
class Prevencion(models.Model):
    numero_de_orden = models.BigAutoField(primary_key=True)
    nombre_y_apellidos = models.CharField(null=True, blank=True, max_length=255)
    grupo = models.CharField(null=True, blank=True, max_length=255)
    sexo = models.CharField(null=True, blank=True, max_length=255)
    nacionalidad = models.CharField(null=True, blank=True, max_length=255)
    consumo_social_alcohol = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    consumo_riesgoso_alcohol = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    consumo_ocasional_cigarro = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    consumo_regular_cigarro = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    otros_tipos_adicciones_numero = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    otros_tipos_adicciones_tipo = models.CharField(null=True, blank=True, max_length=255)
    consumo_psicofarmacos_receta = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    consumo_psicofarmacos_automedicacion = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    vinculo_grupos_sociales_numero = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    vinculo_grupos_sociales_tipo = models.CharField(null=True, blank=True, max_length=255)
    problemas_personalidad = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    problemas_psiquiatricos = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    problemas_personales_familiares_sociales_economicos = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    problemas_academicos = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    problemas_disciplina = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    problema_asistencia = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    caso_nuevo = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')], null=True, blank=True)
    
    def __str__(self):
        return self.nombre_y_apellidos
    
    def obtener_mensaje_atributos_positivos(self):
        partes_mensaje = []
        
        nombres_campos = {
            'consumo_social_alcohol': 'Consumo social de alcohol',
            'consumo_riesgoso_alcohol': 'Consumo riesgoso de alcohol',
            'consumo_ocasional_cigarro': 'Consumo ocasional de cigarro',
            'consumo_regular_cigarro': 'Consumo regular de cigarro',
            'otros_tipos_adicciones_numero': 'Otros tipos de adicciones',
            'consumo_psicofarmacos_receta': 'Consumo de psicofármacos con receta',
            'consumo_psicofarmacos_automedicacion': 'Consumo de psicofármacos por automedicación',
            'vinculo_grupos_sociales_numero': 'Vínculo con grupos sociales',
            'problemas_personalidad': 'Problemas de personalidad',
            'problemas_psiquiatricos': 'Problemas psiquiátricos',
            'problemas_personales_familiares_sociales_economicos': 'Problemas personales, familiares, sociales o económicos',
            'problemas_academicos': 'Problemas académicos',
            'problemas_disciplina': 'Problemas de disciplina',
            'problema_asistencia': 'Problemas de asistencia',
            'caso_nuevo': 'Caso nuevo'
        }
        
        for campo, nombre_mostrar in nombres_campos.items():
            if getattr(self, campo) == 1:
                partes_mensaje.append(nombre_mostrar)
        
        if partes_mensaje:
            return "El estudiante presenta: " + ", ".join(partes_mensaje)
        return "No se encontraron factores de riesgo"
    
    class Meta:
        db_table = 'prevencion'

class AcademicYear(models.Model):
    """ Model definition for AcademicYear. """
    number = models.PositiveSmallIntegerField(
        verbose_name=_("Number"),
        help_text=_("Enter the academic year number."),
        unique=True,
    )

    class Meta:
        verbose_name = _("Academic Year")
        verbose_name_plural = _("Academic Years")

    def __str__(self):
        return f"{self.number}"

class Group(models.Model):
    """ Model definition for Group. """
    number = models.CharField(
        verbose_name=_("Group Number"),
        max_length=255,
        help_text=_("Enter the group number."),
        unique=True,
        blank=True,
        null=True,
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        verbose_name=_("Academic Year"),
        on_delete=models.CASCADE,
        help_text=_("Select the academic year."),
        related_name="groups",
    )
    prevenciones = models.ManyToManyField(
        Prevencion,
        verbose_name=_("Prevenciones"),
        help_text=_("Select the prevenciones."),
        related_name="groups",
        blank=True,
    )

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    def __str__(self):
        return f"Group {self.number} - Academic Year {self.academic_year}"