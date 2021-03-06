# Generated by Django 2.2 on 2020-08-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca_3', '0003_auto_20200819_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='prestamoAlumno',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblioteca_3.Alumno'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='prestamoLibro',
            field=models.ManyToManyField(blank=True, null=True, to='Biblioteca_3.Libro'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='prestamoProfesor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Biblioteca_3.Profesor'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='prestamoRevista',
            field=models.ManyToManyField(blank=True, null=True, to='Biblioteca_3.Revista'),
        ),
    ]
