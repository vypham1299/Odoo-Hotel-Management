from datetime import datetime, timedelta
from odoo import models, fields, api, exceptions

class Services(models.Model):
    _inherit = 'product.template'

    hotel_id = fields.Many2one('hotel', string='Hotel')