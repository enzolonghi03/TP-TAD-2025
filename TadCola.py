from TadCita import *
#TAD cola

def crearCola():
    cola = []
    return cola

def esVacia(cola):
    return len(cola) == 0

def encolar(cola, cita):
    cola.append(cita)

def desencolar(cola):
    if not esVacia(cola):
            return cola.pop(0)  
    return None



def copiar(cola1, cola2):
    aux = crearCola()
    while not cola1.esVacia():
        elemento = cola1.desencolar()
        aux.encolar(elemento)
    while not aux.esVacia():
        elemento = aux.desencolar()
        cola2.encolar(elemento)