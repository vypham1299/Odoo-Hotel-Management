from odoo import models, fields, api


class Room_2(models.Model):
    _name = 'booking.history'
    _inherit = 'booking'
    _description = 'History'

    customer = fields.Char(string='Customer Name', required=True)
    date = fields.Datetime(required=True, default=fields.Datetime.now)
    check_in = fields.Datetime(string='Check-In', required=True)
    check_out = fields.Datetime(string='Check-Out', required=True)

    hotel_id = fields.Many2one('hotel', string='Hotel', required=True)
    bed_type = fields.Selection(
        [('single', 'Single'), ('double', 'Double')],
        string='Bed Type',
        required=True
    )
    room_id = fields.Many2one('room', string='Room', 
                              domain="[('hotel_id', '=', hotel_id), ('is_available', '=', True), ('bed_type', '=', bed_type)]", 
                              required=True)
