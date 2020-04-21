# -*- coding: utf-8 -*-
from odoo import models, fields, api
from . import model_persona
from . import adreca_persona
class Pacienthospital(model_persona.Persona, adreca_persona.Adreca):
    _name='pacient.hospital' 
    #_inherit=''
   # _inherit='persona.gestiohospital'

    _historial=fields.Integer(
    string='Historial',
       )

   
   
