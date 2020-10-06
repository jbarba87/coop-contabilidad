# -*- coding: utf-8 -*-
from odoo import http

# class Coop-contabilidad(http.Controller):
#     @http.route('/coop-contabilidad/coop-contabilidad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coop-contabilidad/coop-contabilidad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coop-contabilidad.listing', {
#             'root': '/coop-contabilidad/coop-contabilidad',
#             'objects': http.request.env['coop-contabilidad.coop-contabilidad'].search([]),
#         })

#     @http.route('/coop-contabilidad/coop-contabilidad/objects/<model("coop-contabilidad.coop-contabilidad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coop-contabilidad.object', {
#             'object': obj
#         })