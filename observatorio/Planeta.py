from SateliteNatural import SateliteNatural

class Planeta:
    def __init__(self, nombre, distanciaMediaSol, exentricidad, periodoOrbitalSinodico, velocidadOrbitalMedia, inclinacion):
        self.__satelites = []
        self.__nombre = nombre
        self.__distanciaMediaSol = distanciaMediaSol
        self.__exentricidad = exentricidad
        self.__periodoOrbitalSinodico = periodoOrbitalSinodico
        self.__velocidadOrbitalMedia = velocidadOrbitalMedia
        self.__inclinacion = inclinacion
        
    def getNombre (self):
        return self.__nombre
    def getDistanciaMediaSol (self):
        return self.__distanciaMediaSol
    def getInclinacion(self):
        return self.__inclinacion
    
    def agregarSatelite (self, nombre, exentricidad, inclinacion):
        agrego = False
        nuevo = SateliteNatural(nombre, exentricidad, inclinacion)
        self.__satelites.append(nuevo)
        if nuevo is not None:
            agrego = True
        return agrego
    
    def getSatelites(self):
        return self.__satelites
    
    def eliminarSatelite(self, nombre):
        self.__satelites.remove(nombre)
        
    def getSatelite(self, nombre):
        return self.__satelites[self.__satelites.index(nombre)]
    
    def editarSatelite(self, nombre, exentricidad, inclinacion):
        for satlite in self.__satelites:
            if satlite.getNombre() == nombre:
                satlite.setInclinacionOrbita(inclinacion)
                satlite.setExentricidad(exentricidad)