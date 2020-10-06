

from odoo import models, fields, api

class coop_socio_acc(models.Model):
    _inherit = 'res.partner'

    facturas = fields.One2many('account.invoice', 'partner_id', string="Facturas")