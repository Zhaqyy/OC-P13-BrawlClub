from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'player_lookup'

urlpatterns = [
    path('update_clubs/', views.update_all_clubs, name='update_clubs'),
    path('club_members/<str:club_tag>', views.update_club_members),
    path("api/player/<str:player_tag>", views.update_player_profile),
]

drf_patterns = [
    path("api/leaderboard/<str:entity>/<str:size>", views.LeaderBoardView.as_view()),
]

urlpatterns += format_suffix_patterns(drf_patterns)
