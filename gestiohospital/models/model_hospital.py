from odoo import models, fields, api
from . import model_persona
class Hospital(models.Model):
    _name='hospitalprincipal'
    _inherit = 'adreca.hospital'

    nomHospital=fields.Char(
        string='Nom del Hospital',
        required=True,
        )