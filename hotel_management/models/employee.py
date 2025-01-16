from odoo import models, fields, api


class Employees(models.Model):
    _inherit = 'hr.employee'

    hotel_id = fields.Many2one('hotel', string="Hotel",
                               domain="[('manager_id', '=', parent_id)]")
    hotel_manage_ids = fields.One2many('hotel', 'manager_id', string="Manage hotels")