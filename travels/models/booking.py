from odoo import models, fields

class TravelBooking(models.Model):
    _name = 'travel.booking'
    
    customer_name = fields.Char('Customer Name', required=True)
    destination = fields.Char('Destination', required=True)
    travel_date = fields.Date('Travel Date')
    is_confirmed = fields.Boolean('Confirmed')