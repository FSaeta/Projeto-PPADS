from django.db import models


from usuarios.models import Usuario
from itens.models import Filme, Livro, Serie


class Avaliacao(models.Model):
    CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )

    create_date = models.DateTimeField("Data de Criação", auto_now=True, blank=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", blank=True)
    valor = models.IntegerField("Avaliação", choices=CHOICES)
    avaliacao = models.CharField("Comentário", max_length=200, null=True)

    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        abstract = True
    
    def get_class(self):
        return self.__class__

class Comentario(models.Model):
