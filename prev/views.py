from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.urls import reverse_lazy
from .models import Prevencion, Reporte
from .forms import PrevencionForm
from django.shortcuts import render
from django.http import HttpResponse
from .utils import cargar_datos_desde_excel, GPTResponse  # Asegúrate de importar la función
from .models import AcademicYear, Group
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ReporteForm
import tempfile
from django.contrib import messages
from django.views.generic import View, CreateView, DeleteView, TemplateView



@login_required
def update_profile_photo(request):
    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a la página de perfil o donde desees
    else:
        form = ProfilePhotoForm(instance=request.user)
    
    return render(request, 'update_profile_photo.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def user_create(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
           
            return redirect('user_list')

        else:
            print(user_form.errors)
    else:
        user_form = UserCreationForm()
        
    return render(request, 'user_form.html', {'user_form': user_form})

@login_required
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')
    else:
        user_form = UserForm(instance=user)
    return render(request, 'user_form.html', {'user_form': user_form})

@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

@login_required
def academic_year_list(request):
    academic_years = AcademicYear.objects.all()
    return render(request, 'academic_year_list.html', {'academic_years': academic_years})

@login_required
def prevencion_list(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    prevenciones = Prevencion.objects.annotate(
        total=(
            F('consumo_social_alcohol') +
            F('consumo_riesgoso_alcohol') +
            F('consumo_ocasional_cigarro') +
            F('consumo_regular_cigarro') +
            F('otros_tipos_adicciones_numero') +
            F('consumo_psicofarmacos_receta') +
            F('consumo_psicofarmacos_automedicacion') +
            F('vinculo_grupos_sociales_numero') +
            F('problemas_personalidad') +
            F('problemas_psiquiatricos') +
            F('problemas_personales_familiares_sociales_economicos') +
            F('problemas_academicos') +
            F('problemas_disciplina') +
            F('problema_asistencia') +
            F('caso_nuevo')
        )
    ).filter(groups = group)
    return render(request, 'prevencion_list.html', {'prevenciones': prevenciones})

@login_required
def prevencion_create(request):
    if request.method == "POST":
        form = PrevencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prevencion_list')
    else:
        form = PrevencionForm()
    return render(request, 'prevencion_form.html', {'form': form})

@login_required
def prevencion_update(request, pk):
    prevencion = get_object_or_404(Prevencion, pk=pk)
    if request.method == "POST":
        form = PrevencionForm(request.POST, instance=prevencion)
        if form.is_valid():
            form.save()
            return redirect('prevencion_list')
    else:
        form = PrevencionForm(instance=prevencion)
    return render(request, 'prevencion_form.html', {'form': form})

@login_required
def prevencion_delete(request, pk):
    prevencion = get_object_or_404(Prevencion, pk=pk)
    if request.method == "POST":
        prevencion.delete()
        return redirect('prevencion_list')
    return render(request, 'prevencion_delete_confirm.html', {'prevencion': prevencion})

@login_required
def profile(request):
    return render(request, 'prev/profile.html')

@login_required
def consult_information(request):
    estudiantes = Prevencion.objects.all()
    return render(request, 'prev/consult_information.html',{'estudiantes': estudiantes})

@login_required
def cargar_informacion(request):
    if request.method == 'POST':
        archivo = request.FILES['archivo']
        academic_year_number = request.POST.get('academic_year')
        academic_year = get_object_or_404(AcademicYear, number=int(academic_year_number))
        
        # Crea un archivo temporal en la ubicación adecuada para el sistema operativo
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xls') as temp_file:
            ruta_archivo = temp_file.name
            for chunk in archivo.chunks():
                temp_file.write(chunk)

        cargar_datos_desde_excel(ruta_archivo, academic_year)

        return HttpResponse("<a href='http://127.0.0.1:8000/academic_year/'>Volver al listado</a><br><h2>Datos cargados exitosamente.</h2>")
    
    return render(request, 'prev/cargar_informacion.html')


@login_required
def gestionar_usuarios(request):
    # Logic for managing users
    return render(request, 'prev/gestionar_usuarios.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')


###Estadisticas
class AcademicYearStatiticsView(View):
    """ Class to generate the year statistics """
    def get(self, request, *args, **kwargs):
        academic_year = get_object_or_404(AcademicYear, pk=kwargs['year_id'])
        campo_valor = [
        'consumo_social_alcohol',
        'consumo_riesgoso_alcohol',
        'consumo_ocasional_cigarro',
        'consumo_regular_cigarro',
        'otros_tipos_adicciones_numero',
        'consumo_psicofarmacos_receta',
        'consumo_psicofarmacos_automedicacion',
        'vinculo_grupos_sociales_numero',
        'problemas_personalidad',
        'problemas_psiquiatricos',
        'problemas_personales_familiares_sociales_economicos',
        'problemas_academicos',
        'problemas_disciplina',
        'problema_asistencia',
        'caso_nuevo',
        ]
        total = 0
        estadisticas = {}
        grupos = Group.objects.filter(academic_year=academic_year)
        for grupo in grupos:
            estudiantes = Prevencion.objects.filter(groups=grupo)
            for campo in campo_valor:
                count = estudiantes.filter(**{campo: 1}).count()
                total += count
                nombre_campo = campo.replace('_', ' ').title()
                if nombre_campo not in estadisticas:
                    estadisticas[nombre_campo] = count
                else:
                    estadisticas[nombre_campo] += count
        return render(request, 'academic_year_estadistica.html', {'academic_year':academic_year, 'estadisticas': estadisticas, 'total': total})

class GroupStatiticsView(View):
    """ Class to generate the statistics """
    def get(self, request, *args, **kwargs):
        grupo = get_object_or_404(Group, pk=kwargs['group_id'])
        campo_valor = [
            'consumo_social_alcohol',
            'consumo_riesgoso_alcohol',
            'consumo_ocasional_cigarro',
            'consumo_regular_cigarro',
            'otros_tipos_adicciones_numero',
            'consumo_psicofarmacos_receta',
            'consumo_psicofarmacos_automedicacion',
            'vinculo_grupos_sociales_numero',
            'problemas_personalidad',
            'problemas_psiquiatricos',
            'problemas_personales_familiares_sociales_economicos',
            'problemas_academicos',
            'problemas_disciplina',
            'problema_asistencia',
            'caso_nuevo',
        ]
        estudiantes = Prevencion.objects.filter(groups=grupo)
        estadisticas = {}
        total = 0
        for campo in campo_valor:
            count = estudiantes.filter(**{campo: 1}).count()
            total += count
            nombre_legible = campo.replace('_', ' ').title()
            estadisticas[nombre_legible] = count
        return render(request, 'estadisticas.html', {'estadisticas': estadisticas, 'grupo': grupo,  'total': total})

class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('academic_year_list')
    template_name = 'prev/grupo_delete.html'

###CLASS TO GENERATE THE IA RESPONSE

class ConsultIA(View):
    """ Class to generate the IA response """
    manager_response = GPTResponse()
    
    def post(self, request, *args, **kwargs):
        estudiante_id = request.POST.get('estudiante')
        estudiante = get_object_or_404(Prevencion, pk=estudiante_id)
        message = estudiante.obtener_mensaje_atributos_positivos()
        response = self.manager_response.get_response(message)
        message_response = response.get('result')
        return render(request, 'homepage.html', {'message_response': message_response, 'estudiante': estudiante})

class ReportCreateView(CreateView):
    model = Reporte
    form_class = ReporteForm
    template_name = 'prev/general_reporte.html'
    success_url = reverse_lazy('homepage')
    
    def post(self, request, *args, **kwargs):
        user = request.user
        comentario = request.POST.get('comentario')
        reporte = Reporte(usuario=user, comentario=comentario)
        reporte.save()
        return redirect('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'El reporte ha sido creado exitosamente.')
        return super().form_valid(form)
    
class ReportListView(View):
    template_name = 'prev/reporte_listado.html'
    
    def get(self, request, *args, **kwargs):
        reports = Reporte.objects.all()
        academic_years = AcademicYear.objects.all()
        campo_valor = [
        'consumo_social_alcohol',
        'consumo_riesgoso_alcohol',
        'consumo_ocasional_cigarro',
        'consumo_regular_cigarro',
        'otros_tipos_adicciones_numero',
        'consumo_psicofarmacos_receta',
        'consumo_psicofarmacos_automedicacion',
        'vinculo_grupos_sociales_numero',
        'problemas_personalidad',
        'problemas_psiquiatricos',
        'problemas_personales_familiares_sociales_economicos',
        'problemas_academicos',
        'problemas_disciplina',
        'problema_asistencia',
        'caso_nuevo',
        ]
        total = 0
        estadisticas = {}
        annos = {}
        for academic_year in academic_years:
            grupos = Group.objects.filter(academic_year=academic_year)
            if academic_year.number not in annos:
                annos[academic_year.number] = {}
            for grupo in grupos:
                estudiantes = Prevencion.objects.filter(groups=grupo)
                for campo in campo_valor:
                    count = estudiantes.filter(**{campo: 1}).count()
                    total += count
                    nombre_campo = campo.replace('_', ' ').title()
                    if nombre_campo not in estadisticas:
                        estadisticas[nombre_campo] = count
                    else:
                        estadisticas[nombre_campo] += count
            annos[academic_year.number] = estadisticas
            annos[academic_year.number]['total'] = total
            total = 0
            estadisticas = {}
        return render(request, self.template_name, {'reports': reports, 'annos': annos})

class ReportDeleteView(DeleteView):
    model = Reporte
    success_url = reverse_lazy('listar_reporte')
    template_name = 'prev/reporte_delete.html'
    
class ReporteTemplateView(TemplateView):
    template_name = 'prev/general_reporte.html'