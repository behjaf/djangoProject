import random

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def generator(request):
    characters = list('abc')
    if request.GET.get('capital'):
        characters.extend(list('ABC'))

    if request.GET.get('number'):
        characters.extend(list('123'))

    if request.GET.get('complex'):
        characters.extend(list('!@#'))

    length = request.GET.get('length')

    newpassword = ''
    for x in range(0, int(length), 1):
        newpassword += random.choice(characters)

    return render(request, 'generator.html', {'newpassword': newpassword})
