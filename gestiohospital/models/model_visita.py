from odoo import models, fields, api
class Visita(models.Model):
    _name='visita.pacient'

    data=fields.Date(
        string='Data',
        )

    malaltia= fields.Many2one(
        'malaltia.pacient', 
        string='Malaltia')

    metge= fields.Many2one(
        'hospitalmetge.', 
        string='Metge')