from django.db import models
from config import settings
from django.contrib.auth.models import User


class Chicharrones_LaJulia(models.Model):
    # aumentarle mas códigos para enlazar con otras tablas
    cod_ruc = models.ForeignKey(User, on_delete=models.CASCADE)     #key
    direccion = models.CharField(max_length=300)
    telefono =  models.IntegerField()

class cliente:
    pass

class proovedor:
    pass

class empleado: 
    pass

class cargo:
    pass

class platos:
    pass

class plato_detalles:
    pass

class cliente:
    pass



# para almacen, adicionalmente se podría implementar
class almacen:
    pass

#class otras_tablas:
#    pass
