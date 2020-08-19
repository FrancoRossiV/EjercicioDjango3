from django.db import models

# Create your models here.

class Material(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipoMaterial = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    anio = models.DateField()
    status= models.CharField(max_length=50)

    def __str__(self):
        return "Material: " + str(self.Codigo) + " " + str(self.tipoMaterial) + " " + str(self.autor) + " " + str(self.titulo) + " " + str(self.anio) + " " + str(self.status)


class Libro(Material):
    editorial = models.CharField(max_length=50)

    def __str__(self):
        return "Libro: " + str(self.codigo) + " " + str(self.tipoMaterial) + " " + str(self.autor) + " " + str(self.titulo) + " " + str(self.anio) + " " + str(self.status) + " " + str(self.editorial)
    

class Revista(Material):
    paginas = models.IntegerField()

    def __str__(self):
        return "Revista: " + str(self.codigo) + " " + str(self.tipoMaterial) + " " + str(self.autor) + " " + str(self.titulo) + " " + str(self.anio) + " " + str(self.status) + " " + str(self.paginas)


class Persona(models.Model):
    tipoPersona = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    numLibros = models.IntegerField()
    adeudo = models.IntegerField(null = True)

    def __str__(self):
        return "Persona: " + str(self.tipoPersona) + " " + str(self.nombre) + " " + str(self.apellido) + " " + str(self.correo) + " " + str(self.telefono) + " " + str(self.numLibros) + " " + str(self.adeudo)


class Alumno(Persona):
    matricula = models.IntegerField()

    def __str__(self):
        return "Alumno: " + str(self.tipoPersona) + " " + str(self.nombre) + " " + str(self.apellido) + " " + str(self.correo) + " " + str(self.telefono) + " " + str(self.numLibros) + " " + str(self.adeudo) + " " + str(self.matricula)



class Profesor(Persona):
    numEmpleado = models.IntegerField()   

    def __str__(self):
        return "Persona: " + str(self.tipoPersona) + " " + str(self.nombre) + " " + str(self.apellido) + " " + str(self.correo) + " " + str(self.telefono) + " " + str(self.numLibros) + " " + str(self.adeudo) + " " + str(self.numEmpleado)


class Prestamo(models.Model):
    codigo = models.AutoField(primary_key=True)
    fechaSalida = models.DateField()
    fechaRegreso = models.DateField()
    prestamoLibro = models.ManyToManyField(Libro, blank = True, null = True)
    prestamoRevista = models.ManyToManyField(Revista, blank = True, null = True)  
    prestamoAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default = None, blank = True, null = True)  
    prestamoProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, default = None, blank = True, null = True) 

    def __str__(self):
        return "Prestamo: " + str(self.codigo) + " " + str(self.fechaSalida) + " " + str(self.fechaRegreso) + " " + str(self.prestamoLibro) + " " + str(self.prestamoRevista) + " " + str(self.prestamoAlumno) + " " + str(self.prestamoProfesor) 

