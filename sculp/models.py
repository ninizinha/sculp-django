from django.db import models

class Tatuagem(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.CharField(max_length=50)
    link = models.URLField()
    imagem = models.URLField()

    def __str__(self):
        return self.nome