# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:51:23 2021
@author: CarinaG.
"""

class Cliente:  #defino la clase Cliente que me permite agregar, buscar, mostrar y eliminar a clientes.
    
    def __init__(self,cliente):  #constructor. con este método inicializo al objeto cliente
        self.cliente=cliente
        
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
            print("Los datos del cliente se han actualizado.")
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
    
    

class Banco(Cliente):  #Creo la Clase Banco para cargar agenda y operar con las cuentas.  (reutilizamos la función buscar cliente de la clase cliente)
    
    def __init__(self,cliente):
        self.cliente=cliente  #recibo por parámetro el dict de clientes
        self.agendaxfecha={}  #se crea un diccionario vacío para luego almacenar los horarios y las visitas de los clientes
        
        
    def agenda(self):
         continua1="s"
         print("-------------------------------------------------")
         print("        .·.·  BANCO EL OCHO   ·.·.        ")
         print("Cargamos la Agenda con la visita de los clientes.") 
         print("-------------------------------------------------")
         while continua1=="s":   #ciclo que permite cargar las actividades detallando fecha, hora y descripcion por cada ingreso
            fecha=input("Ingrese la fecha con formato dd/mm/aa:")
            continua2="s"
            lista=[]
            while continua2=="s":   # este ciclo se repite mientras haya que cargar clientes para el mismo día
                 hora=input("Ingrese la hora de la cita del cliente con formato hh:mm ")
                 d=super().buscar_cliente()  #llamo a la función buscar cliente de la clase cliente (Clase Padre)
                 lista=[hora,d,self.cliente[d][0]]
                 continua2=input("Ingresa otra actividad para la misma fecha[s/n]:")
            self.agendaxfecha[fecha]=lista     #cuando se terminan de cargar todos los  clientes para una determinada fecha se procede a insertar la lista en el diccionario:
            continua1=input("Ingresa otra fecha[s/n]:")
         
         return print("\nDetalle de Agenda: \n",self.agendaxfecha)
   
        
        
    def consulta_fecha(self):  #método para consultar los clientes agendados en una fecha ingresada
        print("-------------------------------------------")
        print("Consulta de agenda")
        fecha=input("Ingrese la fecha que desea consultar:")
        if fecha in self.agendaxfecha:
            for i in self.agendaxfecha:
                print(fecha,"  Hora",self.agendaxfecha[fecha][0],"  DNI del cliente",self.agendaxfecha[fecha][1], "  Nombre del Cliente: ",self.agendaxfecha[fecha][2])
            
            
            
    def operar(self):
        print("-------------------------------------------")
        print("Operar con Banco el Ocho")
        fecha=input("Ingresa la fecha para abrir la agenda de hoy, formato dd/mm/aa: ")
        if fecha in self.agendaxfecha:
            dni=int(input("Ingrese el número del DNI para realizar la operación Bancaria: "))
            operacion,monto=0,0
            ganancia=0.8   
            for i in self.agendaxfecha.values():
                if dni == self.agendaxfecha[fecha][1]:
                    print("El cliente tiene agendada visita al banco hoy.")
                    operacion=int(input("Ingrese la operación Bancaria: 1 -Deposito en CA / 2 -Deposito en PF por 30 días/ 3 -Extracción : "))
                     
                    if operacion==1:
                        if cliente[dni][2]=="CA":
                            mon=float(input("Ingrese el monto correspondientea depositar en su Caja de Ahorro: "))
                            cliente[dni][3]=cliente[dni][3] + mon
                            print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
                        else:
                            print("El cliente no posee Caja de Ahorro y no puede operar sin una.")
                        
                
                    elif operacion==2:  # si se elige esta operacion cliente deposita en PF a 30 días
                        if cliente[dni][2]=="PF":
                            mon=float(input("Ingrese el monto correspondientea depositar en Plazo Fijo por 30 días: "))
                            cliente[dni][3]=cliente[dni][3] + mon +(mon * ganancia)
                            print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
                        else:
                            print("El cliente no tiene una cuenta Plazo Fijo y no puede eoprar sin una.")

                    elif operacion==3:  # si se ingresa esta opción el cliente realiza una extraccion de su CA
                        mon=float(input("Ingrese el monto que desea extraer de su cuenta: "))
                        if cliente[dni][3] > mon:
                            cliente[dni][3]=cliente[dni][3] - mon
                            print("El saldo actual del cliente: ",dni,cliente[dni][0], " es: ",cliente[dni][3])
                        else:
                            print("El cliente no posee saldo suficiente para realizar la extracción.")

                    else:
                        print("Ingreso una opción no válida")              
                else:
                    print("El cliente no tiene agendada visita hoy.")
        else:
            print("No hay actividades para la fecha ingresada.")

        

#creo un diccionario con algunos clientes cargados para poder trabajar luego en los métodos y poder controlar los cambios.
cliente={236541:["Carlos Fuentes","carlitos@yahoo.com","CA",98000],456398:["Carla Flores","carlita@gmail.com","PF",35000],3654125:["Rosa Roja","rosita@gmail.com","CA",365000]}
c=Cliente(cliente)  #creo el objeto Cliente y le paso por parámetro el diccionario con clientes 
c.mostrar_clientes()  #instancio a la clase mostrar clientes
c.buscar_cliente()   #instancio a la clase buscar clientes
c.agregar_cliente() #instancio a la clase agregar cliente
c.modificar_cliente()  #instancio a la clase modificar cliente
#c.eliminar_cliente()  #instancio a la clase eliminar cliente 
#c.mostrar_clientes()  #nuevamente voy a instanciar al método mostrar para constatar que se elimino el cliente
bco=Banco(cliente)  #creo el objeto Banco que recibe por parámetro el diccionario con clientes cargados
a=bco.agenda()  #inistancio al método agenda para cargar actividades en el Banco
print(a)
bco.consulta_fecha()   # consulto las fechas cargadas en la agenda
bco.operar()  #instancio al método operar 