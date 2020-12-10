from django.db import models


class Pytanie(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)


def __str__(self):
    return f"{self.text}"
