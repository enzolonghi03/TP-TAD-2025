#Tad simple cita

def crearCitaCola():
    #nombre de la Actividad, nivel de importancia, fecha y hora de inicio 
    cita = {
        'actividad': None,
        'prioridad': None,
    }
    return cita
def cargarCitaCola(cita,act,p):
    cita['actividad'] = act
    cita['prioridad'] = p

def asignarCitaCola(cita1, cita2):
    cita1['actividad']=cita2['actividad']
    cita1['prioridad']=cita2['prioridad']

def verActividadCitaCola(cita):
    return cita['actividad']
def verPrioridadCitaCola(cita):
    return cita['prioridad']

def modActCitaCola(cita, nuevaAct):
    cita['actividad'] = nuevaAct
def modPrioridadCitaCola(cita, p):
    cita['prioridad'] = p
