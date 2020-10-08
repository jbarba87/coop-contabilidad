from odoo import models, fields, api

class coop_cronograma(models.Model):
  _name = 'coop_contabilidad.cronograma'

  socio = fields.Many2one('res.partner', string="Socio")
  num_cuotas = fields.Integer(string="Numero de Cuotas")
  interes = fields.Float(string="Interes")
  monto = fields.Float(string="Monto")

  cuotas = fields.One2many('coop_contabilidad.cuota', 'cronograma_id', string="Cuotas")