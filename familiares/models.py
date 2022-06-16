from django.db import models

class Familia(models.Model):
    PARIENTE = (
        (1, "ABUELA"),
        (2, "ABUELO"),
        (3, "MADRE"),
        (4, "PADRE"),
        (5, "HERMANA"),
        (6, "HERMANO"),
        (7, "HIJA/O")
    )
    parentezco = models.PositiveIntegerField("Parentezco", choices=PARIENTE)
    nombre = models.CharField("Nombre",max_length=15)
    apellido = models.CharField("Apellido",max_length=15)
    edad = models.IntegerField("Edad")
    
