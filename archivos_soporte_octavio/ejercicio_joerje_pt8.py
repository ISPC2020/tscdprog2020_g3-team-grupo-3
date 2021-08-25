import os
import time 
 
if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
 
time.sleep(1)
os.system(var) 
print("**************") 
print("*                                      *")
print("*     BANCON - TU BANCO DIGITAL        *")
print("*                                      *")
print("**************")
 
time.sleep(2)
os.system(var)
 
print("**************")
print("*                                      *")
print("*TE PRESENTAMOS TU NUEVO BANCO DIGITAL *")
print("*                                      *")
print("**************")



#Creamos la clase cliente
class Cliente:
    def _init_(self, nombre, apellido, dni, telefono, dirección, ciudad, codigo, mail): #Aqui definimos los atributos de la clase cliente
        self.nombre = nombre.capitalize()
        self.apellido = apellido.capitalize()
        self.dni = dni
        self.telefono = telefono
        self.dirección = dirección.capitalize()
        self.ciudad = ciudad.capitalize()
        self.codigo = codigo 
        self.mail = mail
        self.monto = 0 

    def _str_(self):
        return(f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"DNI: {self.dni}\n"
                f"Telefono: {self.telefono}\n"
                f"Dirección: {self.dirección}\n"
                f"Ciudad: {self.ciudad}\n"
                f"Codigo Postal: {self.codigo}\n"
                f"Mail: {self.mail}\n"
               )
   
    def depositar(self,monto):  #metodo para sumar un deposito al monto del cliente 
        self.monto=self.monto+monto
        
    def extraer(self,monto):     #metodo para extraer y actualiza el valor de la cuenta del cliente
        self.monto=self.monto-monto

    def retornar_monto(self):     #metodo para mostar el saldo de cada cliente, me sirve para luego sumar todos los montos y sacar el dinero que tiene el banco
        return self.monto

    def imprimir(self):         #metodo
        print(self.dni,"tiene depositado la suma de",self.monto)

        
#creamos la clase Banco 
class Banco:
    def _init_(self):
        self.usuarios = []
       

    def agregar_cliente(self):
        
       
        print("***********************")
        nombre = input("Digite el Nombre del usuario: ")
        apellido = input("Digite el Apellido del usuario: ")
        dni = int(input("Digite el DNI del usuario: "))
        telefono = int(input("Ingrese el Numero de telefono: "))
        dirección = (input ("Ingresar Dirección "))
        ciudad = (input("Ingresar Ciudad"))
        codigo = int(input("Ingresar Codigo Postal"))
        mail = input("Ingresar Mail")
        print("***********************","\n")
        
        
        if self.buscar_por_dni(dni):
            print("***********************")
            print("\n**PRECAUCÍON ** Ya existe un usuario con el mismo DNI ** ")
            print("***********************")
        else:
            self.usuarios.append(Cliente(nombre, apellido, dni, telefono, dirección, ciudad, codigo, mail ))

    def buscar_por_dni(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario

    def mostrar_cliente(self, dni):
        cliente = self.buscar_por_dni(dni)
        if cliente:
            print("\n", cliente)
        else:
            print("******************")
            print("\nNo existe un cliente con el DNI seleccionado","\n")
            print("******************")
            
    def eliminar_cliente(self, dni):
        dni = input("Introduce el DNI del cliente\n> ")
    
        if self.usuarios == dni:
            usuarios = clientes.pop(i)
            show(usuarios)
            #return True
            
    #return False
        
        
        #for usuario in self.usuarios:
            #if usuario == dni:
               # self.usuarios.pop
                #del(usuario)
        
        #cliente = self.buscar_por_dni(dni)
        #if cliente == dni:
            #usuario.dni.pop
            #print("el usuario fue eliminado correctamente")
        
        
        #for i, cliente in enumerate(cliente):
             #if cliente['dni'] == dni:
                #cliente = cliente.pop(i)
               # show(cliente)
               # return true
        #return False
                
                
  
            
        
        

def main():
    time.sleep(1)
    os.system(var)
    banco = Banco()
   
    print("******************")
    print("\n**   BIENVENIDO AL BANCO SUCURSAL 444 CÓRDOBA **","\n")
    print("******************")
    while True:
        try:
            print("**************")
            print("*                                      *")
            print("*         MENU PRINCIPAL               *")
            print("*                                      *")
            print("**************")
            print("\nDigite una opcion: \n\n"
            
                  "  1) Agregar usuario\n"
                  "  2) Visualizar usuario\n"
                  "  3) Eliminar usuario\n"
                  "  4) Generar Deposito\n"
                  "  5) Extracción Caja de Ahorro\n"
                  "  6) Realizar Plazo Fijo\n"
                  "  7) Salir")

            opcion = input("\nDigite una opcion: ")
           
            
            if opcion == "1":
                
                banco.agregar_cliente()

            elif opcion == "2":
                
                dni = int(input("\nDigite el DNI del usuario que desea buscar: "))
                print("======================================================")
                banco.mostrar_cliente(dni)
                print("======================================================")
                
            elif opcion =="3": 
                
                dni = input("Ingrese DNI del Usuario a Eliminar: ")
               
            
            elif opcion =="4": 
                    
                    print("**********************")
                    print(input("Ingrese su numero de DNI:"))
                    print("**********************","\n")
                    deposito = float(input("Cuanto dinero desea depositar en su cuenta ->"))
                    monto = 0
                    saldo = monto + deposito 
                    print("\n")
                    print(f"El dinero se acredito correctamente - Su Saldo es: $", saldo)
                    print("**********************")
                    print("\n")
                    
            elif opcion =="5": 
                    print("**********************")
                    extraer = float(input("Cuanto dinero desea extrer de su cuenta ->"))
                    if extraer > saldo:
                        print("\n")
                        print("El saldo en su cuenta es insuficiente","\n")
                    else:
                        saldo = saldo -extraer
                        print("\n")
                        print(f"El total de dinero en su cuenta Caja de Ahorro es: $", saldo,"\n")
                        print("*********************")
                        
                #elif opcion =="6":
            elif opcion =="7":
                        quit()
                        print("**************************")
                        print(" *Gracias por Utilizar Nuestros Servicios* - Bancon - Tu Banco Digital")
                        print("**************************")
                        
                    
        except ValueError:
            print("\nOpción incorrecta, intentelo nuevamente")
            

main()