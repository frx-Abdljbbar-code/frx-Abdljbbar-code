from django.urls import path
from . import views

app_name = 'prof'

urlpatterns = [
    path('<slug>/', views.profile, name='profile'),
    path('<slug>/edit', views.edit_profile, name='edit_profile'),
]
