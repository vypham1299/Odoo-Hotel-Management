from odoo import models, fields

class Room_detail(models.Model):
    _name = 'room.detail'

    content = fields.Text(required=True)
    room_ids = fields.Many2many('room', 'detail_ids')