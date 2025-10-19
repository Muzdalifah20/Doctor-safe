from django.shortcuts import render, redirect
from django.contrib.auth import logout, login as login_auth
from .forms import CustomRegisterationForm
from django.contrib.auth.views import LogoutView

# Create your views here.
def register(request):
    form = CustomRegisterationForm()
    if request.method == "POST":
        form = CustomRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_auth(request, user)
            return redirect('home')
    else:
        form = CustomRegisterationForm()
    return render(request, 'registeration/register.html', {'form': form})

def home(request):
    return render(request, "home.html")
    


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")