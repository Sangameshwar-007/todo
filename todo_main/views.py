"""
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> Hello This is Home Page</h1>')

"""
from django.shortcuts import render
from todos.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    # print(tasks)  # This will still show <QuerySet ...> in terminal
    context = {
        'tasks': tasks,
    }

    return render(request, 'home.html', context)
