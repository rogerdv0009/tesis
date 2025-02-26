# apps/apps.py
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prev'

    def ready(self):
        import your_app.signals  # Si tienes señales, asegúrate de importarlas aquí



class PrevConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prev'
