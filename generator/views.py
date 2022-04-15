from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    random_list = list('qwertyuioplkjhgfdsazxcvbnm')
    lenght = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        random_list.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        random_list.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        random_list.extend(list('1234567890'))
    password = ''
    for ex in range(lenght):
        password += random.choice(random_list)
    context = {
        'password': password
    }
    return render(request, 'generator/password.html', context=context)


def about_us(request):
    return render(request, 'generator/about_us.html')


def huston(request):
    return render(request, 'generator/homework.html')
