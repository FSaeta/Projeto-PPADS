from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

from .funcoes import CIDADES, ESTADOS

class ManagerUsuario(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)


    def create_superuser(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)

class Usuario(AbstractUser):
    # new_user = Usuario(username='teste', email='teste@teste.com', first_name='teste', last_name='teste', password='Teste@123')

    email = models.EmailField('E-mail', unique=True)
    estado = models.CharField('Estado', max_length=2, choices=ESTADOS, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=10, choices=CIDADES, blank=True, null=True)

    data_nascimento = models.DateField("Data de Nascimento", null=True)

    amigos = models.ManyToManyField("self", db_table="Amigos", blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']

    objects = ManagerUsuario()

    def __str__(self):
        return self.username

    def enviar_pedido_amizade(self, user_recebido):
        meus_pedidos = self.user_enviado.all()
        if user_recebido not in meus_pedidos.filter(user_recebido=user_recebido):
            pedido_amizade = PedidosAmizade(user_enviado=self, user_recebido=user_recebido)
            pedido_amizade.save()
            pedido_amizade.get_amigos_comum()
    
    def get_amigos_comum(self, user):
        amigos = [amigo for amigo in self.amigos.all() if amigo in user.amigos.all()]
        num_amigos = len(amigos)
        return num_amigos
    
    def atualizar_registro(self, values):
        for field in values.keys():
            if field == 'username':
                if values[field] != self.username:
                    self.username = values[field] 
            elif field == 'email':
                if values[field] != self.email:
                    self.email = values[field] 
            elif field == 'first_name':
                if values[field] != self.first_name:
                    self.first_name = values[field] 
            elif field == 'last_name':
                if values[field] != self.last_name:
                    self.last_name = values[field] 
            elif field == 'cidade':
                if values[field] != self.cidade:
                    self.cidade = values[field]
            elif field == 'estado':
                if values[field] != self.estado:
                    self.estado = values[field]
            elif field == 'data_nascimento':
                if values[field] != self.data_nascimento:
                    self.data_nascimento = values[field]

        self.save()
    
class PedidosAmizade(models.Model):
    create_date = models.DateField(auto_now=True)
    user_enviado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='user_enviado')
    user_recebido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='user_recebido')
    aceito = models.BooleanField('Aceito', default=False)
    amigos_comum = models.ManyToManyField(Usuario)

    def get_amigos_comum(self):
        amigos_comum = [amigo for amigo in self.user_enviado.amigos.all() if amigo in self.user_recebido.amigos.all()]
        for amigo in amigos_comum:
            self.amigos_comum.add(amigo)

    def aceitar_pedido(self):
        self.user_enviado.amigos.add(self.user_recebido)
        self.aceito = True
        self.save()
    
    def recusar_pedido(self):
        self.delete()