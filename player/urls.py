from django.urls import path
from . import views

urlpatterns = [
    path('player/', views.player_views, name='player_views'),
]
