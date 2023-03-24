import pytest

from django.contrib.auth.models import User

from tasks.selectors import task_list
from tasks.services import TaskService


@pytest.mark.django_db
def test_task_create_success():
    user1 = User(username='pepe')
    user1.save()

    task = TaskService(user=user1).create(description='Mi primer tarea')

    assert task.user == user1
    assert task.is_done is False


@pytest.mark.django_db
def test_task_get_by_owner_only():
    user1 = User(username='pepe')
    user1.save()

    user2 = User(username='coco')
    user2.save()

    TaskService(user=user1).create(description='Mi primer tarea')

    assert task_list(user1).count() == 1
    assert task_list(user2).count() == 0


@pytest.mark.django_db
def test_task_mark_as_done():
    user1 = User(username='pepe')
    user1.save()

    task = TaskService(user=user1).create(description='Mi primer tarea')
    TaskService.update_is_done(task, True)

    assert task.is_done is True
