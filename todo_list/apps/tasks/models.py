from django.contrib.auth.models import User
from django.db import models


class DateLogModel(models.Model):  # Por comodidad dejo este modelo acá
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class Task(DateLogModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
