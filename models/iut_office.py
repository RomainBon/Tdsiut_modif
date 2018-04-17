# -*- coding: utf-8 -*-

from odoo import models, fields


class IutOffice(models.Model):
    _name = 'iut.office'
    _inherit = 'res.partner'

    employee_nb = fields.Integer()
