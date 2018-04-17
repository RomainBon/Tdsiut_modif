# -*- coding: utf-8 -*-

from odoo import models, fields


class IutModelType(models.Model):
    _name = 'iut.model.type'
    # _sql_constraints = [
    #     ('name_unique', 'unique (name)', 'The ref is unique')
    # ]
    name = fields.Char(required="true")
    models_ids = fields.Many2many('iut.model', String='models')
