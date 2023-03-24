from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .selectors import task_get, task_list_done, task_list_undone
from .services import TaskService


@login_required
def task_list(request):
    template = 'tasks/list.html'

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        template = 'tasks/list_partial.html'

    return render(
        request,
        template,
        {
            'tasks_todo': task_list_undone(user=request.user),
            'tasks_done': task_list_done(user=request.user),
        }
    )


@login_required
def task_new(request):
    if request.method == 'POST':
        TaskService(request.user).create(
            description=request.POST['description']
        )

    return redirect(reverse('task_list'))


@login_required
def task_edit(request, task_id):
    task = task_get(user=request.user, task_id=task_id)

    if request.method == 'GET':
        return render(request, 'tasks/edit.html', {'task': task})

    if request.method == 'POST':
        task = TaskService.update_description(
            task=task,
            description=request.POST['description']
        )
        return render(request, 'tasks/task_inline.html', {'task': task})


@login_required
def task_delete(request, task_id):
    task = task_get(user=request.user, task_id=task_id)
    TaskService.delete(task)

    return redirect(reverse('task_list'))


@login_required
def task_done(request, task_id):
    task = task_get(user=request.user, task_id=task_id)
    TaskService.update_is_done(task, True)

    return redirect(reverse('task_list'))


@login_required
def task_undone(request, task_id):
    task = task_get(user=request.user, task_id=task_id)
    TaskService.update_is_done(task, False)

    return redirect(reverse('task_list'))
