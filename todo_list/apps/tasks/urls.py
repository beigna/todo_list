from django.urls import path

from .views import task_list, task_edit

urlpatterns = [
    path('', task_list),
    path('<int:task_id>/edit', task_edit, name='task_edit'),
    path('<int:task_id>/done', task_edit, name='task_mark_done'),
]
