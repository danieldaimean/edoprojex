from django.db import models

class Zprom(models.Model):
    question = models.TextField()  # Campo para armazenar a pergunta
    response = models.TextField()  # Campo para a resposta
    created_at = models.DateTimeField(auto_now_add=True)  # Campo para armazenar a data de criação

    def __str__(self):
        return self.question
# Create your models here.
