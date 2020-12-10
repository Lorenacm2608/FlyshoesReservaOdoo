# -*- coding: utf-8 -*-
from odoo import http

# class Flyshoesreserva(http.Controller):
#     @http.route('/flyshoesreserva/flyshoesreserva/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flyshoesreserva/flyshoesreserva/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('flyshoesreserva.listing', {
#             'root': '/flyshoesreserva/flyshoesreserva',
#             'objects': http.request.env['flyshoesreserva.flyshoesreserva'].search([]),
#         })

#     @http.route('/flyshoesreserva/flyshoesreserva/objects/<model("flyshoesreserva.flyshoesreserva"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flyshoesreserva.object', {
#             'object': obj
#         })