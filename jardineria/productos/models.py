from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    nombre=models.CharField(primary_key=True, max_length=8, verbose_name="Nombre")
    tipo= models.CharField(max_length=50, verbose_name="Tipo")
    precio=models.CharField(max_length=50, verbose_name="Precio")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.nombre
class Contacto(models.Model):
    usuario=models.CharField(primary_key=True, max_length=8, verbose_name="Usuario")
    correo= models.CharField(max_length=50, verbose_name="Correo")
    telefono=models.CharField(max_length=50, verbose_name="Telefono")
    problema=models.CharField(max_length=50, verbose_name="Problema")
    imagen2=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen2")
    

    def __str__(self):
        return self.usuario       