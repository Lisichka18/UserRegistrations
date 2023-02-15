from django.shortcuts import render, redirect
from .forms import UserForm


def index(request):
    return render(request, 'main/main.html')


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def registration(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration.html', context)


def person(request):
    return render(request, 'main/person.html')