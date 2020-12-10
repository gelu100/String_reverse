from django.shortcuts import render
from .models import Pytanie
from django.views.generic import CreateView
from pytania_python.models import Pytanie

def index(request):
    tasks = Pytanie.objects.all()

    task = request.GET.get('task')
    if task:
        Pytanie.objects.create(text=task)

    return render(request, 'pytania_python/index.html', {"pytanie": tasks})
