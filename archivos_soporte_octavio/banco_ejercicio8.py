class Banco:
    #funcion Cargar clientes
    #funcion cargar cuentas
    #funcion crear cliente
    #funcion crear cuenta
    
    
    def __init__(self):
        self.clientes=[]    #objeto de la clase cliente
        self.cuentas=[]      #objeto de la clase cliente

    def operar(self):               
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self): #funcion que sume todos los montos de las cuentas x clientes
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

class Cuenta:
    
    def __init__ (self,Cliente, monto):
        self.cliente=Cliente
        self.monto=monto
        
    def imprimir(self):
        print("Titular: ", self.cliente.nombre)
        print("Monto: ", self.monto)
        
    def depositar(self,monto):   #metodo para sumar un deposito al monto del cliente
        self.monto=self.monto+monto

    def extraer(self,monto):     #metodo para extraer y actualiza el valor de la cuenta del cliente
        self.monto=self.monto-monto

    def retornar_monto(self):     #metodo para mostar el saldo de cada cliente, me sirve para luego sumar todos los montos y sacar el dinero que tiene el banco
        return self.monto

    def imprimir(self):         #metodo
        print(self.nombre," Tiene depositado la suma de: ",self.monto)
           
class CajaDeAhorro(Cuenta):   #clase CDA hereda la clase cuenta
    
    def __init__ (self, titular, monto) : 
        super().__init__(titular, monto)   #lo hereda de la clase cuenta, lo llamo
        
    def imprimir(self):
        print("Cuenta Caja de Ahorro")
        super().imprimir()    #llamo al imprimir de la clase padre
        
class PlazoFijo(Cuenta):
    
    def __init__(self, titular, monto, plazo, interes):   #plazo fijo ademas de los atributos titular y monto tiene un plazo e interes de ese plazo
        super().__init__(titular,monto)
        self.plazo=plazo   #inicializo el atributo plazo y le copio lo que llega en el parámetro
        self.interes=interes    #inicializo el atributo interes y le copio lo que llega en el parámetro
        
    def imprimir(self):
        print("Cuenta de Plazo Fijo")
        super().imprimir()
        print("Plazo en días: ", self.plazo)
        print("Intereses: ", self.interes)
        self.ganancia()
        
    def ganancia(self):
        ganancia=self.monto*self.interes/100
        print("Monto de Intereses: ", ganancia)

# creamos la clase Cliente
class Cliente:
    def __init__(self,nombre,telefono,mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail
    
    def cargar_cliente(self):
        self.nombre = input("Nombre: " )
        self.telefono = int(input("Telefono: "))
        self.mail = input("Nombre: " )
    
