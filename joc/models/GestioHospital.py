from odoo import models, fields, api

class GestioHospital:
	def __init__(self, nom, metges, adreca, pacients, malalties, historials):
		self.nom = nom
		self.metges = metges
		self.adreca = adreca
		self.pacients = pacients
		self.malalties = malalties
		self.historials = historials