from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

from .models import Person


def log(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email, password)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    user = User.objects.filter(email=email).first()
    if user.check_password(password):
        login(request, user)
        return redirect(reverse('index'))
    return HttpResponse('<h1>Ошибка авторизации</h1>'
                        '<a href="../../index/" %}">На главную!</a>')
                        # '<a href="{% url 'index' %}">На главную!</a>')


# user.is_authenticated
# user.is_anonymous


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(username, email, password)
    if User.objects.filter(username=username).exists():
        return redirect(reverse('log'))
    user = User.objects.create_user(username=username,
                                    email=email,
                                    password=password)
    login(request, user)

    return render(request, 'home_page/index.html')


def logout_user(request):
    logout(request)
    return redirect(reverse('log'))



    # person = Person(username=username, email=email, password=password)
    # person.save()
    # return render(request, 'users/login.html')

    # return render(request, 'my_template.html', context)
#     return redirect(reverse('register'))
#     return redirect('register', permanent=True)

#     return HttpResponseRedirect('/')
#     HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")
