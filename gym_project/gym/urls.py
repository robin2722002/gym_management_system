from django.urls import path
from . import views
urlpatterns = [
    path('workout-plans/', views.workout_plans, name='workout_plans'),
    path('trainer_profile/',views.trainer_profile,name='trainer_profile'),
    path('edit-trainer-profile/', views.edit_trainer_profile, name='edit_trainer_profile'),
    path('logout-trainer/', views.logout_trainer, name='logout_trainer'),
    path('trainer-profile-view/',views.trainer_profile_view,name='trainer_profile_view'),
    path('book_trainer/<int:trainer_id>/', views.book_trainer, name='book_trainer'),
    path('cancel_booking/', views.cancel_booking, name='cancel_booking'),
    path('trainer-members/',views.trainer_members,name='trainer_members'),
    path('member-profile/<int:member_id>/', views.member_profile, name='member_profile'),
]