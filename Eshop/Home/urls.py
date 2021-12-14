from django.urls import path
from . import views
from django.contrib.auth import views as v_iews

app_name = 'Home'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.Contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', v_iews.LoginView.as_view(), name='login'),
    path('password_change/', v_iews.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', v_iews.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', v_iews.PasswordResetView.as_view(), name='password_reset'),
]
