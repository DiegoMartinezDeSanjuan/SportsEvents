"""
URL configuration for SportsEvents project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import register, SportsEventUpdateView, TeamUpdateView, AthleteUpdateView, \
    SportsEventDeleteView, TeamDeleteView, AthleteDeleteView
from django.contrib.auth import views as auth_views
from core.views import events_list
from core.views import event_detail
from core.views import teams_list
from core.views import team_detail
from core.views import athlete_detail
from core.views import athletes_list
from core.views import home
from core.views import SportsEventCreateView, TeamCreateView, AthleteCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('events/', events_list, name='events_list'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('teams/', teams_list, name='teams_list'),
    path('teams/<int:team_id>/', team_detail, name='team_detail'),
    path('athletes/<int:athlete_id>/', athlete_detail, name='athlete_detail'),
    path('athletes/', athletes_list, name='athletes_list'),
    path('', home, name='home'),
    path('events/create/', SportsEventCreateView.as_view(), name='create_event'),
    path('teams/create/', TeamCreateView.as_view(), name='create_team'),
    path('athletes/create/', AthleteCreateView.as_view(), name='create_athlete'),
    path('events/<int:pk>/edit/', SportsEventUpdateView.as_view(), name='edit_event'),
    path('teams/<int:pk>/edit/', TeamUpdateView.as_view(), name='edit_team'),
    path('athletes/<int:pk>/edit/', AthleteUpdateView.as_view(), name='edit_athlete'),

    # Eliminación
    path('events/<int:pk>/delete/', SportsEventDeleteView.as_view(), name='delete_event'),
    path('teams/<int:pk>/delete/', TeamDeleteView.as_view(), name='delete_team'),
    path('athletes/<int:pk>/delete/', AthleteDeleteView.as_view(), name='delete_athlete'),


]

