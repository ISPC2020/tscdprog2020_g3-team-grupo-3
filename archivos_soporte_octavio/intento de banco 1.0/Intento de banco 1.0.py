# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 02:19:52 2021
Finished on Mon Jun  7 02:46:47 2021
@author: User
"""

# importamos modulos

import csv
import itertools
import re
from datetime import datetime

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

# creamos las clases
class Contacto:
    nuevoId = itertools.count()
    def __init__(self, nombre, apellido, dni, domicilio, telefono, caja_ahorro, plazo_fijo):
        self.codigo = next(self.nuevoId)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.domicilio = domicilio
        self.telefono = telefono
        self.caja_ahorro = caja_ahorro
        self.plazo_fijo = plazo_fijo
        self.saldo_ca = saldo_ca
        self.saldo_pf = saldo_pf

class Agenda:
    def __init__(self):
        # creamos una lista
        self.contactos = []

# a partir de aqui creamos los metodos de la agenda
    def ordenarxnombre(self):
        self.contactos.sort(key=lambda contacto: contacto.nombre)

    def ordenarxapellido(self):
        self.contactos.sort(key=lambda contacto: contacto.apellido)

    def insertar(self, nombre, apellido, dni, domicilio, telefono, caja_ahorro, plazo_fijo):
        contacto = Contacto(nombre, apellido, dni, domicilio, telefono, caja_ahorro, plazo_fijo)
        self.contactos.append(contacto)

    def mostrartodos(self):
        self.submenuorden()
        for contacto in self.contactos:
            self.mostrarcontacto(contacto)

    def buscar(self, textobuscar):
        encontrado = 0
        for contacto in self.contactos:
            # para buscar un contacto creamos el condicional y utilizamos las expresiones regulares
            if (re.findall(textobuscar, contacto.nombre)) or (re.findall(textobuscar, contacto.apellido)):
                self.mostrarcontacto(contacto)
                encontrado = encontrado + 1
                self.submenubuscar(contacto.codigo)
        if encontrado == 0:
            self.noencontrado()

    def cargar_saldos(self):
        for contacto in self.contactos:
            if contacto.dni == dni:
                self.contactos.append(contacto.saldo_ca)


    def borrar(self, codigo):
        for contacto in self.contactos:
            if contacto.codigo == codigo:
                print()
                print("\u001B[31m                *********************************")
                print(
                    "\u001B[31m                * Confirma borrar contacto \u001B[33mS\u001B[31m/\u001B[33mN:\u001B[31m *")
                print("\u001B[31m                *********************************")
                opcion = str(input(""))
                if opcion == "s" or opcion == "S":
                    print()
                    print("                *********************************")
                    print("                *   El contacto fue borrado!!!  *")
                    print("                *********************************")
                    del self.contactos[codigo]
                elif opcion == "n" or opcion == "N":
                    break

    def modificar(self, codigo):
        # cuando elegimos modificar, primero borramos el contacto y luego ingresamos nuevamente todos los campos
        for contacto in self.contactos:
            if contacto.codigo == codigo:
                del self.contactos[codigo]
                print("\u001B[32m          ********************************************")
                print("\u001B[32m          ********************************************")
                nombre = str(input("\u001B[37m                   Ingrese el nombre: "))
                apellido = str(input("\u001B[37m                   Ingrese el apellido: "))
                dni = str(input("\u001B[37m                   Ingrese el dni: "))
                domicilio = str(input("\u001B[37m                   Ingrese el domicilio: "))
                telefono = str(input("\u001B[37m                   Ingrese el nro de telefono: "))
                caja_ahorro = str(input("\u001B[37m                   Posee una Caja de Ahorro SI/NO?: "))
                plazo_fijo = str(input("\u001B[37m                   Posee un Plazo Fijo SI/NO: "))
                contacto = Contacto(nombre.capitalize(), apellido.capitalize(), dni, domicilio.capitalize(), telefono, caja_ahorro.upper(), plazo_fijo.upper())
                self.contactos.append(contacto)
                break

    # en la opcion Buscar encontramos las opciones de modificar o borrar un contacto
    def submenubuscar(self, codigo):
        print()
        print("\u001B[32m       ***************************************************")
        print(
            "       *   \u001B[37mUd. desea \u001B[33mM\u001B[37modificar o \u001B[33mB\u001B[37morrar este contacto? \u001B[32m  *")
        print("\u001B[32m       ***************************************************")
        opcion = str(input(""))
        if opcion == "m" or opcion == "M":
            self.modificar(codigo)
        elif opcion == "b" or opcion == "B":
            self.borrar(codigo)
        else:
            print()
            print()
            print("\u001B[32m          *********************************************")
            print("\u001B[32m          *********************************************")
            print()
            print("\u001B[32m          *********************************************")
            print("          * \u001B[37mLos datos se actualizaron exitosamente!!!\u001B[32m *")
            print("          *********************************************")
            print()
            print()

    def submenuorden(self):
        print()
        print("\u001B[32m          *********************************************")
        print(
            "          * \u001B[37m   Desea ordenar por \u001B[33mN\u001B[37mombre o \u001B[33mA\u001B[37mpellido?\u001B[32m   *")
        print("\u001B[32m          *********************************************")
        opcion = str(input(""))
        if opcion == "n" or opcion == "N":
            self.ordenarxnombre()
        elif opcion == "a" or opcion == "A":
            self.ordenarxapellido()
    #guarda en csv
    def guardar(self):
        with open("DB_banco.csv", "w") as archivo:
            escribir = csv.writer(archivo)
            escribir.writerow(("codigo", "nombre", "apellido", "dni", "domicilio", "telefono", "caja_ahorro", "plazo_fijo"))
            for contacto in self.contactos:
                escribir.writerow((contacto.codigo, contacto.nombre, contacto.apellido, contacto.dni, contacto.domicilio,
                                  contacto.telefono, contacto.caja_ahorro, contacto.plazo_fijo))

    def mostrarcontacto(self, contacto):
        print()
        print("\u001B[32m          *********************************************")
        print("          *********************************************")
        print("\u001B[37m                   Código: {}".format(contacto.codigo))
        print("                   Nombre: {}".format(contacto.nombre))
        print("                   Apellido: {}".format(contacto.apellido))
        print("                   D.N.I.: {}".format(contacto.dni))
        print("                   Domicilio: {}".format(contacto.domicilio))
        print("                   Teléfono: {}".format(contacto.telefono))
        print("                   Posee Caja de Ahorro: {}".format(contacto.caja_ahorro))
        print("                   Posee Plazo Fijo: {}".format(contacto.plazo_fijo))
        print("\u001B[32m          *********************************************")
        print("          *********************************************")
        print("")

    def noencontrado(self):
        print("""
              
              """)
        print("""\u001B[31m 
                 *****************************
                 * Contacto no encontrado!!! *
                 *****************************
                         """)

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

class Banco(Agenda):
        def depositar_ca(self):
            dni_dep = str(input("Ingrese D.N.I:"))
            monto_ca = str(input("Ingrese monto a depositar:"))
            monto_ca += saldo_ca
            if dni_dep in self.contactos:
                with open("DB_banco.csv", "w") as archivo:
                    escribir = csv.writer(archivo)
                    escribir.writerow(("codigo", "dni","saldo_ca"))
                    for contacto in self.contactos:
                        escribir.writerow((contacto.codigo, contacto.dni, contacto.saldo_ca))

                    print("se asi")
#            else:
#                break

            self.extraer()
            if menu_banco == "1":
                print("Operaciones con Cajas de Ahorro")
            elif menu_banco == "2":
                print("Operaciones con Plazos Fijos")
                texto = str(input("""\u001B[32m
  ***********************************************************
  *         \u001B[37mEscribe el texto a buscar en Contactos: \u001B[32m        *
  *                                                         *       
                            """))
                agenda.buscar(texto.capitalize())
                agenda.guardar()
            elif menu_banco == "3":
                print("Total Depositos")
            elif menu_banco == "0":
                agenda.noencontrado()
#                ejecutar()

#                break
            else:
                print("""
              
                        """)
                print(""""\u001B[31m 
                 *****************************
                 *    Opción incorrecta!!!   *
                 *****************************
                         """)



if __name__ == "__main__":
    ejecutar()
