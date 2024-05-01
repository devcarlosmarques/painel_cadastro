from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    CATEGORIA_CHOICES = [
        ("SMARTPHONE", "SMARTPHONE"),
        ("VIDEOGAME", "VIDEOGAME"),
    ]
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome