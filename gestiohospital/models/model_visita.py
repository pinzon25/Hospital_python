from odoo import models, fields, api
class Visita(models.Model):
    _name='visita.pacient'

    data=fields.Date(
        string='Data',
        )
