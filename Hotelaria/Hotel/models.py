from django.db import models

# Create your models here.
class homepage(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    logo = models.ImageField(upload_to='homepage/')

    def __str__(self):
        return self.titulo
    

class quarto(models.Model):

    tipo_quarto = [
        ("Solteiro", "Solteiro"),
        ("Premium", "Premium"),
        ("Plus", "Plus"),
    ]

    num_Quarto = models.IntegerField()
    qtd_Hospedes = models.IntegerField()
    tipo = models.CharField(max_length=20, choices=tipo_quarto)
    valor = models.FloatField()
    descricao = models.TextField(max_length=300)
    status = models.BooleanField(default=True)
    img = models.ImageField(upload_to='quarto/')

    def __str__(self):
        x = f"{self.tipo} - {self.num_Quarto}"
        return x
