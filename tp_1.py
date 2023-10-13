# TRABAJOS CASE_1

#Consigna 1

#Realizar un programa que, a su criterio, es más adecuado para ser resuelto con programación orientada a objetos.
# El programa debe tener al menos 3 clases.

# Nomina personal de un Diagrama establecido (Entendiendo por "Diagrama", el periodo de tiempo de trabajo en la zona de obra).

class Nomina():
    def __init__(self,nombre,edad,legajo,diagrama):
        
        self.nombre=nombre
        self.edad=edad
        self.legajo=legajo
        self.diagrama=diagrama
        

    def listado(self):
        lista=("Nombre: {}, Edad: {},Legajo: {}, Diagrama: {}")
        print(lista.format(self.nombre,self.edad,self.legajo,self.diagrama))

    def Primera_quincena(self):
        listado=("Nombre: {}, Edad: {},Legajo: {}, Diagrama: {}")
        print(listado.format(self.nombre,self.edad,self.legajo,self.diagrama))     


Personal1=Nomina("Ricardo","63 años","125","Descanso")

Personal1.listado()

Personal1=Nomina("Ricardo","63 años","125","Primera Quincena Septiembre")

Personal1.listado()

def Accidente(self):
        accidentado=("Nombre: {}, Edad: {},Legajo: {}, Diagrama: {}")
        print(accidentado.format(self.nombre,self.edad,self.legajo,self.diagrama))     

Personal1=Nomina("Ricardo","63 años","125","Accidente con retiro de obra")

Personal1.listado()


# Consigna 2

# Realizar un programa que, a su criterio, es m s adecuado para ser resuelto con programaci n funcional.

# Obtener el cuadrado de todos los elementos en la lista

def cuadrado(elemento=0):
    return elemento * elemento

lista=[1,2,3,4,5,6,7,8,9,10]
resultado=list(map(cuadrado,lista))
print(resultado)

# Obtener la cantidad de elementos mayores a 5 en la tupla.

def mayor_a_cinco(elemento):
    return elemento > 5

tupla=(5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado=tuple(filter(mayor_a_cinco,tupla))
resultado=len(resultado)
print(resultado)

# Obtener la suma de todos los elementos en la lista

lista=[1,2,3,4]
acumulador=0;

for elemento in lista:
    acumulador +=elemento

print(acumulador)
