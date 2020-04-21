# -*- coding: utf-8 -*-
#Made by Ricard Pinzon Suller
from odoo import models, fields, api
from . import model_persona
from . import adreca_persona
class Metgehospital(model_persona.Persona, adreca_persona.Adreca):
    _name='hospitalmetge' 
    #_inherit=''
   # _inherit='persona.gestiohospital'

    numEmpleat=fields.Char(
        string='Numero empleat',
        required=True,
        )
    salariEmpleat=fields.Integer(
        string='Salari',
        )
    codiCompteCorrent=fields.Char(
        string='Codi compte corrent',
        required=True,
        )
   

#Made by Ricard Pinzon Suller
#class Metge(Persona):
#   def __init__(self):
#       self.numEmpleat = numEmpleat
#       self.salariMensual = salariMensual
#       self.codiCompteCorrent = codiCompteCorrent

       #def retornaNumEmpleat(self):
           #return NumEmpleat

       #def retornaSalariMensual(self):
           #return salariMensual

       #def retornacompteCorrent(self):
           #return codiCompteCorrent











