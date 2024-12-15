from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm  
from django.contrib.auth.forms import AuthenticationForm

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # If the form is valid, authenticate the user and log them in
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()

    # Render the login template with the form (and any messages if they exist)
    return render(request, 'login.html', {'form': form})

# # Signup view
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            # If form is invalid, it will show validation error messages
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Change password view
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

# Dashboard view
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

# Profile view
@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


