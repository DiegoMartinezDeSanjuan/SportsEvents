from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SportsEvent, Team, Athlete

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class SportsEventForm(forms.ModelForm):
    teams = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    athletes = forms.ModelMultipleChoiceField(
        queryset=Athlete.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = SportsEvent
        fields = ["name", "date", "location", "sport_type", "teams", "athletes"]


class TeamForm(forms.ModelForm):
    athletes = forms.ModelMultipleChoiceField(
        queryset=Athlete.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Team
        fields = ["name", "country", "sport_type", "athletes"]

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ["name", "age", "nationality", "sport", "team"]