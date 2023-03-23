from django.shortcuts import render

from .models import Task


def task_list(request):

    return render(
        request,
        'tasks/list.html',
        {
            'tasks_todo': Task.objects.filter(is_done=False),
            'tasks_done': Task.objects.filter(is_done=True),
        }
    )


def task_edit(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'GET':
        return render(request, 'tasks/edit.html', {'task': task})

    if request.method == 'POST':
        task.description = request.POST['description']
        task.save()

        return render(request, 'tasks/task_inline.html', {'task': task})
