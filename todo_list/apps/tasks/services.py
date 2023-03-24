import logging

from .models import Task


logger = logging.getLogger('tasks')


class TaskService:
    def __init__(self, user):
        self.user = user

    def create(self, description):
        task = Task()
        task.user = self.user
        task.description = description
        task.save()

        logger.info('The task %s was created by %s', task.id, task.user)
        return task

    @staticmethod
    def update_description(task, description):
        task.description = description
        task.save()

        logger.info('The task %s was updated by %s', task.id, task.user)
        return task

    @staticmethod
    def update_is_done(task, is_done):
        task.is_done = is_done
        task.save()

        logger.info('The task %s was marked as %s by %s',
                    task.id,
                    'done' if is_done else 'undone',
                    task.user)
        return task

    @staticmethod
    def delete(task):
        task.delete()
        logger.info('The task %s was deleted by %s', task.id, task.user)
