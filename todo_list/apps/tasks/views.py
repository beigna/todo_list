from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Task


def task_list(request):
    template = 'tasks/list.html'

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        template = 'tasks/list_partial.html'

    return render(
        request,
        template,
        {
            'tasks_todo': Task.objects.filter(is_done=False),
            'tasks_done': Task.objects.filter(is_done=True),
        }
    )


def task_new(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.description = request.POST['description']
        task.save()

    return redirect(reverse('task_list'))


def task_edit(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'GET':
        return render(request, 'tasks/edit.html', {'task': task})

    if request.method == 'POST':
        task.description = request.POST['description']
        task.save()

        return render(request, 'tasks/task_inline.html', {'task': task})


def task_delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()

    return redirect(reverse('task_list'))


def task_done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = True
    task.save()

    return redirect(reverse('task_list'))


def task_undone(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = False
    task.save()

    return redirect(reverse('task_list'))
