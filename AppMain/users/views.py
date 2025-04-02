from django.shortcuts import render, redirect, reverse


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')


    # return render(request, 'my_template.html', context)
#     return redirect(reverse('register'))
#     return redirect('register', permanent=True)

#     return HttpResponseRedirect('/')
#     HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")
