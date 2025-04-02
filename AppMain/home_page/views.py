from django.shortcuts import render
from django.shortcuts import render


def index(request):
    context = {'name': 'Petr', 'lastname': 'Timokhin'}
    return render(request, 'home_page/index.html', context)
