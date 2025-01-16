from odoo import models, fields, api
from datetime import datetime


class Booking_Invoice(models.Model):
    _inherit = 'booking'

    sale_order_ids = fields.One2many('sale.order', 'booking_id')

    @api.model
    def create(self, vals):
        booking = super(Booking_Invoice, self).create(vals)

        # Calculate night
        delta = fields.Datetime.from_string(booking.check_out) - fields.Datetime.from_string(booking.check_in)
        durartion = delta.total_seconds() / (24 * 3600)  # Convert seconds to days

        # Automatically create invoice
        invoice_vals = {
            'hotel_customer': booking.customer,
            'duration': durartion,
            'move_type': 'out_invoice',
            'invoice_date': booking.date,
            # 'invoice_line_ids': [(0, 0, {
            #     'product_id': booking.hotel_id.product_id.id,
            #     'quantity': 1,
            #     'price_unit': booking.total_price,
            # })],
        }
        invoice = self.env['account.move'].create(invoice_vals)
        booking.invoice_id = invoice.id
        return booking