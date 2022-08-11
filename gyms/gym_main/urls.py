from django.urls import path

from gym_main.views import index

urlpatterns = [
    path('', index, name='index'),
]