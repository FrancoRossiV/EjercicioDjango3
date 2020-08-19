from django.db import models

# Create your models here.

class Material(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipoMaterial = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    anio = models.DateField()
    status= models.CharField(max_length=50)


class Libro(Material):
    editorial = models.CharField(max_length=50)    

class Revista(Material):
    paginas = models.IntegerField()

class Persona(models.Model):
    tipoPersona = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    numLibros = models.IntegerField()
    adeudo = models.IntegerField()

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    numEmpleado = models.IntegerField()   


class Prestamo(models.Model):
    codigo = models.AutoField(primary_key=True)
    fechaSalida = models.DateField()
    fechaRegreso = models.DateField()
    prestamoLibro = models.ManyToManyField(Libro, blank = True, null = True)
    prestamoRevista = models.ManyToManyField(Revista, blank = True, null = True)  
    prestamoAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default = None, blank = True, null = True)  
    prestamoProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, default = None, blank = True, null = True) 

