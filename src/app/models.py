from django.db import models
from config import settings
from django.contrib.auth.models import User


class Chicharrones_LaJulia(models.Model):

    cod_ruc = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    direccion = models.CharField(max_length=300)
    telefono =  models.IntegerField()

    # claves foraneas
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cod_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cod_platos = models.ForeignKey(Platos, on_delete=models.CASCADE)
    cod_almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
        

class Cliente:
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Proveedor:
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Empleado: 
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Cargo:
    nombre_cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_cargo

class Plato:
    pass

class Plato_detalles:
    pass

class Cliente:
    pass



# para almacen, adicionalmente se podría implementar
class Almacen:
    pass

#class Otras_tablas:
#    pass
