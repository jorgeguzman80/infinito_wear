from django.db import models

# Create your models here.
class libro (models.Model):
    id = models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100, verbose_name='categoria')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='imagen', null=True)
    descripcion = models.TextField( verbose_name='Descripcion',null=True)
    
    def __str__(self):
        fila = "Categoria " + self.titulo + "-" "descripcion" ":" + self.descripcion
        return fila

    def delete (self,using=None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        