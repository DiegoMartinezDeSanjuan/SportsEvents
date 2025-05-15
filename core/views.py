from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, SportsEventForm, TeamForm, AthleteForm
from .models import SportsEvent, Team, Athlete


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login automático tras registrarse
            return redirect('home')
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


# Vistas para crear entidades (nuevas)

class SportsEventCreateView(LoginRequiredMixin, CreateView):
    model = SportsEvent
    form_class = SportsEventForm
    template_name = "create_event.html"
    success_url = reverse_lazy("events_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        response = super().form_valid(form)
        # Asignar equipos y atletas al evento
        form.instance.teams.set(form.cleaned_data["teams"])
        form.instance.athletes.set(form.cleaned_data["athletes"])
        return response


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = "create_team.html"
    success_url = reverse_lazy("teams_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        response = super().form_valid(form)
        # Asignar atletas al equipo
        form.instance.athletes.set(form.cleaned_data["athletes"])
        return response


class AthleteCreateView(LoginRequiredMixin, CreateView):
    model = Athlete
    form_class = AthleteForm
    template_name = "create_athlete.html"
    success_url = reverse_lazy("athletes_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

# Vistas para modificar entidades


class SportsEventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SportsEvent
    form_class = SportsEventForm
    template_name = "update_event.html"
    success_url = reverse_lazy("events_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Actualizar las relaciones ManyToMany
        self.object.teams.set(form.cleaned_data["teams"])
        self.object.athletes.set(form.cleaned_data["athletes"])
        return response

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.creator


class TeamUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = "update_team.html"
    success_url = reverse_lazy("teams_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Actualizar las relaciones ManyToMany
        self.object.athletes.set(form.cleaned_data["athletes"])
        return response

    def test_func(self):
        team = self.get_object()
        return self.request.user == team.creator



class AthleteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Athlete
    form_class = AthleteForm
    template_name = "update_athlete.html"
    success_url = reverse_lazy("athletes_list")

    def test_func(self):
        # Solo el creador puede modificar el atleta
        athlete = self.get_object()
        return self.request.user == athlete.creator

# Vistas para eliminar entidades

class SportsEventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SportsEvent
    template_name = "delete_event.html"
    success_url = reverse_lazy("events_list")

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.creator


class TeamDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Team
    template_name = "delete_team.html"
    success_url = reverse_lazy("teams_list")

    def test_func(self):
        team = self.get_object()
        return self.request.user == team.creator


class AthleteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Athlete
    template_name = "delete_athlete.html"
    success_url = reverse_lazy("athletes_list")

    def test_func(self):
        athlete = self.get_object()
        return self.request.user == athlete.creator
