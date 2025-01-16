from datetime import datetime, timedelta
from odoo import models, fields, api, exceptions

class Hotels(models.Model):
    _name = 'hotel'
    _description = 'List hotels'
    _sql_constraints = [
        ('id_unique', 'UNIQUE(hotel_id)', 'The id must be unique.'),
    ]

    hotel_id = fields.Char(required=True)
    address = fields.Char(required=True)
    floors = fields.Integer(required=True)
    
    rooms = fields.Integer(compute='_compute_rooms', store=True)
    available_rooms = fields.Integer(compute='_compute_available_rooms')
    
    room_ids = fields.One2many('room', 'hotel_id')
    booking_ids = fields.One2many('booking', 'hotel_id')
    service_ids = fields.One2many('product.template', 'hotel_id')
    
    manager_id = fields.Many2one('hr.employee', string="Manager", required=True)
    employee_ids = fields.One2many('hr.employee', 'hotel_id', string="Employee")
                                    # domain="[('parent_id', '=', manager_id)]")

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.hotel_id} - {record.address}"
            result.append((record.id, name))
        return result
    
    @api.depends('room_ids')
    def _compute_rooms(self):
        for record in self:
            record.rooms = len(record.room_ids)
    
    @api.depends('room_ids')
    def _compute_available_rooms(self):
        for record in self:
            if record.room_ids:
                record.available_rooms = len(record.room_ids.filtered(lambda r: r.is_available))
    
    @api.constrains('manager_id')
    def _check_manager_is_employee(self):
        for record in self:
            if not record.manager_id.user_id or not record.manager_id.user_id.has_group('hotel_management.group_manager'):
                raise exceptions.ValidationError(
                    "The selected manager must belong to the 'Hotel Manager' group."
                )

    def reduce_price_for_unbooked_rooms(self):
        # Get the date 10 days ago
        a_week_ago = datetime.now() - timedelta(weeks=7)
        # Search for rooms that haven't been booked in the last 7 days
        rooms = self.env['booking'].search([('check_out', '<', a_week_ago)])
        print(rooms)
        if rooms:
            for room in rooms:
                # Reduce the price (e.g., by 10%)
                room.price = room.price * 0.9

    @api.model_create_multi
    def create(self, vals_list):
        hotel = super(Hotels,self).create(vals_list)
        for vals in vals_list:
            manager = self.env['hr.employee'].browse(vals['manager_id'])
            if manager:
                manager.write({'hotel_manage_ids': [(4, hotel.id)]})
            else:
                raise exceptions.ValidationError(
                    "Cannot find the manager in system. Please create manager account first."
                )
            
            # Add hotel_id in model employee when add them in hotel form
            if 'employee_ids' in vals:
                for e in vals:
                    employee = self.env['hr.employee'].browse(e)
                    if employee:
                        employee.hotel_id = hotel.id
                    else: 
                        raise exceptions.ValidationError(
                            "Cannot find the manager in system. Please create manager account first."
                        )
        return hotel
    
    # def write(self, vals):
    #     if 'manager_id' in vals:
    #         old_manager = self.env['hr.employee'].browse(self.manager_id)
    #         manager = self.env['hr.employee'].browse(vals['manager_id'])
    #         if manager:
    #             old_manager.write({'hotel_manage_ids': [(3, self.id)]})
    #             manager.write({'hotel_manage_ids': [(4, self.id)]})
    #         else:
    #             raise exceptions.ValidationError(
    #                 "Cannot find the manager in system. Please create manager account first."
    #             )
    #     if 'employee_ids' in vals:
    #         for e in vals['employee_ids']:
    #             if e not in self.employee_ids:
    #                 new_e = self.env['hr.employee'].browse(e)
    #                 if new_e:
    #                     new_e.hotel_id = self.id
    #     hotel = super(Hotels,self).write(vals)
    #     return hotel

    # def unlink(self):
    #     for record in self:
    #         manager = self.env['hr.employee'].browse(record.manager_id.id)
    #         if manager:
    #             manager.hotel_manage_ids = hotel.id
    #         else:
    #             raise exceptions.ValidationError(
    #                 "Cannot find the manager in system. Please create manager account first."
    #             )
    #     hotel = super(Hotels,self).unlink()
    #     return hotel