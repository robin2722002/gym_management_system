from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('logout/', views.logout_view, name='logout'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
]