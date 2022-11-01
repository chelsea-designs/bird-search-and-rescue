from django.urls import path
from . import views

urlpatterns = [
    path('', views.team, name='team'),
    path('add-team-member/', views.addTeamMember, name='add_team_member'),
    path('edit-team-member/<slug:slug>/', views.editTeamMember,
         name='edit_team_member'),
    path('delete-team-member/<str:pk>/',
         views.deleteTeamMember,
         name='delete_team_member'),
]
