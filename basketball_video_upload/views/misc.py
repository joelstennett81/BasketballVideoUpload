from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from basketball_video_upload.forms import AdminProfileForm, PlayerProfileForm, UserTypeForm


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('basketball_video_upload:login')


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('basketball_video_upload:choose_role')
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def choose_role(request):
    role_form = UserTypeForm(request.POST or None)
    profile_form = None

    if role_form.is_valid():
        user_type = role_form.cleaned_data.get('user_type')
        request.session['user_type'] = user_type

        # Create the appropriate profile form based on the user type
        if user_type == 'administrator':
            profile_form = AdminProfileForm()
        elif user_type == 'player':
            profile_form = PlayerProfileForm()

        return redirect('basketball_video_upload:upload_profile')

    return render(request, 'registration/choose_role.html', {'role_form': role_form, 'profile_form': profile_form})


def upload_profile(request):
    profile_form = AdminProfileForm(request.POST or None) if request.session.get(
        'user_type') == 'administrator' else PlayerProfileForm(request.POST or None)

    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.user = request.user
        if request.session.get('user_type') == 'administrator':
            profile.is_administrator = True
            profile.is_player = False
        else:
            profile.is_administrator = False
            profile.is_player = True
        profile.save()
        return redirect('basketball_video_upload:home')

    return render(request, 'registration/upload_profile.html', {'profile_form': profile_form})
