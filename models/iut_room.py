# -*- coding: utf-8 -*-

from odoo import models, fields


class IutRoom(models.Model):
    _name = 'iut.room'

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The name is unique')
    ]

    floor = fields.Char()
    name = fields.Char(required="true")
    id_room = fields.Many2one('iut.room', string='room')
