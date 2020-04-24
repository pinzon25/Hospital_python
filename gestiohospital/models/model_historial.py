from odoo import models, fields, api
class Historial(models.Model):
    _name='historial.hospital'

    codi = fields.Integer(
        string='Codi',
        )

    visita= fields.Many2one(
        'visita.pacient', 
        string='Visita')