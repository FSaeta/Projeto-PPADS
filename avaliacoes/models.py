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
    likes_cont = models.IntegerField("Número Likes", default=0)

    tipo = models.CharField("Tipo", max_length=200)

    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
    
    def curtir(self, user_id):
        like = LikeAvaliacao(user_id=user_id, avaliacao=self)
        self.likes_cont += 1
        like.save()
        self.save()

    def descurtir(self, user_id):
        like = LikeAvaliacao.objects.get(user_id=user_id, avaliacao=self)
        self.likes_cont -= 1
        like.delete()
        self.save()
    
    def get_liked_users(self):
        users = [like.user_id for like in self.likeavaliacao_set.all()]
        return users

class Comentario(models.Model):
    data_criacao = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField("Comentario", max_length="1024")
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, verbose_name="avaliacao")
    
    def curtir(self, user_id):
        like = LikeComentario(user_id=user_id, comentario=self)
        like.save()

    def descurtir(self, user_id):
        like = LikeComentario.objects.get(user_id=user_id)
        like.delete()
    
    def get_liked_users(self):
        users = [like.user_id for like in self.likecomentario_set.all()]
        return users

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
    
    def __str__(self):
        return f"{self.pk}- {self.comentario}"


class LikeAvaliacao(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", blank=True)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = ('user_id', 'avaliacao')

class LikeComentario(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="user_id", blank=True)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
