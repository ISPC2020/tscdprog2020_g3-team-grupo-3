from datetime import datetime
#importo la clase conexion para tener conexion a la base de datos
import conexion as con
#importo pandas para poder ejecutar querys en la base
import pandas as pd
#Manejo los menus
import os
import time 
 
if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"


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

    #funcion crear un empleado        
    def crear_empleado (self):
        empleado = Empleado
        empleado.cargar_empleado()
        self.empleados.append(empleado)

    #funcion menu cliente
    def main_cliente(self):
        time.sleep(1)
        os.system(var)
        self.cargar_clientes();
        cliente = Cliente()
        print("****************************************************")
        print("\n****   MENU CLIENTES ****","\n")
        print("****************************************************")
        while True:
            try:
                print("****************************************")
                print("*                                      *")
                print("*         MENU PRINCIPAL               *")
                print("*                                      *")
                print("****************************************")
                print("\nDigite una opcion: \n\n"
                
                    "  1) Buscar Cliente\n"
                    "  2) Crear Cliente\n"
                    "  7) Volver Menu Anterior")

                opcion = input("\nDigite una opcion: ")
            
                #Opcion BUSCAR CLIENTE
                if opcion == "1":
                    dni = float(input("Buscar Cliente - Ingrese DNI: "))
                    cliente = self.buscar_cliente(dni)
                    print("Cliente encontrado: ", cliente)
                #Opcion Crear Cliente                      
                elif opcion == "2":
                   cliente = self.crear_cliente()
                   print("Cliente creado: ", cliente)
                #Opcion volver al menu anterior    
                elif opcion =="7": 
                    self.main()       
            except ValueError:
                print("\nOpción incorrecta, intentelo nuevamente")
