# -*- coding: utf-8 -*-
# from odoo import http


# class Alex(http.Controller):
#     @http.route('/alex/alex/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alex/alex/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('alex.listing', {
#             'root': '/alex/alex',
#             'objects': http.request.env['alex.alex'].search([]),
#         })

#     @http.route('/alex/alex/objects/<model("alex.alex"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alex.object', {
#             'object': obj
#         })
