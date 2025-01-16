from odoo import models, fields, api


class Booking_Account_Move(models.Model):
    _inherit = 'account.move'

    hotel_customer = fields.Many2one('booking', string='Hotel Customer')
    duration = fields.Integer(string='Duration (Days)')

class Booking_Account_Move_Line(models.Model):
    _inherit = 'account.move.line'

    hotel_service_ids = fields.Many2one('hotel.service', string='Hotel Services')