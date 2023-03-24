from django.urls import path

from .views import task_list, task_edit, task_new, task_delete, task_done, task_undone  # noqa

urlpatterns = [
    path('', task_list, name='task_list'),
    path('new', task_new, name='task_new'),
    path('<int:task_id>/edit', task_edit, name='task_edit'),
    path('<int:task_id>/done', task_done, name='task_done'),
    path('<int:task_id>/undone', task_undone, name='task_undone'),
    path('<int:task_id>/delete', task_delete, name='task_delete'),
]
