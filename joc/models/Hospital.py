from odoo import models, fields, api
class Hospital:
	def __init__(self, nom, metges, adreca, pacients, malalties, historials):
		self.nom = nom
		self.metges = metges
		self.adreca = adreca
		self.pacients = pacients
		self.malalties = malalties
		self.historials = historials

		def retornaNomHospital(self):
			return nom

		def retornaMetgesHospital(self):
			return metges

		def retornaAdrecaHospital(self):
			return adreca

		def retornaPacientsHospital(self):
			return pacients

		def retornaMalaltiesHospital(self):
			return malalties

		def retornaHistorialsHospital(self):
			return historials