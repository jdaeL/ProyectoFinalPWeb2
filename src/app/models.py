from django.db import models
from config import settings
from django.contrib.auth.models import User


class Chicharrones_LaJulia(models.Model):
    # aumentarle mas códigos para enlazar con otras tablas
    cod_ruc = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    direccion = models.CharField(max_length=300)
    telefono =  models.IntegerField()

    # claves foraneas
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cod_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cod_platos = models.ForeignKey(Platos, on_delete=models.CASCADE)
    cod_almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
        

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
