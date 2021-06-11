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

        '''date= datetime.now()
        #se crea el n° de cuenta automaticamente utilizando el dni del cliente + la fecha
        self.nro_cuenta = self.cliente.dni + date.year + date.month+date.hour+date.minute +date.second '''
        
    def imprimir(self):
        print("Titular: ", self.cliente.nombre)
        print("Nro Cuenta: ", self.nro_cuenta)
        print("Saldo: ", self.monto)
        
    def depositar(self,monto):   #metodo para sumar un deposito al monto del cliente
        self.monto=self.monto+monto

    def extraer(self,monto):     #metodo para extraer y actualiza el valor de la cuenta del cliente
        self.monto=self.monto-monto

    def mostrar_saldo(self):     #metodo para mostar el saldo de cada cliente, me sirve para luego sumar todos los montos y sacar el dinero que tiene el banco
        return self.monto

class PlazoFijo(Cuenta):
    
    def __init__(self):   #plazo fijo ademas de los atributos titular y monto tiene un plazo e interes de ese plazo
        super().__init__(Cliente,0)
        self.nro_cuenta     = 0
        self.plazo          = 0   #inicializo el atributo plazo y le copio lo que llega en el parámetro
        self.monto          = 0    #inicializo el atributo interes y le copio lo que llega en el parámetro
        self.interes        = 0
        self.fecha_creacion = ''

    def crear_plazo__fijo(self, Cliente, monto, plazo, interes ):
        super().__init__(Cliente,monto)
        date= datetime.now()
        self.nro_cuenta = self.cliente.dni + date.year + date.month+date.hour+date.minute +date.second
        self.plazo=plazo   #inicializo el atributo plazo y le copio lo que llega en el parámetro
        self.monto = monto    #inicializo el atributo interes y le copio lo que llega en el parámetro
        self.interes = interes
        self.fecha_creacion = datetime.now()
        
    def imprimir(self):
        print("Cuenta de Plazo Fijo")
        super().imprimir()
        print("Plazo en días: ", self.plazo)
        print("Intereses: ", self.interes)
        print("Ganancias: ", self.ganancia())
        
          
    def ganancia(self):
        ganancia=self.monto*self.interes/100
        return ganancia

