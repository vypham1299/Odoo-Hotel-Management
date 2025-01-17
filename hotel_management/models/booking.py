from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Booking(models.Model):
    _name = 'booking'
    _description = 'Booking rooms'
    _sql_constraints = [
        ('id_unqiue', 'UNIQUE(id)', 'The id must be unique.'),
    ]

    booking_id = fields.Char(string='Order Number', required=True)
    date = fields.Datetime(required=True, default=fields.Datetime.now)
    check_in = fields.Datetime(string='Check-In', required=True)
    check_out = fields.Datetime(string='Check-Out', required=True)
    is_booked = fields.Selection(
        [('new', 'New'), ('booked', 'Booked')],
        string='Is Booked',
        default='new',
        required=True
    )

    hotel_address = fields.Text()

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    hotel_id = fields.Many2one('hotel', string='Hotel', required=True)
    bed_type = fields.Selection(
        [('single', 'Single'), ('double', 'Double')],
        string='Bed Type',
        required=True
    )
    room_id = fields.Many2one('room', string='Room', 
                              domain="[('hotel_id', '=', hotel_id), ('is_available', '=', True), ('bed_type', '=', bed_type)]", 
                              required=True)
    service_ids = fields.Many2one('hotel.service', string='Hotel Services',
                                  domain="[('hotel_id', '=', hotel_id)]")
    account_move_id = fields.Many2one('account.move', string='Booking Invoice')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.room_id.room_id} - {record.customer_id.name}"
            result.append((record.id, name))
        return result
    
    @api.constrains('check_in', 'check_out')
    def _check_dates(self):
        for record in self:
            if record.check_in and record.check_out:
                if record.check_in >= record.check_out:
                    raise ValidationError(
                        "Check-Out Date must be later than Check-In Date."
                    )
    
    @api.onchange('hotel_id')
    def _get_address(self):
        for record in self:
            record.hotel_address = record.hotel_id.address
    
    def is_booked_change(self):
        for record in self:
            record.is_booked = 'booked'
    
    def action_set_booked(self):
        for record in self:
            if record.is_booked == 'new':
                record.is_booked = 'booked'
