from datetime import datetime
#importo la clase conexion para tener conexion a la base de datos
import conexion as con
#importo pandas para poder ejecutar querys en la base
import pandas as pd
#Manejo los menus
import os
import time 
import csv
import itertools
import re
 
if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

class Cuenta:
    
    def __init__ (self,Cliente, monto):
        self.cliente=Cliente
        self.monto=monto
        date= datetime.now()
        #se crea el n° de cuenta automaticamente utilizando el dni del cliente + la fecha
        self.nro_cuenta = self.cliente.dni + date.year + date.month+date.hour+date.minute +date.second
        
    def imprimir(self):
        print("Titular: ", self.cliente.nombre)
        print("Nro Cuenta: ", self.nro_cuenta)
        print("Monto: ", self.monto)
        
    def depositar(self,monto):   #metodo para sumar un deposito al monto del cliente
        self.monto=self.monto+monto

    def extraer(self,monto):     #metodo para extraer y actualiza el valor de la cuenta del cliente
        self.monto=self.monto-monto

    def mostrar_saldo(self):     #metodo para mostar el saldo de cada cliente, me sirve para luego sumar todos los montos y sacar el dinero que tiene el banco
        return self.monto

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

class CajaDeAhorro(Cuenta):   #clase CDA hereda la clase cuenta
     #lo hereda de la clase cuenta, lo llamo
        
    def imprimir(self):
        print("Cuenta Caja de Ahorro")
        super().imprimir()    #llamo al imprimir de la clase padre

# creamos la clase Cliente
class Cliente:

    def __init__(self):
        self.nombre = ""
        self.dni = ""
        self.telefono = 0
        self.mail = ""
    
    def cargar_cliente(self):
        self.nombre = input("Nombre: " )
        self.dni = int(input("DNI: "))
        self.telefono = int(input("Telefono: "))
        self.mail = input("mail: " )

    def modificar_cliente(self):
        # cuando elegimos modificar, modificamos los atributos del objeto
                print("\u001B[32m          ********************************************")
                print("\u001B[32m          ********************************************")
                self.nombre = str(input("\u001B[37m                   Ingrese el nombre: "))
               # self.dni = str(input("\u001B[37m                   Ingrese el dni: "))
                self.telefono = str(input("\u001B[37m                   Ingrese el telefono: "))
                self.mail = str(input("\u001B[37m                   Ingrese el mail: "))
               # sql = "update clientes set nombre = '" + self.nombre + "', telefono = " + self.telefono + ", mail = '" + self.mail + " where dni = " + self.dni + ";"

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
        self.cliente = Cliente()
        self.plazo_fijo = PlazoFijo()
        self.caja_ahorro = CajaDeAhorro()

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
    #crear
    def crear_cliente (self):
        cliente = Cliente
        cliente.cargar_cliente()
        self.clientes.append(cliente)
        return cliente

    def crear_cuenta (self, Cliente, tipo_cuenta, monto):
        cliente = Cliente
        if(tipo_cuenta == 1): #1 = caja de ahorro
            cuenta_caja = CajaDeAhorro(cliente,monto)
            self.cuentas.append(cuenta_caja)
            return cuenta_caja
        else:
            interes = float(input("Ingrese interes: "))
            plazo = float(input("Ingrese plazo: "))
            cuenta_pf = PlazoFijo(cliente,monto,plazo,interes)
            self.cuentas.append(cuenta_pf)
            return cuenta_pf
    
    #Funcion buscar cliente en el array
    def buscar_cliente(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
    
    #Funcion buscar cuenta en el array
    def buscar_cuenta(self, nro_cuenta):
        for cuenta in self.cuentas:
            if cuenta.nro_cuenta == nro_cuenta:
                return cuenta

    #Funcion buscar Cuentas en el array
    def buscar_cuentas_clientes(self, Cliente):
        cuentas_clientes = []
        for cuenta in self.cuentas:
            if cuenta.Cliente == Cliente:
                cuentas_clientes.append(cuenta)
        return cuentas_clientes

datetime.now()