class Vector():
    ##atributos##
    vector_x=0              ##coordenadas x del vector
    vector_y=0              ##coordenadas y del vector
    vector_z=0              ##coordenadas z del vector
    ##fin atributos##

    ##Metodos##
    def __init__(self,x,y,z):
        self.vector_x=x
        self.vector_y=y
        self.vector_z=z

    def imprimir(self):
        print(self.vector_x,",",self.vector_y,",",self.vector_z)

    def addition(self,b):
        result_vector_x=self.vector_x + b.vector_x
        result_vector_y=self.vector_y + b.vector_y
        result_vector_z=self.vector_z + b.vector_z
        s = Vector(result_vector_x,result_vector_y,result_vector_z)
        return s

    def subtraccion(self,b):
        result_vector_x=self.vector_x - b.vector_x
        result_vector_y=self.vector_y - b.vector_y
        result_vector_z=self.vector_z - b.vector_z
        r = Vector(result_vector_x,result_vector_y,result_vector_z)
        return r

    def cross_product(self,b):
        result_vector_x=(self.vector_y * b.vector_z)-(self.vector_z * b.vector_y)
        result_vector_y=-(self.vector_x * b.vector_z)-(self.vector_z * b.vector_x)
        result_vector_z=(self.vector_x * b.vector_y)-(self.vector_y * b.vector_x)
        c = Vector(result_vector_x,result_vector_y,result_vector_z)
        return c

    def product_point(self,b):
        result_vector_x=self.vector_x * b.vector_x
        result_vector_y=self.vector_y * b.vector_y
        result_vector_z=self.vector_z * b.vector_z
        p = (result_vector_x + result_vector_y + result_vector_z)
        return p

     




print("Ingrese coordenadas para el eje x: ")
x = int(input())
print("Ingrese coordenadas para el eje y: ")
y = int(input())
print("Ingrese coordenadas para el eje z: ")
z = int(input())
a=Vector(x,y,z)
a.imprimir()

print("Ingrese otras coordenadas para el eje x: ")
x = int(input())
print("Ingrese otras coordenadas para el eje y: ")
y = int(input())
print("Ingrese otras coordenadas para el eje z: ")
z = int(input())
b=Vector(x,y,z)
b.imprimir()

print("Suma: ")
s=a.addition(b)
s.imprimir()

print("Resta: ")
r=a.subtraccion(b)
r.imprimir()

print("Producto cruzado: ")
c=a.cross_product(b)
c.imprimir()

print("Producto punto: ")
p=a.product_point(b)
print(p)
