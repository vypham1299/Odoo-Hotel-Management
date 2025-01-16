from odoo import models, fields, api


class Room_2(models.Model):
    # _name = 'hotel.2'
    _inherit = 'room'
    _description = 'New Room with Extension'

    room_size = fields.Float(string="Room Size")
    capacity = fields.Integer(string="Capacity")
    smoking = fields.Boolean(string="Smoking")