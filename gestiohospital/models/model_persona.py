from odoo import models, fields, api
from . import adreca_persona
class Persona(models.Model):
    _name='metge.hospital'

    nom = fields.Char(
        string='Nom',
        required=True,
        size=15
    )
    cognoms = fields.Char(
        string='Cognoms',
        required=True,
        size=20
    )
    numSegSocial = fields.Char(
        string ='Nº seguretat social',
        required=True,
        size=24
        )
    nif = fields.Char(
        string='Nif',
        required=True,
        size=9
        )
    telefon=fields.Char(
        string='Telefon',
        required=True,
        size=9
        )
    adreca= fields.Many2one(
        'adreca.hospital', 
        string='Adreca')