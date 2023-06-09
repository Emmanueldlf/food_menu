from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, you successfully logged in')
            return redirect('login')
    else:
        user_form = RegisterForm()
    return render(request,'users/register.html', {'form':user_form})

@login_required
def profile(request):
    return render(request,'users/profile.html')
