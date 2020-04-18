# -*- coding: utf-8 -*-
#Made by Ricard Pinzon Suller
from odoo import models, fields, api
from . import adreca_persona #Ultim afegit
class Persona(models.Model):
    _name='metge.hospital'

    nom = fields.Char(
        string='Nom',
        required=True,
        size=15
    )
    cognoms = fields.Char(
        string='Cognoms',
        required=True,
        size=20
    )
    numSegSocial = fields.Char(
        string ='Nº seguretat social',
        required=True,
        size=24
        )
    nif = fields.Char(
        string='Nif',
        required=True,
        size=9
        )
    telefon=fields.Char(
        string='Telefon',
        required=True,
        size=9
        )
    #ultim afegit
    adreca= fields.Many2one( #Moltes persones poden tenir una adreca.
        'adreca.hospital', 
        string='Adreca')





#Made by Ricard Pinzon Suller
#class Persona(ABC):
#    def __init__(self, name, cognom1, cognom2, numSegSocial, nif, telefon):
#        self.name = name
#        self.cognom1 = cognom1
#        self.cognom2 = cognom2
#        self.numSegSocial = numSegSocial
#        self.nif = nif
#        self.telefon = telefon
#
#        @abstractmethod
#        def FullName(self):
#            return self.name + " " + self.cognom1 + " " + self.cognom2
#
#        @abstractmethod
#        def NumSocialSeg(self):
#            return self.numSegSocial
#
#        @abstractmethod
#        def NifPersona(self):
#            return nif
#
#        @abstractmethod
#        def Telefon(self):
#            return telefon