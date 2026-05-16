from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

@login_required
def workout_plans(request):

    workouts = [
        {
            "name": "Beginner Workout",
            "pdf": "/media/workouts/beginner_plan.pdf",
            "video": "/media/workouts/beginner_workout.mp4",
            "youtube": "https://www.youtube.com/watch?v=U0bhE67HuDY"
        },
        {
            "name": "Weight Loss Workout",
            "pdf": "/media/workouts/weight_loss_plan.pdf",
            "video": "/media/workouts/weight_loss.mp4",
            "youtube": "https://www.youtube.com/watch?v=ml6cT4AZdqI"
        },
        {
            "name": "Muscle Gain Workout",
            "pdf": "/media/workouts/muscle_gain_plan.pdf",
            "video": "/media/workouts/muscle_workout.mp4",
            "youtube": "https://www.youtube.com/watch?v=2tM1LFFxeKg"
        }
    ]

    return render(request, "workout_plans.html", {"workouts": workouts})

from .models import TrainerProfile

@login_required
def trainer_profile(request):

    trainer = TrainerProfile.objects.get(user=request.user)

    return render(request, "trainer_profile.html", {"trainer": trainer})

from .models import TrainerProfile

@login_required
def edit_trainer_profile(request):

    trainer = TrainerProfile.objects.get(user=request.user)
    user = request.user

    if request.method == "POST":

        # User fields
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.save()

        # TrainerProfile fields
        trainer.experience = request.POST.get('experience')

        if request.FILES.get('profile_photo'):
            trainer.profile_photo = request.FILES.get('profile_photo')

        trainer.save()

        return redirect('trainer_profile')

    return render(request, "edit_trainer_profile.html", {"trainer": trainer})



def trainer_profile_view(request):
    return render(request, 'trainer_profile.html', {'user': request.user})

def logout_trainer(request):
    logout(request)
    return redirect('login')


from django.shortcuts import redirect
from .models import Booking
from accounts.models import User

def book_trainer(request, trainer_id):

    trainer = User.objects.get(id=trainer_id)

    booking = Booking.objects.filter(member=request.user).first()

    if not booking:
        Booking.objects.create(
            member=request.user,
            trainer=trainer
        )
        messages.success(request, "You Booked Trainer Successfully 💪")

    return redirect('welcome')


def cancel_booking(request):

    booking = Booking.objects.filter(member=request.user).first()

    if booking:
        booking.delete()
        messages.success(request, "Your Booking Cancelled Successfully")

    return redirect('welcome')

def trainer_members(request):

    bookings = Booking.objects.filter(trainer=request.user)

    return render(request, 'trainer_members.html', {'bookings': bookings})

from accounts.models import User
from django.shortcuts import get_object_or_404

@login_required
def member_profile(request, member_id):

    member = get_object_or_404(User, id=member_id, role="member")

    return render(request, "member_profile.html", {
        "member": member
    })

