from datetime import datetime
#importo la clase conexion para tener conexion a la base de datos
import conexion as con
#importo pandas para poder ejecutar querys en la base
import pandas as pd


class Banco:
    #funcion Cargar clientes
    #funcion cargar cuentas
    #funcion crear cliente
    #funcion crear cuenta
    #funcionar cliente en array
    #funcionar cuenta en array
    #funcionar empleado en array
    def __init__(self):
        self.clientes=[]    #objeto de la clase cliente
        self.cuentas=[]      #objeto de la clase cliente
        self.empleados=[]      #objeto de la clase cliente

    #carga de arrays
    def cargar_clientes(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from clientes"
        #ejecuto el sql y lo cargo en el array de clientes
        self.clientes = pd.read_sql_query(sql,conn)
        conn.close()
    
    def cargar_cuentas(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from cuentas"
        #ejecuto el sql y lo cargo en el array de clientes
        self.cuentas = pd.read_sql_query(sql,conn)
        conn.close()

    def cargar_empleados(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from employees"
        #ejecuto el sql y lo cargo en el array de clientes
        self.cuentas = pd.read_sql_query(sql,conn)
        conn.close()

    #mostrar arrays
    def mostrar_clientes(self):
        return self.clientes

    def mostrar_cuentas(self):
        return self.cuentas

    def mostrar_empleados(self):
        return self.empleados

    def crear_cliente (self):
        cliente = Cliente
        cliente.cargar_cliente()
        self.clientes.append(cliente)

    def crear_cuenta (self, Cliente, tipo_cuenta, monto):
        cliente = Cliente
        if(tipo_cuenta == 1): #1 = caja de ahorro
            cuenta_caja = CajaDeAhorro(cliente,monto)
            self.cuentas.append(cuenta_caja)
        else:
            interes = float(input("Ingrese interes: "))
            plazo = float(input("Ingrese plazo: "))
            cuenta_pf = PlazoFijo(cliente,monto,plazo,interes)
            self.cuentas.append(cuenta_pf)

    def crear_empleado (self):
        empleado = Empleado
        empleado.cargar_empelado()
        self.empleados.append(empelado)
     

'''   def depositos_totales(self): #funcion que sume todos los montos de las cuentas x clientes
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
'''      
class Cuenta:
    
    def __init__ (self,Cliente, monto):
        self.cliente=Cliente
        self.monto=monto
        self.nro_cuenta = "001" + datetime.now()
        
    def imprimir(self):
        print("Titular: ", self.cliente.nombre)
        print("Nro Cuenta: ", self.nro_cuenta)
        print("Monto: ", self.monto)
        
    def depositar(self,monto):   #metodo para sumar un deposito al monto del cliente
        self.monto=self.monto+monto

    def extraer(self,monto):     #metodo para extraer y actualiza el valor de la cuenta del cliente
        self.monto=self.monto-monto

    def retornar_monto(self):     #metodo para mostar el saldo de cada cliente, me sirve para luego sumar todos los montos y sacar el dinero que tiene el banco
        return self.monto
           
class CajaDeAhorro(Cuenta):   #clase CDA hereda la clase cuenta
     #lo hereda de la clase cuenta, lo llamo
        
    def imprimir(self):
        print("Cuenta Caja de Ahorro")
        super().imprimir()    #llamo al imprimir de la clase padre
        
class PlazoFijo(Cuenta):
    
    def __init__(self, Cliente, monto, plazo, interes):   #plazo fijo ademas de los atributos titular y monto tiene un plazo e interes de ese plazo
        super().__init__(Cliente,monto)
        self.plazo=plazo   #inicializo el atributo plazo y le copio lo que llega en el parámetro
        self.monto = monto    #inicializo el atributo interes y le copio lo que llega en el parámetro
        self.plazo = plazo
        self.interes = interes
        
    def imprimir(self):
        print("Cuenta de Plazo Fijo")
        super().imprimir()
        print("Plazo en días: ", self.plazo)
        print("Intereses: ", self.interes)
        self.ganancia()
          
    def ganancia(self):
        ganancia=self.monto*self.interes/100
        return ganancia

# creamos la clase Cliente
class Cliente:

    def __init__(self):
        self.nombre = ""
        self.telefono = 0
        self.mail = ""
    
    def cargar_cliente(self):
        self.nombre = input("Nombre: " )
        self.telefono = int(input("Telefono: "))
        self.mail = input("Nombre: " )

#creo un cliente
cliente = Cliente()
cliente.cargar_cliente()

#creo un una caja de ahorro
#solicito monto
monto = float(input("Ingrese inicial de caja de ahorro: "))
#instancio el objeto caja de ahorro
ca_cliente = CajaDeAhorro(cliente, monto)

#crear un plazo fijo
#solicito los datos del plazo fijo
interes = float(input("Ingrese interes: "))
plazo = float(input("Ingrese plazo: "))
monto = float(input("Ingrese monto: "))

pf_ciente = PlazoFijo(cliente,monto,plazo,interes)
