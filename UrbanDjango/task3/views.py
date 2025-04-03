from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.views import View


# Create your views here.


def roots(request):
    title = "Магазин мягких игрушек"
    text = "Главная страница"
    context = {
        "title": title,
        "text": text
    }

    return render(request, 'third_task/first_page.html', context=context)


def second_page(request):
    title = "Магазин мягких игрушек"
    text = "Вторая страница"
    context = {
        "title": title,
        "text": text
    }
    return render(request, 'third_task/second_page.html', context=context)

def third_page(request):
    title = "Ваша корзина"
    text = "Извините, ваша корзина пуста"
    context = {
        "title": title,
        "text": text
    }
    return render(request, 'third_task/third_page.html', context=context)


