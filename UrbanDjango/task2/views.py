from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.views import View

# Create your views here.


def index(request):
    return render(request,'second_task/func_template.html')


class IndexView(TemplateView):
    template_name = "second_task/class_template.html"
