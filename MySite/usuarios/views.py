from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.shortcuts import redirect

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # role no se pide, se asigna solo (default="user")
            user.save()
            return redirect("login")  # después de registrarse va al login
    else:
        form = CustomUserCreationForm()
    return render(request, "usuarios/register.html", {"form": form})

@login_required
def protected_view(request):
    return render(request, "usuarios/protected.html")
