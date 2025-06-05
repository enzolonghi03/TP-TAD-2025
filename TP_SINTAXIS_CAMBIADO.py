
##5) Desarrollar una aplicación que permita gestionar una agenda personal de citas, utilizando los Tipos Abstractos de Datos (TADS) que el estudiante considere apropiados. Cada cita deberá contener: actividad a realizar, nivel de importancia, fecha y hora de inicio. La aplicación deberá presentar un menú interactivo para que el usuario realice distintas operaciones de administración sobre las citas registradas.
##a. Alta de citas:
##Implementar la opción para agregar nuevas citas a la agenda, solicitando todos los datos requeridos: actividad, nivel de importancia, fecha y hora de inicio.
##b. Modificación de una cita existente:
##Permitir la actualización completa o parcial de los datos de una cita ya registrada, identificándola mediante la fecha y hora de inicio.
##c. Eliminación de citas individuales:
##Desarrollar la funcionalidad para eliminar una cita específica de la agenda, liberando su espacio en el calendario personal.
##d. Listado general de citas:
##Implementar una función que muestre todas las citas almacenadas, detallando actividad, importancia, fecha y hora de cada una. e. Reorganización y depuración por fecha: o a) Trasladar todas las citas de una fecha determinada a una nueva fecha ingresada por el usuario.
##0
##b) Eliminar todas las citas correspondientes a un día específico, permitiendo limpiar completamente la agenda para esa fecha.
##f. Generación de cola filtrada por día: Crear una nueva cola que contenga únicamente las actividades y su nivel de importancia de un día específico. Esta cola deberá generarse y mostrarse
##automáticamente en pantalla.

###APLICACION DE CITAS PERSONALES###

from TadCita import *
from TadAgenda import *
import datetime
#variables globales
agen=crearAgenda()

citas = [
        ("Turno con el Dentista", datetime.datetime.strptime("15/06/2025-10:30", "%d/%m/%Y-%H:%M"), 3),
        ("Reunion de trabajo",datetime.datetime.strptime("18/06/2025-14:00", "%d/%m/%Y-%H:%M") , 2),
        ("Ir al gimnasio",datetime.datetime.strptime( "20/06/2025-19:00", "%d/%m/%Y-%H:%M"), 1),
        ("Cumpleaños de Ana",datetime.datetime.strptime("25/06/2025-20:00", "%d/%m/%Y-%H:%M") , 2),
        ("Parcial de Algebra",datetime.datetime.strptime("01/07/2025-08:00", "%d/%m/%Y-%H:%M") , 3)
    ]
for i in citas:
        c = crearCita()
        cargarCita(c, *i) 
        agregarAgenda(agen, c)  

#imprime agenda completa
def mostrar_cita(cita):
    print("Nombre:",verActividad(cita))
    print("Fecha:", verFecha(cita))
    print("Prioridad:",verPrioridad(cita))
    
def verAgenda():
    if tamanio(agen)==0:
        print("No hay citas en agenda ")
    else:
        for i in range(tamanio(agen)):
            aux=recuperarCita(agen, i)
            print(f"\nCita {i+1}:")
            mostrar_cita(aux)
            print("-" * 40)

        
#funciones para el menu de seleccion
def agregar():#Crea y carga una nueva cita
    print("=" * 40)
    print("       NUEVA CITA")
    print("=" * 40)
    print("Para comenzar presione s")  #Punto -A- "ALTA DE CITAS"
    aux = 's'
    while aux == 's':
        cita=crearCita()
        print("-"*40)
        print("- INGRESE LOS DATOS DE LA NUEVA CITA\n")
        nombre=input("- Nombre de la cita - ")       
        fecha = input("- Ingrese la fecha (DD/MM/AAA):  ")
        hora = input("- Ingrese la hora (HH:SS): ")
        
        fecha_completa = datetime.datetime.strptime(f'{fecha}-{hora}', "%d/%m/%Y-%H:%M")
        c = True
        while c:
            try: 
                importancia = int(input("- Nivel de importancia (1 bajo, 2 medio, 3 alto): "))
                if 0<importancia<4:
                    c=False
                else:
                    print("Ingrese un valor valido")
            except ValueError:
                print("Ingrese un valor valido")
        cargarCita(cita,nombre,fecha_completa,importancia)
        agregarAgenda(agen,cita)
        #devuelve la cita creada
        print("="*21)
        mostrar_cita(cita)
        print("="*21)

        print("Desea agregar otra cita? ")
        aux = input("s=si, n=no")
        

