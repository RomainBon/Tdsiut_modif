# -*- coding: utf-8 -*-

from odoo import models, fields


class IutModel(models.Model):
    _name = 'iut.model'
    # _sql_constraints = [
    #     ('ref_uniq', 'unique (ref)', 'The ref is unique')
    # ]
    name = fields.Char(required="true")
    ref = fields.Char(index='True')
    type_ids = fields.Many2many('iut.model.type')
    id_brand = fields.Many2one('iut.brand', string='brand')


