from odoo import models, fields, api
class Malaltia(models.AbstractModel):
    _name='malaltia.pacient'

    codi=fields.Integer(
        string='Codi',
        required=True,
        )

    nom=fields.Char(
        string='Nom',
        )

    causaBaixa=fields.Boolean(
        string='Causa baixa',
        )

    tractament=fields.Char(
        string='Tractament',
        )

    duradaTractament=fields.Date(
        string='Durada tractament',
        )