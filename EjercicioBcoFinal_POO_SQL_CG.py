# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:45:40 2021

@author: CarinaGiovine
"""


import pymysql

class Cliente:  #defino la clase Cliente que me permite agregar, buscar, mostrar y eliminar a clientes.
    
    def __init__(self,cliente):  #constructor. con este método inicializo al objeto cliente
        self.cliente=cliente
        
    def menu_op(self):
        
        opcion=0
        print("Menú de opciones: ")
        print(" 1- Agregar un nuevo cliente.")
        print(" 2- Buscar un cliente. ")
        print(" 3- Modificar/Actulizar datos de un cliente. ")
        print(" 4- Eliminar un cliente.")
        opcion=int(input("Ingresa la opción deseada: "))
        if opcion==1:
            self.agregar_cliente()
        elif opcion==2:
            self.buscar_cliente()
        elif opcion==3:
            self.modificar_cliente()
        elif opcion==4:
            self.eliminar_cliente()
        else:
            op=int(input("Ingreso una opción no válida. Si desea volver al menú ingrese 1 / 0 para terminar."))
            if op==1:
                self.menu_op()
            elif op==0:
                print("Gracias por visitar nuestro Banco")
            else:
                print("Ingreso opción no válida.")
                
        
    def agregar_cliente(self):  #método para agregar un cliente nuevo al dict
        print(".·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨.·.¨")
        print("Ingrese los datos para dar de alta a un nuevo cliente.")
        nro_DNI=int(input("Ingresa el número de DNI del nuevo cliente: "))
        if nro_DNI not in self.cliente:
            nombre=input("Ingresa el nombre y apellido del cliente: ")
            mail=input("Ingresa el correo electrónico: ")
            tipo_cta=input("Ingresa CA para cuenta Caja de Ahorro o PF para cuenta Plazo Fijo: ")
            monto=float(input("Ingresa el monto inicial: "))
            self.cliente[nro_DNI]=[nombre.capitalize(),mail,tipo_cta.upper(),monto]
        else:
            print("El cliente ya existe.")
     
   
    def buscar_cliente(self):  #método para buscar un cliente cuyo DNi lo ingreso por consola
        nro_DNI=int(input("Ingresa el DNI del cliente a consultar: "))
        if nro_DNI in self.cliente:
            print("El cliente existe.")
            print("Nro de DNI: ",nro_DNI,"  Nombre:",self.cliente[nro_DNI][0],"  Mail:",self.cliente[nro_DNI][1],"  Tipo de Cuenta Bria:",self.cliente[nro_DNI][2],"  Monto:",self.cliente[nro_DNI][3])
            return nro_DNI
        else:
            print("No existe cliente")
        
            
    def mostrar_clientes(self): #método mostrar clientes que lista todos los clientes almacenados
        for DNI in self.cliente:  
           
           print(DNI,"Nombre: ",self.cliente[DNI][0],"  E-mail: ",self.cliente[DNI][1],"  Tipo de Cuenta: ",self.cliente[DNI][2], "  Monto: $ ",self.cliente[DNI][3])

        return self.cliente
    
    def modificar_cliente(self): # método para modificar el mail del cliente
        print("Modificar mail de un Cliente")
        nro_DNI=int(input("Ingresa el nro de DNI del cliente para actualizar sus datos: "))
        if nro_DNI in self.cliente:
            mail=input("Ingresa el nuevo E-mail: ")
            self.cliente[nro_DNI][1]=mail
            print("Los datos del cliente se han actualizados.")
            print("Nro DNI: ",nro_DNI,"  Nombre:",self.cliente[nro_DNI][0],"   E-mail: ",self.cliente[nro_DNI][1])
        else:
            print("No existe cliente.")
    
    
    def eliminar_cliente(self):  #creo el método para eliminar un cliente ingresando su nro de DNI
         nro_DNI=int(input ("Ingresa el número de DNI del Cliente que deseas eliminar:  "))
         
         if nro_DNI in self.cliente:  #verifico si el DNI existe y en caso positivo elimina el registro
            del self.cliente[nro_DNI]
            print("Se elimino con éxito el Cliente de la Base de Datos")
         else:
            print("El Cliente no existe en la Base de Datos.")

           


class Conexion:   #clase conexion - usada en este caso en la clase empleado para conectar a la Base de datos Employees
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = ''
        self.db = 'employees'

    def conectar(self):
        try:
            conexion = pymysql.connect(host=self.host,
                                       user=self.user,
                                       password=self.password,
                                       db=self.db)
            #print("Conexion exitosa")
            return conexion   

        except (pymysql.err.OperationalError, pymysql.err.InternalError) as error:
            print("Ocurrió un error al conectar: ", error)


class Empleado():  #clase para agregar, consultar, modificar o eliminar un empleado de la BD
    
    def __init__(self):
        
        self.conn=Conexion()
    
        
    def menu(self):        
       opcion=0
       print("Menú de opciones: ")
       print(" 1- Agregar un nuevo Empleado.")
       print(" 2- Buscar un Empleado. ")
       print(" 3- Modificar/Actulizar datos de un empleado. ")
       print(" 4- Eliminar un empleado.")
       print(" 5- Salir")
       opcion=int(input("Ingresa la opción deseada: "))
       if opcion==1:
           self.agregar_empleado()
       elif opcion==2:
           self.buscar_empleado()
       elif opcion==3:
           self.modificar_empleado()
       elif opcion==4:
           self.eliminar_empleado()
       else:
           print("Gracias.")
   
        
    def agregar_empleado(self):
        
        conn=self.conn.conectar()
        cursor = conn.cursor()
        nro_em=int(input("Ingresa el número del nuevo empleado: "))
        b_day=input("Ingresa la fecha de nacimiento formato aaaa/mm/dd: ")
        nombre=input("Ingrese en nombre: ")
        apellido=input("Ingrese el apellido: ")
        genero=input("Ingrese el genero M / F: ")
        f_alta=input("Ingrese la fecha de ingreso a la empresa, formato aaaa/mm/dd: ")
        sqlinsertar=" INSERT INTO `employees` (emp_no, birth_date,first_name, last_name,gender, hire_date) VALUES (%s,%s, %s, %s, %s, %s ) "
        datos=(nro_em,b_day,nombre,apellido,genero,f_alta)
        cursor.execute(sqlinsertar,datos)
        conn.commit()   # con commit se guardan los valores en la tabla
        sqlcon= " SELECT emp_no, first_name FROM `employees` WHERE  last_name=%s   "   #hago una consulta para ver si se agrego el valor que agregue en el insert
        cursor.execute(sqlcon,apellido)
        resul=cursor.fetchall()
        conn.close()
        for i in resul:
            print(i)
        
            
    def buscar_empleado(self):
        conn=self.conn.conectar()
        cursor = conn.cursor()
        nro_em=int(input("Ingrese el nro de empleado que desea consultar: "))
        sql= "SELECT * FROM `employees` WHERE emp_no=%s " 
        cursor.execute(sql,nro_em)
        resultado=cursor.fetchall()
        conn.close()
        print(resultado)   #me muestra todos los resultados de mi consulta
        
        
    def modificar_empleado(self):
        conn=self.conn.conectar()
        cursor = conn.cursor()
        nro_em=int(input("Ingrese el nro de empleado que desea modificar: "))
        gen=input("Ingrese el género actual: ")        
        sqlupd=" UPDATE `employees` SET gender=%s WHERE emp_no=%s "   #actualizo un dato del registro de empleado nro 10005
        d=(gen, nro_em)
        cursor.execute(sqlupd, d)
        conn.commit()
        sqlcons=" SELECT * FROM `employees` WHERE emp_no=%s"   # hago una consulta para verificar si se actualizo el registro
        cursor.execute(sqlcons,nro_em)
        resu=cursor.fetchone()
        conn.close()
        print(resu)
        
        
    def eliminar_empleado(self):
        conn=self.conn.conectar()
        cursor = conn.cursor()
        nro_em=int(input("Ingrese el nro de empleado que desea eliminar: "))
        sqleli=" DELETE  FROM `employees` WHERE emp_no= %s"    #elimino de la BD el registro cuyo emp_no=5
        cursor.execute(sqleli, nro_em)
        conn.commit()
        cons_ver= "SELECT * FROM `employees` WHERE emp_no= %s"
        cursor.execute(cons_ver, nro_em)   #consulto la base para ver si aun está el registro que elimine en el query de arriba
        re=cursor.fetchone()
        conn.close()
        print(re)
            


class Banco():    #clase Banco, creo objetos de las otras clases y opero con el Banco.
    
    def __init__(self):
        pass
    
    def menu_bco(self):
        opcion=0
        print("BIENVENIDO")
        print("Ingrese la opción válida para trabajar.")
        print(" 1 -Clientes")
        print(" 2 -Operar / Transacciones con cuentas.")
        print(" 3 -Empleados")
        print(" 4 -Salir")
        
        opcion=int(input("Ingresa la opción deseada: "))
        if opcion==1:
            c=Cliente(cliente)
            c.menu_op()
            otravez=int(input("Quieres realizar otra operación? Ingresa 1 para SI / 2 para NO: "))
            if otravez==1:
                self.menu_bco()
            else:
                print("Gracias")
       
        elif opcion==2:
            def operar():
                ganancia=0.8 
                dni=int(input("Ingrese el número del DNI para realizar la operación Bancaria: "))   #agregar que si no esta el cliente, dar la opcion de agregarlo
                #for dni in cliente:
                if dni in cliente:    
                    operacion=int(input("Ingrese la operación Bancaria: 1 -Depósito en CA / 2- Deposito en PF por 30 días/ 3  -Extracción : "))
            
                    if operacion ==1:
                        if cliente[dni][2]=="CA":
                            mon=float(input("Ingrese el monto correspondientea depositar en su Caja de Ahorro: "))
                            cliente[dni][3]=cliente[dni][3] + mon
                            print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
                        else:
                            print("El cliente no posee Caja de Ahorro y no puede operar sin una.") 
                    elif operacion==2:
                        if cliente[dni][2]=="PF":
                            mon=float(input("Ingrese el monto correspondientea depositar en Plazo Fijo por 30 días: "))
                            cliente[dni][3]=cliente[dni][3] + mon +(mon * ganancia)
                            print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
                        else:
                            print("El cliente no tiene una cuenta Plazo Fijo y no puede eoprar sin una.")
                    elif operacion==3:
                        mon=float(input("Ingrese el monto que desea extraer de su cuenta: "))
                        if cliente[dni][3] > mon:
                            cliente[dni][3]=cliente[dni][3] - mon
                            print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
                        else:
                            print("El cliente no posee saldo suficiente para realizar la extracción.")
                    else:
                        print("No existe cliente.")  #dar la opcion de cargar cliente c.cargar_cliente()
    
                opcion=int(input("Ingresa 1 para realizar otra operación Bancaria con cliente o 2 para terminar. Gracias. : "))
                if opcion==1:
                    operar()    #Función recursiva  
               
                else:
                    print("Gracias por operar con nuestro banco.")
                    
        elif opcion==3:
            e=Empleado()
            e.menu()
            otravez=int(input("Quieres realizar otra operación? Ingresa 1 para SI / 2 para NO: "))
            if otravez==1:
                self.menu_bco()
            else:
                print("Gracias")
        else:
            print("Gracias")



cliente={236541:["Carlos Fuentes","carlitos@yahoo.com","CA",98000],456398:["Carla Flores","carlita@gmail.com","PF",35000],3654125:["Rosa Roja","rosita@gmail.com","CA",365000]}
cli=Cliente(cliente)
#cli.menu_op()
#e=Empleado
#e.menu()
bco=Banco()
bco.menu_bco()
