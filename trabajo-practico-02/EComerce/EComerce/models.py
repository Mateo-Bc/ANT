from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.nombre) + ' | ' + str(self.telefono)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length = 50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)

#el stock debe almacenar cada producto y la cantidad del mismo disponible. De ser 0, no se pueden realizar ventas con dicho bien.
class Stock(models.Model):
    id = models.AutoField(primary_key=True)

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.producto)

#una venta es una transacción de cierto producto cotizado a cierto valor, por lo que venta contiene un producto y el precio del mismo.
class Venta(models.Model):
    id = models.AutoField(primary_key=True)

    articulo = models.ForeignKey(Stock, on_delete=models.CASCADE, blank=True, null=True)
    precioUnidad = models.IntegerField(blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)

    

    def precio_total(self):
        return self.precioUnidad * self.unidades

    def __str__(self):
        return str(self.articulo.producto.nombre)

#el carro contiene productos cotizados en cierto valor que puede variar, entonces, para evitar cambios, asignamos que el carro es el conjunto de ventas de cada objeto cotizado en x valor durante el momento de la compra.
class Carro(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        pass