from odoo import models, fields, api

class coop_cuota(models.Model):
  _name = 'coop-contabilidad.cuota'


  fecha_venc = fields.Date(string="Fecha de Vencimiento")

  socio = fields.Char(string="Socio")
  num_cuota = fields.Integer(string="Numero de Cuota")
  interes = fields.Float(string="Interes")
  monto_cuota = fields.Float(string="Monto")

  cronograma_id = fields.Many2one('coop-contabilidad.cronograma', string="Cronograma" )