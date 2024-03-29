from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Cursos(models.Model): #Define la estructura de nuestra tabla
    IdCurso = models.SmallIntegerField(primary_key=True,verbose_name="Id curso")
    nombreCurso = models.TextField(max_length=30,verbose_name="Nombre del Curso")
    Descripcion = models.TextField(verbose_name="Descripción del Curso")
    Cupo = models.PositiveSmallIntegerField(verbose_name="Cupos Disponibles")
    FechaInicio = models.DateField(verbose_name="Fecha de Inicio")
    FechaFinal = models.DateField(verbose_name="Fecha de Fin de curso")
    Comentario= models.TextField(max_length=120,verbose_name="Comentarios del Curso")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateField(auto_now_add=True) 
    updated = models.DateField(auto_now_add=True) 

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["-created"]
        #El - Ordenado del más reciente a más nuevo
    
    def __str__(self):
        return self.nombreCurso
        #Mostrado por nombre
        
class Actividad(models.Model):
    IdActividad= models.SmallIntegerField(primary_key=True,verbose_name="Id Actividad")
    NombreActividad= models.TextField(max_length=30,verbose_name="Nombre de la Actividad")
    ComentActividad = RichTextField(verbose_name="Comentario de la Actividad")
    created = models.DateField(auto_now_add=True,verbose_name="Creado el") 
    
    class Meta:
        verbose_name = "actividad"
        verbose_name_plural = "actividades"
        ordering = ["-created"]
    
    def __str__(self):
        return self.NombreActividad

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave")
    usuario = models.TextField(verbose_name="nombre")
    correo = models.TextField(verbose_name="correo")
    cursos = models.TextField(verbose_name="cursos")
    mensaje= models.TextField(verbose_name="comentario")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
        #El - indica que se ordena del más reciente al mas viejo
    
    def __str__(self):
        return self.mensaje	