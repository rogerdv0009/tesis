from django.urls import path
from .views import (prevencion_list,update_profile_photo, profile_view, prevencion_create,
                    update_profile_photo, prevencion_update, prevencion_delete, profile, 
                    consult_information, cargar_informacion, general_reporte, gestionar_usuarios, 
                    user_list, user_create, user_update, user_delete, homepage, academic_year_list,
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
    path('general_reporte/', general_reporte, name='rrr'),
    path('cargar-informacion/', cargar_informacion, name='cargar_informacion'),  # New URL
    path('general-reporte/', general_reporte, name='general_reporte'),  # New URL
    path('gestionar-usuarios/', gestionar_usuarios, name='gestionar_usuarios'),
    path('users/', user_list, name='user_list'),# New URL
    path('users/create/', user_create, name='user_create'),
    path('users/update/<int:pk>/', user_update, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),
    path('update-profile-photo/', update_profile_photo, name='update_profile_photo'), 
    path('update-profile-photo/', update_profile_photo, name='update_profile_photo'),
    path('profile/', profile_view, name='profile'),
    #path("consultar_ia/", ConsultIA.as_view(), name="consultar_ia")
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)