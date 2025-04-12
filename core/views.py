from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import SportsEvent
from .models import Team
from .models import Athlete


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

@login_required
def teams_list(request):
    teams = Team.objects.all()
    return render(request, "teams_list.html", {"teams": teams})

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    athletes = team.athletes.all()
    events = team.events.all()
    return render(request, "team_detail.html", {
        "team": team,
        "athletes": athletes,
        "events": events
    })

@login_required
def athlete_detail(request, athlete_id):
    athlete = get_object_or_404(Athlete, id=athlete_id)
    return render(request, "athlete_detail.html", {
        "athlete": athlete,
        "team": athlete.team,
        "events": athlete.events.all()
    })

@login_required
def athletes_list(request):
    athletes = Athlete.objects.all()
    return render(request, "athletes_list.html", {"athletes": athletes})

@login_required
def home(request):
    return render(request, "home.html")
