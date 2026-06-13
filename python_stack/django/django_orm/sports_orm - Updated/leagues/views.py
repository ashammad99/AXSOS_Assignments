from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

from django.shortcuts import render
from .models import League, Team, Player

def index(request):

    context = {
        # 🏀 Leagues
        "baseball_leagues": League.objects.filter(sport="Baseball"),

        "women_leagues": League.objects.filter(name__icontains="Women"),

        "hockey_leagues": League.objects.filter(sport="Hockey"),

        "non_football_leagues": League.objects.exclude(sport="Football"),

        "conferences": League.objects.filter(name__icontains="Conference"),

        "atlantic_leagues": League.objects.filter(name__icontains="Atlantic"),

        # 🏟️ Teams
        "dallas_teams": Team.objects.filter(location__icontains="Dallas"),

        "raptors_teams": Team.objects.filter(team_name="Raptors"),

        "city_teams": Team.objects.filter(location__icontains="City"),

        "t_teams": Team.objects.filter(team_name__startswith="T"),

        "teams_by_location": Team.objects.all().order_by("location"),

        "teams_by_name_desc": Team.objects.all().order_by("-team_name"),


        # 👤 Players
        "cooper_players": Player.objects.filter(last_name="Cooper"),

        "joshua_players": Player.objects.filter(first_name="Joshua"),

        "cooper_not_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),

        "alexander_or_wyatt": Player.objects.filter(
            first_name__in=["Alexander", "Wyatt"]
        ),
    }

    return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")