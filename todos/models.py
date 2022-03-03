from django.db import models
from django.utils import timezone


class Task(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    created_at = models.DateTimeField(verbose_name='Created At',
                                      default=timezone.now)
    done = models.BooleanField(default=False, verbose_name='Is the task done?')

    def __str__(self):
        return self.name
