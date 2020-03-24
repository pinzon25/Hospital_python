from models import Persona
from abc import abstractmethod

class Pacient(Persona):
    def __init__(self, name, cognom1, cognom2, numSegSocial, nif, telefon):
        self.name = name
        self.cognom1 = cognom1
        self.cognom2 = cognom2
        self.numSegSocial = numSegSocial
        self.nif = nif
        self.telefon = telefon

        @abstractmethod
        def FullName(self):
            return self.name + " " + self.cognom1 + " " + self.cognom2

        @abstractmethod
        def NumSocialSeg(self):
            return self.numSegSocial

        @abstractmethod
        def NifPersona(self):
            return nif

        @abstractmethod
        def Telefon(self):
            return telefon