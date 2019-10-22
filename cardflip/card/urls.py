from django.urls import path
from card import views


urlpatterns = [
    path('',views.signup,name='index'),
    path('game',views.game,name='game')
]