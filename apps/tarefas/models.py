from django.db import models

# Create your models here.

class Categoria(models.Model) :
    nome = models.CharField('Nome',max_length=50)
    descricao = models.TextField('Descrição', blank=True, null=True)

    def __str__(self):
        return self.nome


class Tarefas(models.Model):
    PRIORIDADE_CHOICE = (
        (1, 'Alta'),
        (2, 'Média'),
        (3, 'Baixa'),
    )

    STATUS_CHOICE= (
        ('AF', 'A Fazer'),
        ('PD', 'Pendente'),
        ('CD', 'Concluída'),
    )

    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição')
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE)
    prioridade = models.PositiveIntegerField('Prioridade', choices=PRIORIDADE_CHOICE)
    status = models.CharField('Status',max_length=2, choices=STATUS_CHOICE, default='AF')

    def __str__(self):
        return self.titulo
