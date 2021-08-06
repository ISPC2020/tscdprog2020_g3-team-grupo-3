# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:31:25 2021

@author: Escritorio
"""

"""
Created on Fri Jun 11 18:30:04 2021
Last update Fri Jul 2 19:38:05 2021
@author: Octavio / Eduardo
"""
from datetime import datetime
#importo la clase conexion para tener conexion a la base de datos
import conexion as con
import numpy as np
#importo pandas para poder ejecutar querys en la base
import pandas as pd
#Manejo los menus
import os
import time 
#import csv
#import itertools
#import re

if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
import pymysql
#conexion
con = con.Conexion()

def fecha_actual(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)
    return messsage

now = datetime.now()
hora_actual = now.strftime("%H:%M Hs")

class Cuenta:
    
    def __init__ (self, Cliente, monto):
        self.cliente = Cliente
        self.monto = monto
        self.nro_cuenta = 0 #

        '''date= datetime.now()
        #se crea el n° de cuenta automaticamente utilizando el dni del cliente + la fecha
        self.nro_cuenta = self.cliente.dni + date.year + date.month+date.hour+date.minute +date.second '''
        
    def imprimir(self):
        print("\u001B[32m                  * *********************************** *")
        print("                       Titular: ", self.cliente.nombre)
        print("                       Nro Cuenta: ", self.nro_cuenta)
        print("                       Saldo: ", self.monto)
        print("\u001B[32m                  * *********************************** *")

    def depositar(self, monto):   #metodo para sumar un deposito al monto del cliente
        self.monto = self.monto+monto
        # hago update de tabla
        monto = str(self.monto)
        nro_cuenta = str(self.nro_cuenta)
        sql= "UPDATE cajas_ahorros SET monto = "+monto+" where nro_cuenta = "+nro_cuenta+";"
        sql = str(sql)
        print(sql)
        #conecto a la base de datos
        conn = con.conectar()
        #defino un cursor
        cur = conn.cursor()
        #ejecuto el cursor con la query y devuelve a result
        result = cur.execute(sql)
        #meto commit
        conn.commit()
        # result = pd.read_sql_query(sql,conn)
        print(result)
        if result != True:
            print("error al actualizar cuenta registro: ", result)
        

    def extraer(self, monto):     #metodo para extraer y actualiza el valor de la cuenta del cliente
        self.monto = self.monto-monto
        #valido si el saldo a descontar no devuelve un valor negativo
        if (self.monto < 0):
            self.monto = self.monto + monto
            print("LA SOLICITUD NO SE PUEDE PROCESAR POR FALTA DE FONDOS. \n LA EXTRACCION NO PUEDE SUPERAR : ", self.monto)
        else:
            # PUEDE HACER LA EXTRACCION
            monto = str(self.monto)
            nro_cuenta = str(self.nro_cuenta)
            sql= "UPDATE cajas_ahorros SET monto = "+monto+" where nro_cuenta = "+nro_cuenta+";"
            sql = str(sql)
            print(sql)
            #conecto a la base de datos
            conn = con.conectar()
            #defino un cursor
            cur = conn.cursor()
            #ejecuto el cursor con la query y devuelve a result
            result = cur.execute(sql)
            #meto commit
            conn.commit()
            # result = pd.read_sql_query(sql,conn)
            print(result)
            if result != True:
                print("Error al actualizar cuenta registro: ", result)

    def mostrar_saldo(self):     #metodo para mostar el saldo de cada cliente, me sirve para luego sumar todos los montos y sacar el dinero que tiene el banco
        return self.monto

class PlazoFijo(Cuenta):
    
    def __init__(self):   #plazo fijo ademas de los atributos titular y monto tiene un plazo e interes de ese plazo
        super().__init__(Cliente,0)
        self.nro_cuenta = 0
        self.plazo = 0   #inicializo el atributo plazo y le copio lo que llega en el parámetro
        self.monto = 0   #inicializo el atributo interes y le copio lo que llega en el parámetro
        self.interes = 0
        self.fecha_creacion = ''

    def crear_plazo__fijo(self, Cliente, monto, plazo, interes ):
          super().__init__(Cliente,monto)
          date= datetime.now()
          self.nro_cuenta = self.cliente.dni + date.year + date.month+date.hour+date.minute +date.second
          self.plazo = plazo   #inicializo el atributo plazo y le copio lo que llega en el parámetro
          self.monto = monto    #inicializo el atributo interes y le copio lo que llega en el parámetro
          self.interes = interes
          self.fecha_creacion = datetime.now()
          nro_cuenta = str(self.nro_cuenta)
          dni = str(Cliente.dni)
          monto = str(self.monto)
          fecha = str(self.fecha_creacion )
  
  
          sql= "insert into plazos_fijos values ("+nro_cuenta+","+dni+","+ monto +","+ interes +",'"+fecha+"');"
          sql = str(sql)
          #conecto a la base de datos
          conn = con.conectar()
          #defino un cursor
          cur = conn.cursor()
          #ejecuto el cursor con la query y devuelve a result
          result = cur.execute(sql)
          #meto commit
          conn.commit()
          # result = pd.read_sql_query(sql,conn)
          print(result)
          if result != True:
              print("\u001B[31m  ***********************************************************")
              print("       ERROR AL INSERTAR REGISTRO: ", result)
              print("\u001B[31m  ***********************************************************")
              time.sleep(1.5)
          
    def imprimir_pf(self):
        print("\u001B[32m               ********************************************")
        print("\u001B[32m               * **************************************** *")
        print("                          Cuenta de Plazo Fijo: ")
        super().imprimir()
        print("                       Plazo en días: ", self.plazo)
        print("                       Intereses: ", self.interes)
        print("                       Ganancia: ", self.ganancia())
        print("\u001B[32m               * **************************************** *")
        print("\u001B[32m               ********************************************")
          
    def ganancia(self):
        ganancia = self.monto*self.interes/100
        return ganancia

class CajaDeAhorro(Cuenta):   #clase CDA hereda la clase cuenta
     #lo hereda de la clase cuenta, lo llamo
    def __repr__(self):
        return str(self.__dict__)
        
    def mostrar_saldo(self):
        print("Cuenta Caja de Ahorro: ")
        super().imprimir()    #llamo al imprimir de la clase padre
        
    def crear_caja_ahorro(self, Cliente, monto):
        #error no se como instanciarlo
        super().__init__(Cliente, monto)
        date= datetime.now()
        nro_cuenta =str( self.cliente.dni + date.year + date.month+date.hour+date.minute +date.second)
        dni = str(Cliente.dni)
        monto = str(self.monto)
        sql= "insert into cajas_ahorros (nro_cuenta, dni,monto) values ("+nro_cuenta+",'"+ dni +"',"+monto+");"
        sql = str(sql)
        print(sql)
        #conecto a la base de datos
        conn = con.conectar()
        #defino un cursor
        cur = conn.cursor()
        #ejecuto el cursor con la query y devuelve a result
        result = cur.execute(sql)
        #meto commit
        conn.commit()
        # result = pd.read_sql_query(sql,conn)
        print(result)
        if result != True:
            print("\u001B[31m       * ********************************************************* *")
            print("            ERROR AL INSERTAR REGISTRO: ", result)
            print("\u001B[31m       * ********************************************************* *")
            time.sleep(1.5)
        
        super().imprimir() 
       
        #print("no se como instanciar el constructor de la clase heredada")


# creamos la clase Cliente
class Cliente:

    def __init__(self):
        self.nombre = ""
        self.dni = ""
        self.telefono = 0
        self.mail = ""
    
    def __repr__(self):
        return str(self.__dict__)
    
    def cargar_cliente(self):
        print("")
        print("")
        print("\u001B[32m              * ******************************************** *")
        self.nombre = input("                     Nombre: " )
        self.dni = int(input("                     DNI: "))
        self.telefono = int(input("                     Teléfono: "))
        self.mail = input("                     eMail: " )
        print("\u001B[32m              * ******************************************** *")
        time.sleep(1.5)
        dni = str(self.dni)
        telefono = str(self.telefono)
        
        sql= "insert into clientes values ("+dni+",'"+self.nombre+"',"+ telefono +",'"+self.mail+"');"
        sql = str(sql)
        #conecto a la base de datos
        conn = con.conectar()
        #defino un cursor
        cur = conn.cursor()
        #ejecuto el cursor con la query y devuelve a result
        result = cur.execute(sql)
        #meto commit
        conn.commit()
        # result = pd.read_sql_query(sql,conn)
        print(result)
        if result != True:
            print("\u001B[31m       * ********************************************************* *")
            print("            ERROR AL INSERTAR REGISTRO: ", result)
            print("\u001B[31m       * ********************************************************* *")
            time.sleep(1.5)

    def buscar_cliente_base(self):
        #conecto a la base de datos
        conn = con.conectar()
        dni = str(self.dni)
        #creo el sql
        sql= "select * from clientes where dni = " + dni +";"
        #print(sql)
        df = pd.read_sql_query(sql,conn)
        #print(result)
        for c in df.index:
            self.nombre = df["nombre"][c]
            self.dni = df["dni"][c]
            self.telefono = df["telefono"][c]
            self.mail = df["mail"][c]
        return self
    
    def mostrar_cliente(self):
        print("\u001B[32m                    * ************ CLIENTE: ************ *")
        print("\u001B[32m                         Nombre: ", self.nombre)
        print("\u001B[32m                         DNI: ", self.dni)
        print("\u001B[32m                         Teléfono: ", self.telefono)
        print("\u001B[32m                         eMail: ", self.mail)
        print("\u001B[32m                    * ********************************** *")

    def modificar_cliente(self):
        # cuando elegimos modificar, modificamos los atributos del objeto
                print("\u001B[32m               * **************************************** *")
                self.nombre = str(input("\u001B[37m                      Ingrese el nombre: "))
               # self.dni = str(input("\u001B[37m                 Ingrese el dni: "))
                self.telefono = str(input("\u001B[37m                      Ingrese el teléfono: "))
                self.mail = str(input("\u001B[37m                      Ingrese el eMail: "))
                print("\u001B[32m               * **************************************** *")
                time.sleep(1)
               # sql = "update clientes set nombre = '" + self.nombre + "', telefono = " + self.telefono + ", mail = '" + self.mail + " where dni = " + self.dni + ";"

class Banco:
    # funcion cargar clientes
    # funcion cargar cuentas
    # funcion crear cliente
    # funcion crear cuenta
    # funcionar cliente en array
    # funcionar cuenta en array
    # funcionar empleado en array
    def __init__(self):
        self.array_clientes = []  #array de objetos
        self.array_plazo_fijo = []        #array de objetos
        self.array_caja_ahorro = []   #array de objetos
        self.array_empleados = []     #array de objetos
        
        self.cliente = Cliente()    #objeto individual inicializado en un objeto vacio
        self.plazo_fijo = PlazoFijo() #objeto individual inicializado en un objeto vacio
        self.caja_ahorro = CajaDeAhorro(self.cliente,0) #objeto individual inicializado en un objeto vacio
       # self.con = Conexion()

    # Carga de arrays
    def cargar_clientes(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql = "select * from clientes"
        #ejecuto el sql y lo cargo en el array de clientes
        df = pd.read_sql_query(sql, conn)
        print(df)
        for i in df.index:
            cli = Cliente()
            cli.dni = df["dni"][i]
            cli.nombre = df["nombre"][i]
            cli.telefono = df["telefono"][i]
            cli.mail = df["mail"][i]

            self.array_clientes.append(cli)  
          
       
        conn.close()
        self.cliente = Cliente() #clear #none
        #self.cliente.mostrar_cliente()

    def exit(self):
        print("""\u001B[35m
        *************************************************************
        *  Gracias por utilizar nuestro Software - Hasta pronto!!!  *
        *************************************************************
                  """)
        time.sleep(2)
        exit()

    # Metodos pora ordenar el array
    def ordenarxnombre(self):
        # Doc = https://docs.python.org/es/3/howto/sorting.html
        self.array_clientes.sort(key=lambda cliente: cliente.nombre)

    def ordenarxdni(self):
        self.array_clientes.sort(key=lambda cliente: cliente.dni)
    
    def cargar_plazo_fijo(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql = "select * from plazos_fijos"
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
        sql = "select * from cajas_ahorros"
        #ejecuto el sql y lo cargo en el df
        df = pd.read_sql_query(sql,conn)
        #print(df)
        for i in df.index:
               #instancio cliente
            cli = Cliente()
            #le asigno el dni del df al artributo del objeto cliente
            cli.dni = df["dni"][i]
            #ejecuto la funcion del cliente (ver funcion en la clase cliente)
            cli.buscar_cliente_base()
            # capturo el monto que esta en la base de datos para luego instanciar el objeto CH
            monto = df["monto"][i]
            nro_cuenta = df["nro_cuenta"][i]
            #intancio el objeto CH
            ch = CajaDeAhorro(cli,monto)
            # le asigno el numero de cuenta de la CH existente
            ch.nro_cuenta = df["nro_cuenta"][i]
            self.array_caja_ahorro.append(ch)
        conn.close()

    def cargar_empleados(self):
        #conecto a la base de datos
        conn = con.conectar()
        #creo el sql
        sql = "select * from employees"
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
            cuenta_pf = PlazoFijo(cliente, monto, plazo, interes)
            self.array_cuentas.append(cuenta_pf)
            return cuenta_pf
       # Funcion buscar cliente en el array
    def buscar_cliente_array(self, textobuscar):
        encontrado = 0
        for cliente in self.array_clientes:
            # para buscar un cliente creamos el condicional y utilizamos las expresiones regulares
              #print(cliente)
              if cliente.dni == textobuscar:
                                  
                self.cliente.nombre = cliente.nombre
                self.cliente.dni = cliente.dni
                self.cliente.telefono = cliente.telefono
                self.cliente.mail = cliente.mail
                self.cliente.mostrar_cliente()
                encontrado = encontrado + 1
                
                print("\u001B[34m                 * ******** CLIENTE ENCONTRADO: ********* *")
                self.cliente.mostrar_cliente()
                break
        return encontrado

    # Funcion buscar plazo fijo por nro de cuenta
    def buscar_array_plazo_fijo(self, nro_cuenta):
        encontrado = 0
        for pf in self.array_plazo_fijo:
            if pf.nro_cuenta == nro_cuenta:
                self.plazo_fijo.cliente = pf.cliente
                self.plazo_fijo.monto = pf.monto
                self.plazo_fijo.nro_cuenta = pf.nro_cuenta
                encontrado = encontrado + 1

                print("\u001B[34m             * ********** PLAZO FIJO ENCONTRADO: ********** *")
                self.plazo_fijo.imprimir()
                time.sleep(1.5)
                break
        return encontrado

    # Funcion buscar plazo fijo del cliente
    def buscar_ch_de_clientes(self):
        ch_clientes = []
        for cuenta in self.array_caja_ahorro:
            if cuenta.cliente.dni == self.cliente.dni:
                ch_clientes.append(cuenta)
        return ch_clientes
    
    # Funcion buscar CJ AHORRO por nro de cuenta
    def buscar_array_caja_ahorro(self, nro_cuenta):
        encontrado = 0
        for ch in self.array_caja_ahorro:
            if ch.nro_cuenta == nro_cuenta:
                self.caja_ahorro.cliente = ch.cliente
                self.caja_ahorro.monto = ch.monto
                self.caja_ahorro.nro_cuenta = ch.nro_cuenta
                encontrado = encontrado + 1
                
                print("\u001B[34m             * ******** CAJA DE AHORRO ENCONTRADA: ******** *")
                self.caja_ahorro.imprimir()
                break
        return encontrado
                

    # Funcion buscar CJ AHORRO del cliente
    def buscar_pf_de_clientes(self):
        pf_clientes = []
        for cuenta in self.array_caja_ahorro:
            if cuenta.cliente.dni == self.cliente.dni:
                pf_clientes.append(cuenta)
        return pf_clientes

    # Mostrar Cliente
    def mostrarcliente(self):
        contacto = self.cliente
        print()
        print("\u001B[32m               *********************************************")
        print("               * ***************************************** *")
        print("\u001B[37m              DNI: {}".format(contacto.dni))
        print("                        Nombre: {}".format(contacto.nombre))
        print("                        Telefono: {}".format(contacto.telefono))
        print("                        Mail: {}".format(contacto.mail))
        print("\u001B[32m               * ***************************************** *")
        print("               *********************************************")
        print("")

    def noencontrado(self):
        print("""
              
                """)
        print("""\u001B[31m 
                         *****************************************
                         * LA BUSQUEDA NO DEVUELVE RESULTADOS!!! *
                         *****************************************
                """)
        time.sleep(1.5)

        # menu principal con encabezado mostrando fecha y hora
    def menu_index(
            self):
        print("\u001B[32m  ***********************************************************************")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  * *", "\u001B[36m                   SISTEMA BANCARIO EN PYTHON", "\u001B[32m                  * *")
        print("\u001B[32m  * *", "\u001B[37m        Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m         * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *                          Menu Principal:                        * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *", "                      \u001B[33m 1 \u001B[37m- Clientes", "\u001B[32m                            * *")
        print("\u001B[32m  * *", "                      \u001B[33m 2 \u001B[37m- Cuentas Bancarias", "\u001B[32m                   * *")
        print("\u001B[32m  * *", "                      \u001B[33m 3 \u001B[37m- Empleados", "\u001B[32m                           * *")
        print("\u001B[32m  * *", "                      \u001B[33m 0 \u001B[37m- Salir", "\u001B[32m                               * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  ***********************************************************************")
        menu_main = str(input("                             Ingresar opcion: "))
        
        if menu_main == "1":
            self.menu_cliente()
        elif menu_main == "2":
            self.cargar_clientes()
            # print(self.array_clientes)
            print("")
            print("\u001B[32m               * ***************************************** *")
            buscar = int(input("\u001B[37m                   Ingresar DNI del cliente: "))
            result = self.buscar_cliente_array(buscar)
            #print(result)
            if result == 0:
                print("")
                print("\u001B[31m                * ******** CLIENTE NO ENCONTRADO! ******** *")
                print("")
                time.sleep(1.5)
                self.menu_cliente()
            elif result == 1:
                self.menu_cuentas()
        elif menu_main == "3":
            print("Este modulo esta en desarrollo")
            time.sleep(1.5)
            self.menu_index()
        elif menu_main == "0":
            self.exit()
        else:
            print("")
            print("\u001B[31m      * ******** OPCION INCORRECTA - INTENTE NUEVAMENTE! ******** *")
            print("")
            time.sleep(1.5)
            self.menu_index()



    def menu_cliente(self):
        now = datetime.now()
        hora_actual = now.strftime("%H:%M Hs")
        print("\u001B[32m  ***********************************************************************")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  * *", "\u001B[36m                   SISTEMA BANCARIO EN PYTHON", "\u001B[32m                  * *")
        print("\u001B[32m  * *", "\u001B[37m        Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m         * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *                          Menu Clientes:                         * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *", "                      \u001B[33m 1 \u001B[37m- Crear Cliente", "\u001B[32m                       * *")
        print("\u001B[32m  * *", "                      \u001B[33m 2 \u001B[37m- Buscar Cliente", "\u001B[32m                      * *")
        print("\u001B[32m  * *", "                      \u001B[33m 3 \u001B[37m- Editar Cliente", "\u001B[32m                      * *")
        print("\u001B[32m  * *", "                      \u001B[33m 4 \u001B[37m- Volver al Menu Principal", "\u001B[32m            * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  ***********************************************************************")
        opcion = str(input("                             Ingresar opción: "))
        if opcion == "1":
            self.cliente.cargar_cliente()
            print("""\u001B[34m
                       *******************************
                       *  Nuevo cliente guardado!!!  *
                       *******************************
                     """)
            time.sleep(0.5)
            self.cliente.mostrar_cliente()
            self.menu_cliente()
        elif opcion == "2":
            self.cargar_clientes()
            # print(self.array_clientes)
            print("")
            print("\u001B[32m               * ***************************************** *")
            buscar = int(input("\u001B[37m                   Escriba el DNI del cliente: "))
            result = self.buscar_cliente_array(buscar)
            #print(result)
            if result == 0:
                print("")
                print("\u001B[31m                * ******** CLIENTE NO ENCONTRADO! ******** *")
                print("")
                time.sleep(1.5)
                self.menu_cliente()
            elif result == 1:
                #self.cliente.mostrar_cliente()
                self.menu_cuentas()
        elif opcion == "3":
            print("")
        elif opcion == "4":
            self.menu_index()

    def menu_cuentas(self):
        print("\u001B[32m  ***********************************************************************")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  * *", "\u001B[36m                   SISTEMA BANCARIO EN PYTHON", "\u001B[32m                  * *")
        print("\u001B[32m  * *", "\u001B[37m        Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m         * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *                          Menu Cuentas:                          * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *", "                   \u001B[33m 1 \u001B[37m- Caja de Ahorro", "\u001B[32m                         * *")
        print("\u001B[32m  * *", "                   \u001B[33m 2 \u001B[37m- Plazo Fijo", "\u001B[32m                             * *")
        print("\u001B[32m  * *", "                   \u001B[33m 3 \u001B[37m- Volver al Menu Clientes", "\u001B[32m                * *")
        print("\u001B[32m  * *", "                   \u001B[33m 4 \u001B[37m- Volver al Menu Principal", "\u001B[32m               * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  ***********************************************************************")
        opcion = str(input("                             Ingresar opción: "))
        if opcion == "1":
            self.menu_caja_ahorro()
        elif opcion == "2":
            self.menu_plazo_fijo()
        elif opcion == "3":
            self.menu_cliente()
        elif opcion == "4":
            self.menu_index()
        else:
            self.menu_cuentas()

    def menu_caja_ahorro (self):
        self.buscar_ch_de_clientes()
        print("\u001B[32m  ***********************************************************************")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  * *", "\u001B[36m                   SISTEMA BANCARIO EN PYTHON", "\u001B[32m                  * *")
        print("\u001B[32m  * *", "\u001B[37m        Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m         * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *                       Menu Caja de Ahorro:                      * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *", "                  \u001B[33m 1 \u001B[37m- Crear una Caja de Ahorro", "\u001B[32m                * *")
        print("\u001B[32m  * *", "                  \u001B[33m 2 \u001B[37m- Ver Cajas de Ahorro", "\u001B[32m                     * *")
        print("\u001B[32m  * *", "                  \u001B[33m 3 \u001B[37m- Operar una Caja de Ahorro", "\u001B[32m               * *")
        print("\u001B[32m  * *", "                  \u001B[33m 4 \u001B[37m- Volver al Menu Cuentas", "\u001B[32m                  * *")
        print("\u001B[32m  * *", "                  \u001B[33m 5 \u001B[37m- Volver al Menu Principal", "\u001B[32m                * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  ***********************************************************************")
        self.cargar_caja_ahorro()
        #print(self.cargar_caja_ahorro())
        opcion = str(input("                             Ingresar opción: "))

        if opcion == "1":
            monto = float(input("                 Ingrese el saldo inicial: "))
            self.caja_ahorro.crear_caja_ahorro(self.cliente, monto)
            #self.caja_ahorro = caja_ahorro
            self.menu_caja_ahorro()
        elif opcion == "2":
            print(self.buscar_ch_de_clientes())
            ch2 =  int(input("              Ingrese el número de la caja de ahorro: "))
            result = self.buscar_array_caja_ahorro(ch2);
            if result == 0:    
                print("")
                print("\u001B[31m            * ******** CAJA DE AHORRO NO ENCONTRADA: ******** *")
                print("")
                time.sleep(1.5)
                self.menu_caja_ahorro()
            elif result == 1:
                print("")
                print("\u001B[34m                   * ******** YA PUEDE OPERAR ******** *")
                print("")
                self.menu_caja_ahorro()
        elif opcion == "3":
            print(self.buscar_ch_de_clientes())
            ch2 = int(input("Ingrese el número de la caja de ahorro en la que quiere operar: "))
            result = self.buscar_array_caja_ahorro(ch2);
            if result == 0:    
                print("")
                print("\u001B[31m            * ******** CAJA DE AHORRO NO ENCONTRADA: ******** *")
                print("")
                time.sleep(1.5)
                self.menu_caja_ahorro()
            elif result == 1:
                print("")
                print("\u001B[34m                   * ******** YA PUEDE OPERAR ******** *")
                print("")

                self.buscar_ch_de_clientes()
                print("\u001B[32m  ***********************************************************************")
                print("\u001B[32m  * ******************************************************************* *")
                print("\u001B[32m  * *", "\u001B[36m                   SISTEMA BANCARIO EN PYTHON", "\u001B[32m                  * *")
                print("\u001B[32m  * *", "\u001B[37m        Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m         * *")
                print("\u001B[32m  * *                                                                 * *")
                print("\u001B[32m  * *                     Opciones Caja de Ahorro:                    * *")
                print("\u001B[32m  * *                                                                 * *")
                print("\u001B[32m  * *", "                  \u001B[33m 1\u001B[37m - Depositar\u001B[32m                                * *")
                print("\u001B[32m  * *", "                  \u001B[33m 2\u001B[37m - Extraer\u001B[32m                                  * *")
                print("\u001B[32m  * *", "                  \u001B[33m 3\u001B[37m - Saldo Total\u001B[32m                              * *")
                print("\u001B[32m  * *", "                  \u001B[33m 4\u001B[37m - Volver al Menu Cuentas", "\u001B[32m                  * *")
                print("\u001B[32m  * *", "                  \u001B[33m 5\u001B[37m - Volver al Menu Principal", "\u001B[32m                * *")
                print("\u001B[32m  * *                                                                 * *")
                print("\u001B[32m  * ******************************************************************* *")
                print("\u001B[32m  ***********************************************************************")
                self.cargar_caja_ahorro()
                #print(self.cargar_caja_ahorro())
                menu_ch = str(input("                             Ingresar opción: "))
                if menu_ch == "1":
                     monto = float(input("          Ingrese el monto a Depositar: "))
                     self.caja_ahorro.depositar(monto)
                     self.caja_ahorro.mostrar_saldo()
                     self.menu_caja_ahorro()
                elif menu_ch == "2":
                     monto = float(input("          Ingrese el monto a Extraer: "))
                     self.caja_ahorro.extraer(monto)
                     self.caja_ahorro.mostrar_saldo()
                     self.menu_caja_ahorro()
                elif menu_ch == "3":
                     self.caja_ahorro.mostrar_saldo()
                     self.menu_caja_ahorro()
                elif menu_ch == "4":
                     self.menu_cuentas()
                elif menu_ch == "5" :
                     self.menu_index()
        elif opcion == "4":
                self.menu_cuentas()
        elif opcion == "5" :
                self.menu_index()

    def menu_plazo_fijo (self):
        self.buscar_pf_de_clientes()
        print("\u001B[32m  ***********************************************************************")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  * *", "\u001B[36m                   SISTEMA BANCARIO EN PYTHON", "\u001B[32m                  * *")
        print("\u001B[32m  * *", "\u001B[37m        Hoy es", fecha_actual(now), "\u001B[37my son las", hora_actual, "\u001B[32m         * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *                         Menu Plazo Fijo:                        * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * *", "                  \u001B[33m 1 \u001B[37m- Crear Plazo Fijo", "\u001B[32m                        * *")
        print("\u001B[32m  * *", "                  \u001B[33m 2 \u001B[37m- Ver Plazo Fijo", "\u001B[32m                          * *")
        print("\u001B[32m  * *", "                  \u001B[33m 3 \u001B[37m- Volver al Menu Cuentas", "\u001B[32m                  * *")
        print("\u001B[32m  * *", "                  \u001B[33m 4 \u001B[37m- Volver al Menu Principal", "\u001B[32m                * *")
        print("\u001B[32m  * *                                                                 * *")
        print("\u001B[32m  * ******************************************************************* *")
        print("\u001B[32m  ***********************************************************************")
        #self.cargar_plazo_fijo

        opcion = str(input("                       Ingresar opcion: "))
        if opcion == "1":
            monto = int(input("                  Ingrese el MONTO del plazo fijo: "))
            plazo = int(input("                  Ingrese la CANT. DIAS del plazo fijo: "))
            interes = int(input("                  Ingrese el INTERES ANUAL del plazo fijo: "))
            plazo_fijo = self.crear_plazo__fijo(self, Cliente, monto, plazo, interes)
            self.PlazoFijo.imprimir_pf()
            time.sleep(1.5)
            self.plazo_fijo = plazo_fijo
            self.menu_cuentas()

        elif opcion == "2":
            print(self.buscar_pf_de_clientes())
            ch2 =  int(input("              Ingrese el número del Plazo Fijo: "))
            result = self.buscar_array_plazo_fijo(ch2);
            if result == 0:
                print("")
                print("\u001B[31m              * ******** PLAZO FIJO NO ENCONTRADO: ******** *")
                print("")
                time.sleep(1.5)
                self.menu_plazo_fijo()
            elif result == 1:
                print("")
                print("\u001B[34m                   * ******** YA PUEDE OPERAR ******** *")
                print("")
                self.menu_plazo_fijo()
#
        elif opcion == "3":
                self.menu_cuentas()
        elif opcion == "4":
                self.menu_index()
b = Banco()
b.menu_index()
