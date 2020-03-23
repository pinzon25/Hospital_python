from odoo import models, fields, api
class Visita:
	def __init__(self, nomHospital, metges, adreca, pacients, malalties, historials):
		self.nomHospital = nomHospital
		self.metge = metge
		self.pacient = pacient
		self.malaltia = malaltia
		self.data = data

		def retornaNomHospitalVisita(self):
			return nomHospital

		def retornaMetgeVisita(self):
			return metge

		def retornaPacientVisita(self):
			return pacient

		def retornaMalaltiaVisita(self):
			return malaltia

		def retornaDataVisita(self):
			return data

		