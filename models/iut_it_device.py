# -*- coding: utf-8 -*-

from odoo import models, fields


class IutDevice(models.Model):
    _name = 'iut.device'

    name = fields.Char(required="true")
    date_allocation = fields.Date()
    value = fields.Integer()
    serial_number = fields.Char(required="true")
    date_purchase = fields.Date()
    date_warranty_ent = fields.Date(on_change='on_change')
    id_partner = fields.Many2one('res.partner', String='Partner')
    id_model = fields.Many2one('iut.model', string="Model")
    #room_id
    #office_id


def on_change():
    pass
