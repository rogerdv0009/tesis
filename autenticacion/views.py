from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
        
            return redirect("homepage" )
        return render(request, "login.html")

    def post(self, request):
        if not request.user.is_authenticated:
            username = request.POST.get("username")
            password = request.POST.get("password")

            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    auth_login(request, user)
                    messages.success(request, "Logeado con éxito")
                  
                    return redirect("homepage")

                else:
                    print('Credenciales incorrectas')
            except User.DoesNotExist:
                messages.error(request, "Credenciales incorrectas")
            return redirect("login")

   
        return redirect("prevencion_list" )


class Logout(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        messages.success(request, "Sesión cerrada con éxito")
        return redirect("login")
