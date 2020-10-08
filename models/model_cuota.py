from odoo import models, fields, api

class coop_cuota(models.Model):
  _name = 'coop_contabilidad.cuota'


  fecha_venc = fields.Date(string="Fecha de Vencimiento")

  socio = fields.Char(string="Socio")
  num_cuota = fields.Integer(string="Numero de Cuota")
  interes = fields.Float(string="Interes")
  monto_cuota = fields.Float(string="Cuota")
  monto_abonado = fields.Float(string="Abono")

  estado = fields.Selection([
    ('pendiente', 'Pendiente de pago'),
    ('pagada', 'Pagada'),
    ('vencida', 'Vencida')
  ], default='pendiente')


  factura_id = fields.Many2one('account.invoice', string="Factura" )

  