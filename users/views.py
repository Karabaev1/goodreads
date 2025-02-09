from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):

    @staticmethod
    def get(request):
        return render(request, 'users/register.html')

    @staticmethod
    def post(request):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()

        return redirect("users:login")


class LoginView(View):

    @staticmethod
    def get(request):
        return render(request, 'users/login.html')
