from odoo import models, fields, api
from . import model_persona
class Pacienthospital(model_persona.Persona):
    _name='pacient.hospital'
    _inherit = 'adreca.hospital'

    _historial=fields.Integer(
    string='Historial',
       )

   
   
