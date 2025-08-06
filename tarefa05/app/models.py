from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=400)
    dataPublicao = models.DateField(default='2025-01-01')
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)

    def __str__(self):
        return self.titulo