#Menues
    #funcion menu cliente Cuentas
    def main_cliente_cuentas(self, Cliente="[]"):
        time.sleep(1)
        os.system(var)
        self.cargar_clientes();
        cliente = Cliente
        print("****************************************************")
        print("\n****   MENU CLIENTES CUENTAS ****","\n")
        print("****************************************************")
        while True:
            try:
                print("****************************************")
                print("*                                      *")
                print("*         MENU PRINCIPAL ", cliente.nombre ,"               *")
                print("*                                      *")
                print("****************************************")
                print("\nDigite una opcion: \n\n"
                
                    "  1) Buscar Cuentas \n"
                    "  2) Crear Cuentas \n"
                    "  7) Volver Menu Anterior")

                opcion = input("\nDigite una opcion: ")
            
                #Opcion BUSCAR CLIENTE
                if opcion == "1":
                   cuentas = self.buscar_cuentas_clientes(cliente)
                   print(cuentas)
                   cuenta_opera = input("\nDigite el numero de cuenta que quiere operar: ")
                   cuenta_opera = self.buscar_cuenta(cuenta_opera)

                #Opcion Crear Cliente                      
                elif opcion == "2":
                    print("\nDigite una opcion: \n\n"
                
                    "  1) Caja de Ahorro \n"
                    "  2) Plazo Fijo \n"
                    "  7) Volver Menu Anterior")
                    tipo_cuenta = input("\nDigite una opcion: ")
                    monto = input("\nIngrese el monto inicial: ")
                    cuenta = self.crear_cuenta(cliente, tipo_cuenta,monto)
                    print("Cuenta creada: ", cuenta)
                #Opcion volver al menu anterior    
                elif opcion =="7": 
                    self.main()       
            except ValueError:
                print("\nOpción incorrecta, intentelo nuevamente")

    #funcion menu cliente Cuentas
    def main_cuentas(self, Cliente):
        time.sleep(1)
        os.system(var)
        self.cargar_cuentas();
        cliente = Cliente
        print("****************************************************")
        print("\n****   MENU CUENTAS ****","\n")
        print("****************************************************")
        while True:
            try:
                print("****************************************")
                print("*                                      *")
                print("*         MENU PRINCIPAL ", cliente.nombre ,"               *")
                print("*                                      *")
                print("****************************************")
                print("\nDigite una opcion: \n\n"
                
                    "  1) Buscar Cuentas \n"
                    "  2) Crear Cuentas \n"
                    "  7) Volver Menu Anterior")

                opcion = input("\nDigite una opcion: ")
            
                #Opcion BUSCAR CLIENTE
                if opcion == "1":
                   cuentas = self.buscar_cuentas_clientes(cliente)
                   print(cuentas)
                   cuenta_opera = input("\nDigite el numero de cuenta que quiere operar: ")
                   cuenta_opera = self.buscar_cuenta(cuenta_opera)

                #Opcion Crear Cliente                      
                elif opcion == "2":
                    print("\nDigite una opcion: \n\n"
                
                    "  1) Caja de Ahorro \n"
                    "  2) Plazo Fijo \n"
                    "  7) Volver Menu Anterior")
                    tipo_cuenta = input("\nDigite una opcion: ")
                    monto = input("\nIngrese el monto inicial: ")
                    cuenta = self.crear_cuenta(cliente, tipo_cuenta,monto)
                    print("Cuenta creada: ", cuenta)
                #Opcion volver al menu anterior    
                elif opcion =="7": 
                    self.main()       
            except ValueError:
                print("\nOpción incorrecta, intentelo nuevamente")
        
    def main_cuenta_ch(self, Cliente, CajaDeAhorro):
            time.sleep(1)
            os.system(var)
            self.cargar_clientes();
            cliente = Cliente
            print("****************************************************")
            print("\n****   MENU CUENTAS ****","\n")
            print("****************************************************")
            while True:
                try:
                    print("****************************************")
                    print("*                                      *")
                    print("*         MENU PRINCIPAL ", cliente.nombre ,"               *")
                    print("*                                      *")
                    print("****************************************")
                    print("\nDigite una opcion: \n\n"
                    
                        "  1) Buscar Cuentas \n"
                        "  2) Crear Cuentas \n"
                        "  7) Volver Menu Anterior")

                    opcion = input("\nDigite una opcion: ")
                
                    #Opcion BUSCAR CLIENTE
                    if opcion == "1":
                        cuentas = self.buscar_cuentas_clientes(cliente)
                        print(cuentas)
                        cuenta_opera = input("\nDigite el numero de cuenta que quiere operar: ")
                        cuenta_opera = self.buscar_cuenta(cuenta_opera)

                    #Opcion Crear Cliente                      
                    elif opcion == "2":
                        print("\nDigite una opcion: \n\n"
                    
                        "  1) Caja de Ahorro \n"
                        "  2) Plazo Fijo \n"
                        "  7) Volver Menu Anterior")
                        tipo_cuenta = input("\nDigite una opcion: ")
                        monto = input("\nIngrese el monto inicial: ")
                        cuenta = self.crear_cuenta(cliente, tipo_cuenta,monto)
                        print("Cuenta creada: ", cuenta)
                    #Opcion volver al menu anterior    
                    elif opcion =="7": 
                        self.main()       
                except ValueError:
                    print("\nOpción incorrecta, intentelo nuevamente")
    #funcion menu principal
    def main():
        time.sleep(1)
        os.system(var)
        banco = Banco()
        print("****************************************************")
        print("\n****   BIENVENIDO AL BANCO ISPC CÓRDOBA ****","\n")
        print("****************************************************")
        while True:
            try:
                print("****************************************")
                print("*                                      *")
                print("*         MENU PRINCIPAL               *")
                print("*                                      *")
                print("****************************************")
                print("\nDigite una opcion: \n\n"
                
                    "  1) Clientes\n"
                    "  2) Cuentas\n"
                    "  3) Empleados\n"
                    "  7) Salir")

                opcion = input("\nDigite una opcion: ")
            
                
                if opcion == "1":
                    banco.agregar_cliente()

                elif opcion == "2":
                    dni = int(input("\nDigite el DNI del usuario que desea buscar: "))
                    print("======================================================")
                    banco.mostrar_cliente(dni)
                    print("======================================================")
                    
                    
                    
                elif opcion =="7": 
                    dni = input("Ingrese DNI del Usuario a Eliminar: ")
                # if cliente(dni).delete():    
                    # print("Cliente Eliminado Correctamente")
                
            
                    #usuarios.eliminar[dni]
                    #self.usuarios(dni)
                    #remove.banco.mostrar_cliente(dni)
                    #print("El Usuario fue eliminado del Sistema")
                    
                    
            except ValueError:
                print("\nOpción incorrecta, intentelo nuevamente")
                
                

    if __name__=='__main__':
        main()

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
        self.dni = ""
        self.telefono = 0
        self.mail = ""
    
    def cargar_cliente(self):
        self.nombre = input("Nombre: " )
        self.dni = int(input("DNI: "))
        self.telefono = int(input("Telefono: "))
        self.mail = input("mail: " )

class Empleado:
    
    def __init__(self):
        self.nombre = ""
        self.dni = ""
        self.telefono = 0
        self.mail = ""
    
    def cargar_empleado(self):
        self.nombre = input("Nombre: " )
        self.dni = int(input("DNI: "))
        self.telefono = int(input("Telefono: "))
        self.mail = input("mail: " )

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
