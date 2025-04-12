from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login automático tras registrarse
            return redirect('home')  # puedes cambiar esta redirección
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
