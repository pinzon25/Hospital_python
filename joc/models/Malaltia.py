from odoo import models, fields, api
class Malaltia:
	def __init__(self, codi, nom, causaBaixa, tractament, duradaTractament):self.codi = codi
        self.nom = nom
        self.causaBaixa = causaBaixa
        self.tractament = tractament
        self.duradaTractament = duradaTractament
        def retornaCodiMalaltia(self):
            return codi

        def retornaNomMalaltia(self):
            return nom
        
        def retornacausaBaixaMalaltia(self):
            return causaBaixa

        def retornaTractamentMalaltia(self):
            return tractament

        def retornaduradaTractamentMalaltia(self):
            return duradaTractament