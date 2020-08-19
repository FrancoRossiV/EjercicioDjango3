from django.contrib import admin
from Biblioteca_3.models import *



class PrestamoInLine(admin.TabularInline):
    model = Prestamo


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'telefono','numLibros', 'adeudo')
    inlines = [PrestamoInLine,]

    fieldsets = (
        ('Datos Personales', {
            'fields': ('nombre', 'apellido')
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono', 'numLibros', 'adeudo')
        })
    )

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'telefono','numEmpleado', 'numLibros', 'adeudo')

    fieldsets = (
        ('Datos Personales', {
            'fields': ('nombre', 'apellido')
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono', 'numEmpleado', 'numLibros', 'adeudo')
        })
    )

class LibroAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'anio', 'tipoMaterial','status', 'editorial')
    list_filter = ('titulo',)

class RevistaAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'anio', 'tipoMaterial','status', 'paginas')
    list_filter = ('titulo',)

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('fechaSalida', 'fechaRegreso','prestamoAlumno', 'prestamoProfesor')
    

# Register your models here.
admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Material, )
admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Persona)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)