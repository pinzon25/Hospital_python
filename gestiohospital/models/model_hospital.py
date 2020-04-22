from odoo import models, fields, api
from . import model_persona
class Hospital(models.Model):
    _name='hospitalprincipal'

    nomHospital=fields.Char(
        string='Nom del Hospital',
        required=True,
        )