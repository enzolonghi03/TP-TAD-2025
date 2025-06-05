#TAD AGENDA
#crear, agregar, recuperar, eliminar y cantidad.
from TadCita import *

def crearAgenda():
    # Crear agenda vacía
    agenda = []
    # Cargar citas precargadas  
    return agenda

def agregarAgenda(agenda, cita):
    agenda.append(cita)
def eliminarCita(agenda, cita):
    if 0 <= cita < len(agenda):
        agenda.pop(cita)

def recuperarCita(agenda, i):
    return agenda[i]

def tamanio(agenda):
    return len(agenda)
