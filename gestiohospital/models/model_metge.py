from odoo import models, fields, api
from . import model_persona
class Metgehospital(model_persona.Persona):
    _name='hospitalmetge'
    _inherit = 'adreca.hospital'


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
   









