from django.db import models

class Chicharrones_LaJulia:
    cod_ruc = models.ForeignKey()                   #key
    direccion = models.CharField(max_length=300)
    telefono =  models.IntegerField()
