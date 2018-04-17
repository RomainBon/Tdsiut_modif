# -*- coding: utf-8 -*-

from odoo import models, fields
import erppeek


DATABASE = 'dip2'
SERVER = 'http://localhost:8069'
ADMIN_PASSWORD = 'admin'


class IutBrand(models.Model):
    _name = 'iut.brand'
    # _sql_constraints = [
    #     ('name_uniq', 'unique (name)', 'The name is unique')
    # ]

    name = fields.Char(required="true", index="true")
    warranty_delay_month = fields.Integer()
    support_phone = fields.Integer()

