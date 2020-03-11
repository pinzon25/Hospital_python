# -*- coding: utf-8 -*-

from odoo import models, fields, api
class joc(models.Model):
    _name = 'joc.carta'
    id_carta=fields.Integer(
        string='codi de la carta'
    )
    nom=fields.Char(
        string='Nom de la carta',
        required=True,
        size=15
    )
    victories=fields.Integer(
        string='Quantitat de victories',
        required=True,
        size=20
    )
    descripcio=fields.Char(
        string='Descripció de la carta',
        required=True,
        size=64
    )
    