# Muestra las citas agendadas
# Modifica las citas por items
# modifica la cita completa
def modificar():
    #verifica que la lista no este vacia
    if not agen:
        print("No hay citas agendadas")
    else:
        verAgenda()    
        print("\n")
    #opciones para modificar la cita
    continuar = 's'
    while continuar == 's':
        cita=int(input("Ingrese el numero de la cita a modificar: "))
        if 1 <= cita <= tamanio(agen):
            print("=" * 40)
            print("    - CITA SELECCIONADA: ",cita,"-")            
            aux=recuperarCita(agen, cita-1)
            mostrar_cita(aux)
            print("=" * 40)
            mod=input("¿DESEA MODIFICAR LA CITA SELECCIONADA? S/N ").lower()
            print("-" * 40)
            if mod == "s":
                cont = "s"
                while cont == "s":
                    print("indique que desea modificar")
                    print("1 - Actividad")
                    print("2 - Fecha")          #Punto -B- "Modificacion de citas existentes"
                    print("3 - Prioridad")
                    print("4 - Modificar TODO")
                    print("=" * 40)
                    aux1=input("")
                    validos = ["1", "2", "3", "4", "5"]
                    if aux1 in validos:
                        if aux1=="1":
                            print("Nombre",verActividad(aux))
                            act=input("ingrese nueva actividad ")
                            modAct(aux,act)
                            print("."*40)
                            print("El nombre fue cambiada exitosamente")
                            mostrar_cita(aux)
                            print("."*40)
                        elif aux1=="2":
                            print("Fecha",verFecha(aux))
                            fecha = input("- Ingrese la nueva fecha (DD/MM/AAA):  ")
                            hora = input("- Ingrese la nueva hora (HH:SS): ")
                            fecha_completa = datetime.datetime.strptime(f'{fecha}-{hora}', "%d/%m/%Y-%H:%M")
                            modFecha(aux,fecha_completa)
                            print("."*40)
                            print("    - La fecha fue cambiada exitosamente")
                            mostrar_cita(aux)
                            print("."*40)
                        elif aux1=="3":
                            print("Prioridad",verPrioridad(aux))
                            prioridad=input("ingrese la nueva prioridad ")
                            modNivel(aux,prioridad)
                            print("."*40)
                            print("La prioridad de la cita fue cambiada")
                            mostrar_cita(aux)
                            print("."*40)
                        elif aux1=="4":
                            mostrar_cita(aux)
                            print("\n")
                            act=input("ingrese nueva actividad ")
                            modAct(aux,act)
                            fech=input("ingrese nueva Fecha ")
                            modFecha(aux,fech)
                            prioridad=input("ingrese nueva prioridad ")
                            modNivel(aux,prioridad)
                            print("."*40)
                            print("La cita fue modificada exitosamente")
                            mostrar_cita(aux)
                            print("."*40)                       
                        break
                    else:
                        print("Opcion incorrecta por favor ingrese 1 - 2 - 3 - 4 - 5")
        else:
            print("cita no encontrada")
        print("Desea continuar modificando citas?: ")
        continuar = input("s=si, n=no")
def eliminar():
    print("=" * 40)
    print("    - ELIMINAR CITA -")
    print("=" * 40)
    while True:
        a=input("Desea ver la agenda? s/n ").lower()  
        if a=="s":
            verAgenda()
        nro=int(input("Ingresa el numero de la cita a eliminar: "))
        if 1 <= nro <= tamanio(agen):
            aux=recuperarCita(agen,nro-1)
            print("-"*40)
            mostrar_cita(aux)
            print("-"*40)
            eliminar=input("¿DESEA ELIMINAR LA CITA SELECCIONADA? s/n ").lower()
            print("-"*40)
            if eliminar == "s":
                eliminarCita(agen, nro-1)
                print("    * CITA ELIMINADA *\n")
                opc=input("Desea eliminar otra cita s/n ")
                if opc=="s":
                    continue
                else:
                    return
            elif eliminar=="n":
                print("NO SE ELIMINÓ NINGUNA CITA.\n")
                return
                
def verCitas():
    print("=" * 40) 
    print("    - VER CITAS -") 
    print("="*40)   
    print("Cantidad de citas agendadas: ",tamanio(agen))
    verAgenda()


def mover_citas_entre_fechas():
    fecha1 = input("Ingrese la fecha de donde quiere obtener las citas (DD/MM/AAAA): ")
    fecha_buscada = datetime.datetime.strptime(fecha1,'%d/%m/%Y')
    fecha2 = input("Ingrese la fecha a donde quiere mover las citas (DD/MM/AAAA): ")
    for i in range(tamanio(agen)):
        aux = recuperarCita(agen, i-1)
        print(verFecha(aux))
        fecha_aux = verFecha(aux)
        if fecha_aux.date() == fecha_buscada.date():
            horario_cita = fecha_aux.strftime("%H:%M")
            fecha_nueva = datetime.datetime.strptime(f'{fecha2}-{horario_cita}',"%d/%m/%Y-%H:%M")
            modFecha(aux, fecha_nueva)
        print("Nueva fecha: \n")
        print(verFecha(aux))


def eliminar_citas_de_fecha():
    fecha1 = input("Ingrese la fecha de donde quiere eliminar las citas (DD/MM/AAAA): ")
    fecha_buscada = datetime.datetime.strptime(fecha1,'%d/%m/%Y')
    for i in range(tamanio(agen)):
        aux = recuperarCita(agen, i-1)
        fecha_aux = verFecha(aux)
        if fecha_aux.date() == fecha_buscada.date():
            eliminarCita(agen, i-1)
        
            
        


def cola():    
   
    print("MODIFICAR UNA CITA\n ")
          



#lista de opciones
menu = {
    "1": agregar,
    "2": modificar,
    "3": eliminar,
    "4": verCitas,
    "5": mover_citas_entre_fechas,
    "6": cola,
    "7": eliminar_citas_de_fecha,
    }

#Menu Principal
print("=" * 40)
print("BIENVENIDOS A TU AGENDA PERSONAL DE CITAS")

while True:
    
    print("=" * 40)    
    print("      -----MENU PRINCIPAL-----")   
    print("=" * 40)
    print("Por favor eliga una opción")
    print("-" * 40) 
    print("1 Agregar nueva cita")
    print("2 Modificar citas")    
    print("3 Eliminar Cita")       
    print("4 Ver Citas")
    print("5 Mover citas de un dia hacia otro")
    print("6 cola")
    print("7 Eliminar citas de una fecha")
    print("-" * 40)
    print("PARA TERMINAR PRESIONE s")    
    print("-" * 40)

    opc= input("-->")     
#selectro de opciones y finalizacion del programa
    if opc in menu:
        menu[opc]()
    elif opc.lower() == "s":
        break
    else:
        print("Opcion inválida")
            
            

