from .models import Task


def task_list(user):
    return Task.objects.filter(user=user)


def task_list_done(user):
    qs = task_list(user)
    return qs.filter(is_done=True)


def task_list_undone(user):
    qs = task_list(user)
    return qs.filter(is_done=False)


def task_get(user, task_id):
    qs = task_list(user)
    return qs.get(pk=task_id)
