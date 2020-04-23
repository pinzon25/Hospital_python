from odoo import models, fields, api
class Adreca(models.Model):
    _name='adreca.hospital'

    ciutat = fields.Char(
        string='Ciutat',
        required=True,
        size=15
        )
    codipostal=fields.Integer(
        string='Codi Postal',
        required=True,
        size=20
        )
    carrer = fields.Char(
        string='Carrer',
        required=True,
        size=25
        )
    numero= fields.Integer(
        string='Numero',
        required=True,
        )
    planta=fields.Char(
        string='Planta'
        )
    porta=fields.Char(
        string='Porta'
        )



