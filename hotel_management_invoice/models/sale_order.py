from odoo import models, fields, api
from datetime import datetime


class Sale_Order_Hotel(models.Model):
    _inherit = 'sale.order'

    booking_id = fields.Many2one('booking', string='Booking')

    @api.onchange('booking_id')
    def _onchange_booking_id(self):
        self.partner_id = self.booking_id.customer_id

    # @api.onchange('booking_id')
    # def _onchange_booking_id(self):
    #     if self.booking_id:
    #         # Clear existing services
    #         self.service_ids = [(5, 0, 0)]
    #         # Fetch services related to the selected booking
    #         services = self.env['service.model'].search([('booking_id', '=', self.booking_id.id)])
    #         self.service_ids = [(0, 0, {'service_name': service.name, 'price': service.price}) for service in services]

    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     """
    #     Override the `name_search` method to allow searching by customer name or room name.
    #     """
    #     args = args or []
    #     domain = args + ['|', ('customer_id.name', operator, name), ('room_name', operator, name)]
    #     bookings = self.env['your.booking.model'].search(domain, limit=limit)
    #     return bookings.name_get()