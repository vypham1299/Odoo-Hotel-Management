from odoo import models, fields, api
from datetime import datetime, timedelta
import logging

# Configure logger to write to a file
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logfile.log')  # Replace with your desired file path
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Room(models.Model):
    _name = 'room'
    _description = 'List rooms'
    _sql_constraints = [
        ('id_unique', 'UNIQUE(room_id)', 'The id must be unique.'),
    ]

    room_id = fields.Char(string='Room Number', required=True)
    bed_type = fields.Selection(
        [('single', 'Single'), ('double', 'Double')],
        string='Bed Type',
        required=True
    )
    price_per_night = fields.Float(string='Price Per Night', required=True)
    is_available = fields.Boolean(string='Is Available', default=True)
    latest_booked = fields.Datetime(string='Latest Booked')

    hotel_id = fields.Many2one('hotel', string='Hotel', required=True)
    detail_ids = fields.Many2many('room.detail')
    booking_ids = fields.One2many('booking', 'room_id')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.room_id} - {record.hotel_id.hotel_id}"
            result.append((record.id, name))
        return result

    def check_rooms_not_booked(self):
        """This method checks for rooms that have not been booked in the last 7 days."""
        print('runnnnnnnnnnnnnnnnn')
        today = datetime.today().date()
        logger.info("Today's date: %s", today)
        date_seven_days_ago = today - timedelta(days=7)

        # Search for rooms that have not been booked in the last 7 days
        rooms = self.env['room'].search([
            ('latest_booked', '<', date_seven_days_ago)
        ])

        # Loop through the rooms and log their information
        for room in rooms:
            print(f"Room: {room.room_id}, Hotel: {room.hotel_id.hotel_id}, Last Booked Date: {room.latest_booked}")
