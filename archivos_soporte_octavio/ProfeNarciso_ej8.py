# -*- coding: utf-8 -*-
"""
Created on Fri May  7 19:00:25 2021

@author: Admins
"""

# creamos nuestra clase agenda
class Agenda:
	# iniciamos nuestra clase
	def __init__(self):
		# crearemos una lista donde guardaremos los datos de nuestra agenda
		self.contactos=[]
 
 
	# función para añadir un contacto
	def anadir(self):
		print("---------------------")
		print("Añadir nuevo contacto")
		print("---------------------")
		nom=input("Introduzca el nombre: ")
		telf=int(input("Introduzca el teléfono: "))
		email=input("Introduzca el email: ")
		self.contactos.append({'nombre':nom,'telf':telf,'email':email})
		
 
	# función para imprimir la lista de contactos
	# En este caso imprimiremos solo los nombres de los contactos
	# con ellos podremos buscar luego un contacto
	def lista(self):
		print("------------------")
		print("Lista de contactos")
		print("------------------")
		if len(self.contactos) == 0:
			print("No hay ningún contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(self.contactos[x]['nombre'])
		
 
	# función para buscar un contacto a través del nombre
	def buscar(self):
		print("---------------------")
		print("Buscador de contactos")
		print("---------------------")
		nom=input("Introduzca el nombre del contacto: ")
		for x in range(len(self.contactos)):
			if nom == self.contactos[x]['nombre']:
				print("Datos del contacto")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telf'])
				print("E-mail: ",self.contactos[x]['email'])
				return x
# creamos la clase Cuenta
class Cuenta:
	# inicializamos los atributos de la clase
	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad

	# imprimimos los datos
	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)


# creamos la clase CajaAhorro
# esta clase hereda atributos de la clase Cuenta
class CajaAhorro(Cuenta):
	# iniciamos los atributos de la clase
	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)

	# imprimimos los datos de la cuenta
	def imprimir(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()


# creamos la clase PlazoFijo
# esta clase también hereda atributos de la clase Cuenta
class PlazoFijo(Cuenta):
	# inicializamos los atributos de la clase
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes


	# calculamos la ganancia
	def ganancia(self):
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)


	# imprimimos los resultados
	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()

# creamos la clase banco
class Banco:
    # inicializamos
    def __init__(self):
        self.cliente1=Cliente("Ivan")
        self.cliente2=Cliente("Marcos")
        self.cliente3=Cliente("Juan")
        

    # función para operar
    def operacion(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(300)
        self.cliente3.depositar(43)
        self.cliente1.extraer(400)

    # función para obtener los depósitos totales
    def depositos(self):
        total=self.cliente1.devolver_cantidad()+self.cliente2.devolver_cantidad()+self.cliente3.devolver_cantidad()
        print("El total de dinero del banco es: ",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()



# creamos la clase Cliente
class Cliente:
    # inicializamos
    def __init__(self,nombre):
        self.nombre=nombre
        self.cantidad=0
        self.CajaAhorro=CajaAhorro(self.nombre, 0)
        self.PlazoFijo=PlazoFijo(self.nombre,0,0,0)

    # función para depositar dinero
    def depositar(self,cantidad):
        self.cantidad+=cantidad

    # función para extraer dinero
    def extraer(self,cantidad):
        self.cantidad-=cantidad
    
    # función para obtener el total de dinero
    def devolver_cantidad(self):
        return self.cantidad

    # función para imprimir los datos del cliente
    def imprimir(self):
        print(self.nombre, " tiene depositada una cantidad de ",self.cantidad)

agenda1=Agenda()
agenda1.anadir()
agenda1.lista()


'''
banco1=Banco()
banco1.operacion()
banco1.depositos()
'''