class CajaDeAhorro(Cuenta):   #clase CDA hereda la clase cuenta
     #lo hereda de la clase cuenta, lo llamo
        
    def mostrar_saldo(self):
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
        sql= "insert in to clientes value"
    
    def buscar_cliente_base(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from clientes where dni = " + self.dni +";"
        result = pd.read_sql_query(sql,conn)
        for c in result:
            self.nombre = c["nombre"]
            self.dni = c["dni"]
            self.telefono = c["telefono"]
            self.mail = c["mail"]




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
        self.array_clientes=[]    #array de objetos
        self.array_plazo_fijo=[]   #array de objetos
        self.array_caja_ahorro=[]   #array de objetos
        self.array_empleados=[]     #array de objetos    
        self.cliente = Cliente()    #objeto individual inicializado en un objeto vacio
        self.plazo_fijo = PlazoFijo() #objeto individual inicializado en un objeto vacio
        self.caja_ahorro = CajaDeAhorro() #objeto individual inicializado en un objeto vacio

    #carga de arrays
    def cargar_clientes(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from clientes"
        #ejecuto el sql y lo cargo en el array de clientes
        self.array_clientes = pd.read_sql_query(sql,conn)
        conn.close()
        
    # metodos pora ordenar el array
    def ordenarxnombre(self):
        # Doc = https://docs.python.org/es/3/howto/sorting.html
        self.array_clientes.sort(key=lambda cliente: cliente.nombre)

    def ordenarxdni(self):
        self.array_clientes.sort(key=lambda cliente: cliente.dni)
    
    def cargar_plazo_fijo(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from plazos_fijos"
        #ejecuto el sql y lo cargo en un df para luego recorrer y crear el array de objetos
        df = pd.read_sql_query(sql,conn)
        for row in df:
            pf = PlazoFijo()
            pf.nro_cuenta = row["nro_cuenta"]
            pf.plazo = row["plazo"]
            pf.interes = row["interes"]
            pf.fecha_creacion = row["fecha_creacion"]
            # instancio un cliente
            cli = Cliente()
            #le asigno el dni que esta en la tabla plazos_fijos al dni del objeto cliente
            cli.dni = row["dni"]
            #ejecuto la funcion que me carga los datos del objeto Cliente que esta en la tabla clientes
            cli.buscar_cliente_base()
            # con el objeto cliente creado y cargado lo cargo en el plazo fijo 
            pf.cliente = cli
            # agrego el objeto plazo fijo al array de banco
            self.array_plazo_fijo.append(pf)
        conn.close()

    def cargar_caja_ahorro(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from cajas_ahorros"
        #ejecuto el sql y lo cargo en el df
        df = pd.read_sql_query(sql,conn)
        for row in df:
            ch = CajaDeAhorro()
            ch.nro_cuenta = row["nro_cuenta"]
            ch.monto =  row["monto"]
            cli = Cliente()
            #le asigno el dni que esta en la tabla plazos_fijos al dni del objeto cliente
            cli.dni = row["dni"]
            #ejecuto la funcion que me carga los datos del objeto Cliente que esta en la tabla clientes
            cli.buscar_cliente_base()
            # con el objeto cliente creado y cargado lo cargo en el plazo fijo 
            ch.cliente = cli
            # agrego el objeto plazo fijo al array de banco
            self.array_caja_ahorro.append(ch)
        conn.close()

    def cargar_empleados(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql= "select * from employees"
        #ejecuto el sql y lo cargo en el array de clientes
        self.array_cuentas = pd.read_sql_query(sql,conn)
        conn.close()

    #mostrar arrays
    def mostrar_clientes(self):
        return self.array_clientes

    def mostrar_cuentas(self):
        return self.array_cuentas

    def mostrar_empleados(self):
        return self.array_empleados
    #crear
    def crear_cliente (self):
        cliente = Cliente
        cliente.cargar_cliente()
        self.array_clientes.append(cliente)
        return cliente

    def crear_cuenta (self, Cliente, tipo_cuenta, monto):
        cliente = Cliente
        if(tipo_cuenta == 1): #1 = caja de ahorro
            cuenta_caja = CajaDeAhorro(cliente,monto)
            self.array_cuentas.append(cuenta_caja)
            return cuenta_caja
        else:
            interes = float(input("Ingrese interes: "))
            plazo = float(input("Ingrese plazo: "))
            cuenta_pf = PlazoFijo(cliente,monto,plazo,interes)
            self.array_cuentas.append(cuenta_pf)
            return cuenta_pf
    
    #Funcion buscar cliente en el array
    def buscar_cliente_array(self, textobuscar):
        encontrado = 0
        for cliente in self.array_clientes:
          # para buscar un cliente creamos el condicional y utilizamos las expresiones regulares
         if (re.findall(textobuscar, cliente.nombre)) or (re.findall(textobuscar, cliente.nombre)):
            self.mostrarcliente(cliente)
            encontrado = encontrado + 1
            self.submenubuscar(cliente.dni)
         if encontrado == 0:
             self.noencontrado()
    #Funcion buscar plazo fijo por nro de cuenta
    def buscar_array_plazo_fijo(self, nro_cuenta):
        for pf in self.array_plazo_fijo:
            if pf.nro_cuenta == nro_cuenta:
                return pf
    #Funcion buscar plazo fijo del cliente
    def buscar_pf_de_clientes(self):
        ch_clientes = []
        for cuenta in self.array_plazo_fijo:
            if cuenta.cliente.dni == self.cliente.dni:
                ch_clientes.append(cuenta)
        return ch_clientes
    #Funcion buscar CJ AHORRO por nro de cuenta
    def buscar_array_caja_ahorro(self, nro_cuenta):
        for ch in self.array_caja_ahorro:
            if ch.nro_cuenta == nro_cuenta:
                return ch
    #Funcion buscar CJ AHORRO del cliente
    def buscar_ch_de_clientes(self):
        pf_clientes = []
        for cuenta in self.array_caja_ahorro:
            if cuenta.cliente.dni == self.cliente.dni:
                pf_clientes.append(cuenta)
        return pf_clientes

    # Mostrar Cliente
    def mostrarcliente(self, Cliente):
        contacto = Cliente
        print()
        print("\u001B[32m          *********************************************")
        print("          *********************************************")
        print("\u001B[37m         DNI: {}".format(contacto.dni))
        print("                   Nombre: {}".format(contacto.nombre))
        print("                   Telefono: {}".format(contacto.telefono))
        print("                   Mail: {}".format(contacto.mail))
        print("\u001B[32m          *********************************************")
        print("          *********************************************")
        print("")

    def noencontrado(self):
        print("""
              
              """)
        print("""\u001B[31m 
                 *****************************
                 * LA BUSQUEDA NO DEVUELVE RESULTADOS!!! *
                 *****************************
                         """)
    def menu_index(self):
        hora_actual = now.strftime("%H:%M Hs")
        # menu principal con encabezado mostrando fecha y hora

        print("\u001B[32m  ***********************************************************")
        print("\u001B[32m  * ******************************************************* *")
        print("\u001B[32m  * *", "\u001B[36m            SISTEMA BANCARIO EN PYTHON", "\u001B[32m             * *")
        print("\u001B[32m  * *", "\u001B[37m  Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m   * *")
        print("\u001B[32m  * *                                                     * *")
        print("\u001B[32m  * *                   Menu Principal:                   * *")
        print("\u001B[32m  * *                                                     * *")
        print("\u001B[32m  * *", "              \u001B[33m 1 \u001B[37m- Clientes", "\u001B[32m                          * *")
        print("\u001B[32m  * *", "              \u001B[33m 2 \u001B[37m- Cuentas Bancarias", "\u001B[32m           * *")
        print("\u001B[32m  * *", "              \u001B[33m 2 \u001B[37m- Empleados", "\u001B[32m           * *")
        print("\u001B[32m  * *", "              \u001B[33m 0 \u001B[37m- Salir", "\u001B[32m                           * *")
        print("\u001B[32m  * *                                                     * *")
        print("\u001B[32m  * ******************************************************* *")
        print("\u001B[32m  ***********************************************************")
        menu_main = str(input())
        
        if menu_main == "1":
                menu_cliente(self)
        elif menu_main == "2":
            menu_cuentas = str(input("""\u001B[32m 
  ***********************************************************
  * ******************************************************* *
  * *                                                     * *
  * *  \u001B[37m   Cuentas Bancarias:\u001B[32m          * *
  * *  Para poder operar debera   seleccionar un cliente,* *
  * *       Ingrese el DNI del Ciente que desea operar:    * *
  * *  \u001B[33m 1 \u001B[37m- si quiere buscar por NOMBRE digite 1",
  * *                                                     * *
  * ******************************************************* *
  ***********************************************************

        """))
        if menu_cuentas == 1 :

    
        if 





    def ejecutar():
        agenda = Agenda()
#    try:  # comprobamos si el archivo .csv ya existe
#        with open("DB_banco.csv", "r") as archivo:
#            lector = csv.DictReader(archivo, delimiter=",")
#            for fila in lector:
#                agenda.insertar(fila["nombre"].capitalize(), fila["apellido"].capitalize(), fila["dni"], fila["domicilio"].capitalize(), fila["telefono"],fila["caja_ahorro"].upper(), fila["plazo_fijo"].upper())
#    except:
#        print("")
#        print("           Archivo .csv dañado o inexistente ٩(๏_๏)۶  ")  # si ya tenemos guardado algun contacto este
#        # aviso no sale mas
    while True:  # menu principal con encabezado mostrando fecha y hora

        print("\u001B[32m  ***********************************************************")
        print("\u001B[32m  * ******************************************************* *")
        print("\u001B[32m  * *", "\u001B[36m            SISTEMA BANCARIO EN PYTHON", "\u001B[32m             * *")
        print("\u001B[32m  * *", "\u001B[37m  Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m   * *")
        print("\u001B[32m  * *                                                     * *")
        print("\u001B[32m  * *                   Menu Principal:                   * *")
        print("\u001B[32m  * *                                                     * *")
        print("\u001B[32m  * *", "              \u001B[33m 1 \u001B[37m- Agenda", "\u001B[32m                          * *")
        print("\u001B[32m  * *", "              \u001B[33m 2 \u001B[37m- Operaciones Bancarias", "\u001B[32m           * *")
        print("\u001B[32m  * *", "              \u001B[33m 0 \u001B[37m- Salir", "\u001B[32m                           * *")
        print("\u001B[32m  * *                                                     * *")
        print("\u001B[32m  * ******************************************************* *")
        print("\u001B[32m  ***********************************************************")
        menu_main = str(input())
        if menu_main == "1":
            menu_agenda = str(input("""\u001B[32m 
            ***********************************************************
            * ******************************************************* *
            * *                                                     * *
            * *              \u001B[37m    Opciones de Agenda:\u001B[32m                * *
            * *                                                     * *
            * *       \u001B[33m 1\u001B[37m - Mostrar lista de contactos\u001B[32m               * *
            * *       \u001B[33m 2\u001B[37m - Buscar, Editar o Borrar un contacto\u001B[32m      * *
            * *       \u001B[33m 3\u001B[37m - Agregar contacto\u001B[32m                         * *
            * *       \u001B[33m 0\u001B[37m - Volver al Menu Principal\u001B[32m                 * *
            * *                                                     * *
            * ******************************************************* *
            ***********************************************************

                    """))
        if menu_agenda == "1":
                agenda.mostrartodos()
        elif menu_agenda == "2":
                texto = str(input("""\u001B[32m
  ***********************************************************
  *         \u001B[37mEscribe el texto a buscar en Contactos: \u001B[32m        *
  *                                                         *       
                            """))
                agenda.buscar(texto.capitalize())
                agenda.guardar()
        elif menu_agenda == "3":
                print("\u001B[32m  ***********************************************************")
                print("\u001B[32m  ***********************************************************")
                nombre = str(input("\u001B[37m     Ingrese el nombre: "))
                apellido = str(input("\u001B[37m     Ingrese el apellido: "))
                dni = str(input("\u001B[37m     Ingrese el D.N.I.: "))
                domicilio = str(input("\u001B[37m     Ingrese el domicilio: "))
                telefono = str(input("\u001B[37m     Ingrese el nro de teléfono: "))
                caja_ahorro = str(input("\u001B[37m     Posee Caja de Ahorro SI/NO: "))
                plazo_fijo = str(input("\u001B[37m     Posee un Plazo Fijo SI/NO: "))
                agenda.insertar(nombre.capitalize(), apellido.capitalize(), dni, domicilio.capitalize(), telefono, caja_ahorro.upper(), plazo_fijo.upper())
                agenda.guardar()
                print("\u001B[32m  ***********************************************************")
                print("\u001B[32m  ***********************************************************")
                print("""\u001B[34m
                     ******************************
                     *    Contacto guardado!!!    *
                     ******************************
                        """)
        elif menu_agenda == "0":
                print("""\u001B[35m
*************************************************************
*  Gracias por utilizar nuestro Software - Hasta pronto!!!  *
*************************************************************
                  """)
                agenda.guardar()
                break
            else:
                print("""
              
                        """)
                print(""""\u001B[31m 
                 *****************************
                 *    Opción incorrecta!!!   *
                 *****************************
                         """)
        elif menu_main == "2":
            menu_banco = str(input("""\u001B[32m 
  ***********************************************************
  * ******************************************************* *
  * *                                                     * *
  * *             \u001B[37m    Opciones Bancarias:\u001B[32m                 * *
  * *                                                     * *
  * *        \u001B[33m 1\u001B[37m - Operaciones con Cajas de Ahorro\u001B[32m         * *
  * *        \u001B[33m 2\u001B[37m - Operaciones con Plazos Fijos\u001B[32m            * *
  * *        \u001B[33m 3\u001B[37m - Total Depositos\u001B[32m                         * *
  * *        \u001B[33m 0\u001B[37m - Volver al Menu Principal\u001B[32m                * *
  * *                                                     * *
  * ******************************************************* *
  ***********************************************************

        """))
    # definimos fecha y hora creando funciones especificas con el formato de salida que nosotros queremos mostrar
def fecha_actual(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)
    return messsage

now = datetime.now()
hora_actual = now.strftime("%H:%M Hs")