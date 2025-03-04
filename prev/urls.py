from django.urls import path
from .views import (prevencion_list,update_profile_photo, profile_view, prevencion_create,
                    update_profile_photo, prevencion_update, prevencion_delete, profile, 
                    consult_information, cargar_informacion, gestionar_usuarios, 
                    user_list, user_create, user_update, user_delete, homepage, academic_year_list,
                    GroupStatiticsView, AcademicYearStatiticsView, ConsultIA, ReportCreateView,
                    ReportListView, ReportDeleteView, GroupDeleteView, ReporteTemplateView
                )
from django.conf import settings
from django.conf.urls.static import static
# urls.py



urlpatterns = [
    path("", homepage, name="homepage"),
    path("academic_year/", academic_year_list, name="academic_year_list"),
    path('prevencion/<int:group_id>', prevencion_list, name='prevencion_list'),
    path('create/', prevencion_create, name='prevencion_create'),
    path('update/<int:pk>/', prevencion_update, name='prevencion_update'),
    path('delete/<int:pk>/', prevencion_delete, name='prevencion_delete'),
    path('profile/', profile, name='profile'),
    path('consult-information/', consult_information, name='consult_information'),
    path('cargar-informacion/', cargar_informacion, name='cargar_informacion'),  # New URL
    path('gestionar-usuarios/', gestionar_usuarios, name='gestionar_usuarios'),
    path('users/', user_list, name='user_list'),# New URL
    path('users/create/', user_create, name='user_create'),
    path('users/update/<int:pk>/', user_update, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),
    path('update-profile-photo/', update_profile_photo, name='update_profile_photo'), 
    path('update-profile-photo/', update_profile_photo, name='update_profile_photo'),
    path('profile/', profile_view, name='profile'),
    path("estadistica_grupo/<int:group_id>", GroupStatiticsView.as_view(), name="estadistica_grupo"),
    path("estadistica_year/<int:year_id>", AcademicYearStatiticsView.as_view(), name="estadistica_year"),
    path("consultar_ia/", ConsultIA.as_view(), name="consultar_ia"),
    path("reporte/template", ReporteTemplateView.as_view(), name="template_reporte"),
    path("reporte/crear", ReportCreateView.as_view(), name="crear_reporte"),
    path("reporte/listado", ReportListView.as_view(), name="listar_reporte"),
    path("reporte/eliminar/<int:pk>", ReportDeleteView.as_view(), name="eliminar_reporte"),
    path("grupo/eliminar/<int:pk>", GroupDeleteView.as_view(), name="eliminar_grupo")
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)