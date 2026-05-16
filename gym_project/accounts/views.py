from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from gym.models import Booking
from gym.models import TrainerProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()

# def login_view(request):

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         if not User.objects.filter(username=username).exists():
#             return render(request, 'login.html', {
#                 'error': 'Not a user. Please create an account.'
#             })

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('welcome')
#         else:
#             return render(request, 'login.html', {
#                 'error': 'Invalid username or password'
#             })

#     return render(request, 'login.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            return render(request, 'login.html', {
                'error': 'Not a user. Please create an account.'
            })


        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            if user.role == "trainer":
                return redirect("trainer_profile")

            elif user.role == "member":
                return redirect("welcome")

            elif user.role == "admin":
                return redirect("/admin/")

        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


def register_view(request):

    if request.method == 'POST':

        if User.objects.filter(username=request.POST['username']).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            weight=request.POST['weight'],
            joining_date=request.POST['joining_date'],
            role='member'
        )

        if 'profile_photo' in request.FILES:
            user.profile_photo = request.FILES['profile_photo']
            user.save()

        
        messages.success(request, "Account created successfully!")

        return redirect('login')

    return render(request, 'register.html')


# @login_required
# def welcome_view(request):

#     trainers = TrainerProfile.objects.select_related('user').all()

#     return render(request, 'welcome.html', {
#         'trainers': trainers,
#         'user': request.user
#     })



@login_required
def welcome_view(request):

    trainers = TrainerProfile.objects.select_related('user').all()

    booking = Booking.objects.filter(member=request.user).first()

    return render(request, 'welcome.html', {
        'trainers': trainers,
        'user': request.user,
        'booking': booking
    })


@login_required
def profile_view(request):
    return render(request, 'profile_view.html', {'user': request.user})


@login_required
def profile_update(request):

    user = request.user

    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.weight = request.POST['weight']

        if 'profile_photo' in request.FILES:
            user.profile_photo = request.FILES['profile_photo']

        user.save()
        return redirect('profile')

    return render(request, 'profile_update.html', {'user': user})



@login_required
def delete_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'profile_view.html', {'error': 'Please fill all fields'})

        user = authenticate(username=username, password=password)

        if user is not None and user == request.user:
            user.delete()
            messages.success(request, "Account deleted successfully!")
            return redirect('login')
        else:
            return render(request, 'profile_view.html', {'error': 'Invalid username or password'})

    return render(request, 'profile_view.html')

def logout_view(request):
    logout(request)
    return redirect('login')


# def forgot_password(request):

#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         new_password = request.POST.get('new_password')

#         try:
#             user = User.objects.get(username=username, email=email)
#             user.set_password(new_password)
#             user.save()

#             return render(request, "login.html", {
#                 "success": "Password changed successfully. Please login."
#             })

#         except User.DoesNotExist:
#             return render(request, "forgot_password.html", {
#                 "error": "Username or Email incorrect"
#             })

#     return render(request, "forgot_password.html")

def forgot_password(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(username=username, email=email)
            user.set_password(new_password)
            user.save()

            messages.success(request, "Password reset successful. Please login.")
            return redirect('login')

        except User.DoesNotExist:
            return render(request, "forgot_password.html", {
                "error": "Username or Email incorrect"
            })

    return render(request, "forgot_password.html")