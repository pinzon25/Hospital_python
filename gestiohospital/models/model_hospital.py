# -*- coding: utf-8 -*-
#Made by Ricard Pinzon Suller
from odoo import models, fields, api
from . import model_persona
class Hospital(models.Model):
    _name='hospitalprincipal' 
    #_inherit=''
   # _inherit='persona.gestiohospital'

    nomHospital=fields.Char(
        string='Nom del Hospital',
        required=True,
        )
