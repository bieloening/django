from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Tarefas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.CharField(max_length=10)
    status = models.BooleanField()

    def __str__(self):
        return self.titulo

