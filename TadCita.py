#Tad simple cita

def crearCita():
    #nombre de la Actividad, nivel de importancia, fecha y hora de inicio 
    cita = {
        'actividad': None,
        'fecha': None,
        'prioridad': None,
    }
    return cita
def cargarCita(cita,act,fe,h):
    cita['actividad'] = act    
    cita['fecha'] = fe
    cita['prioridad'] = h

def asignarCita(cita1, cita2):
    cita1['actividad']=cita2['actividad']
    cita1['fecha']=cita2['fecha']
    cita1['prioridad']=cita2['prioridad']

def verActividad(cita):
    return cita['actividad']
def verFecha(cita): 
    return cita['fecha']
def verPrioridad(cita):
    return cita['prioridad']

def modAct(cita, nuevaAct):
    cita['actividad'] = nuevaAct
def modFecha(cita, nuevaFecha):
    cita['fecha'] = nuevaFecha
def modNivel(cita, nuevoNivel):
    cita['prioridad'] = nuevoNivel
