from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages

class LoginViewTests(TestCase):
    def setUp(self):
        # Crear un usuario para las pruebas
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_get_authenticated_user(self):
        # Simular que el usuario ya está autenticado
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse("login"))
        
        # Verificar que redirige a 'prevencion_list'
        self.assertRedirects(response, reverse("prevencion_list"))

    def test_login_get_unauthenticated_user(self):
        # Simular que el usuario no está autenticado
        response = self.client.get(reverse("login"))
        
        # Verificar que se renderiza la plantilla 'login.html'
        self.assertTemplateUsed(response, "login.html")

    def test_login_post_success(self):
        # Intentar iniciar sesión con credenciales correctas
        response = self.client.post(reverse("login"), {
            "username": self.username,
            "password": self.password,
        })

        # Verificar que redirige a 'prevencion_list'
        self.assertRedirects(response, reverse("prevencion_list"))
        
        # Verificar que el usuario está autenticado
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_post_incorrect_password(self):
        # Intentar iniciar sesión con una contraseña incorrecta
        response = self.client.post(reverse("login"), {
            "username": self.username,
            "password": "wrongpassword",
        })

        # Verificar que redirige a 'login'
        self.assertRedirects(response, reverse("login"))
        
        # Verificar que se muestra un mensaje de error
        messages_list = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].message, "Credenciales incorrectas")

    def test_login_post_nonexistent_user(self):
        # Intentar iniciar sesión con un usuario que no existe
        response = self.client.post(reverse("login"), {
            "username": "nonexistentuser",
            "password": "any_password",
        })

        # Verificar que redirige a 'login'
        self.assertRedirects(response, reverse("login"))
        
        # Verificar que se muestra un mensaje de error
        messages_list = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)
        self.assertEqual(messages_list[0].message, "Credenciales incorrectas")
        # python manage.py test autenticacion
