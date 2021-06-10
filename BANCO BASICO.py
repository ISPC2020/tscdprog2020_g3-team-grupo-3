class Cliente:
    def __init__(self, dni, nombre, apellido, domicilio, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.domicilio = domicilio
        self.telefono = telefono


    def __str__(self):
        return ("DNI: "+self.dni+"\nNombre: "+self.nombre+"\nApellido: "+self.apellido+"\nDomicilio: "+self.domicilio+"\nTelefono: "+ str(self.telefono))

class Banco:
    def __init__(self, cliente, num_cta, saldo,):
        self.cliente = cliente
        self.num_cta = num_cta
        self.saldo = saldo

    def extrac(self, monto):
        if monto > self.saldo:
            print("\nNo se puede realizar esta operación: Saldo insuficiente!")
        else:
            self.saldo -= monto
            print(f"\nSe extrajeron ${monto} Pesos. Su saldo actual es de ${self.saldo} Pesos")

    def deposito(self, monto):
        if monto < 0 or monto == 0:
            print(f"\nNo se puede realizar esta operación: Monto insuficiente!")
        else:
            self.saldo += monto
            print(f"\nSe depositaron ${monto} Pesos.Su saldo actual es de ${self.saldo} Pesos")

    def mostrar_saldo(self):
        print(f"\nEl Saldo actual de su cuenta es de ${self.saldo} Pesos.")

#   def mostrar_info(self):
#        print(f"Hola {user1.nombre}, su nro de cuenta es {cta1.num_cta}.")


#  Menu Clientes
dni = str(input("Ingrese su DNI: "))
nombre = str(input("Ingrese su Nombre: "))
apellido = str(input("Ingrese su Apellido: "))
domicilio = str(input("Ingrese su Domicilio: "))
telefono = str(input("Ingrese su nro de teléfono: "))


user1 = Cliente(dni, nombre, apellido , domicilio, telefono)

# Menu Operaciones
num_cta = str(input("Ingrese el número de cuenta: "))
saldo = int(input("Deposito inicial?: "))
cta1 = Banco(user1, num_cta, saldo)



menuoper = True

while menuoper:
    opcion = int(input("""\nIngrese una opcion:
    1 - Extracción
    2 - Depósito
    3 - Saldo
    
    0 - Salir
    
                          """))

    if opcion == 1:
        valor = int(input(f"Su disponible es de {cta1.saldo}. Cuanto desea extraer? "))
        cta1.extrac(valor)
    elif opcion == 2:
        valor = int(input(f"Monto a depositar? "))
        cta1.deposito(valor)
    elif opcion == 3:
        cta1.mostrar_saldo()
#    elif opcion == 4:    ---> 4 - Mostrar información
#       user1.mostrar_info()
    elif opcion == 0:
        print("Hasta pronto!!")
        break
    else:
        print("Opcion incorrecta: Intente nuevamente!")


