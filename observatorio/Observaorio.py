from Planeta import Planeta
class Observaorio:
    """________________________________________________________
    #Constantes
    ________________________________________________________"""
    CANTIDAD_PLANETAS = 8
    NOMBRES_PLANETAS={
        "MERCURIO" : "mercurio",
        "VENUS" : "venus",
        "TIERRA" : "tierra",
        "MARTE" : "marte",
        "JUPITER" : "jupiter",
        "SATURBO" : "saturno",
        "URANO" : "urano",
        "NEPTUNO" : "neptuno"
    }

    """________________________________________________________
    #Metodos
    ________________________________________________________"""
    
    def __init__(self):
        self.__planetas = []
    
    def getNombresPlanetas (self):
        nombrePlanetas = []
        for nombre in self.NOMBRES_PLANETAS.items():
            keys = nombre(0)
            nombrePlanetas.append(keys)
        return nombrePlanetas
    
    def getSateliteNaturalNombre (self, nombre):
        Planeta.getSatelite(nombre)
        
    def getPlanetaPorDistancia (self, distancia):
        Planeta.getSatelite(distancia)
        
    def getPlanetaPorInclinacion(self, inclinacion):
        Planeta.getSatelite(inclinacion)
        
    def agregarSateliteNatural(self, nombre, exentricidad, inclinacion):
        Planeta.agregarSatelite(nombre, exentricidad, inclinacion)
        return Planeta.agregarSatelite(nombre, exentricidad, inclinacion)
    def eliminarSatelite (self, nombre):
        Planeta.eliminarSatelite(nombre)
    def editarSatelite(self, nombre, exentricidad, inclinacion):
        Planeta.esitarSatelite(nombre, exentricidad, inclinacion)