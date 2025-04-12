from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import SportsEvent

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

@login_required
def events_list(request):
    events = SportsEvent.objects.all()
    return render(request, "events_list.html", {"events": events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(SportsEvent, id=event_id)
    teams = event.teams.all()
    athletes = event.athletes.all()
    return render(request, "event_detail.html", {
        "event": event,
        "teams": teams,
        "athletes": athletes
    })