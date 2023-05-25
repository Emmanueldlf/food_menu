from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account was successfully created!')
            return redirect('food:index')
    else:
        user_form = UserCreationForm()
    return render(request,'users/register.html', {'form':user_form})
