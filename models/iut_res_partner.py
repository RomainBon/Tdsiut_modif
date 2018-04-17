# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    employee_ref = fields.Char()
    device_ids = fields.One2many('iut.device', 'id_partner')
