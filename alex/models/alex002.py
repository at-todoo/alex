# -*- coding: utf-8 -*-

from odoo import models, fields


class alex002(models.Model):
     _name = 'alex002.alex002'
     _description = 'alex002.alex002'

     Nombre = fields.Char()
     Valor = fields.Integer()
     Cantidad = fields.Float(compute="_value_pc", store=True)
     DEscripcion = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
