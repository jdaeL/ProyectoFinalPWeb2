from django.db import models

class Chicharrones_LaJulia:
    # aumentarle mas códigos para enlazar con otras tablas
    cod_ruc = models.ForeignKey()                   #key
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
