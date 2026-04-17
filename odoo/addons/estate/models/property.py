# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Property(models.Model):
    _name = 'estate.property'
    _description = 'This is the property model'


    name = fields.Char(string="Property", required=True)
    description = fields.Text(string="Description", required=True)
    postcode = fields.Char(string="Postal code", required=True)
    date_availability = fields.Date(string="Availability From", required=True)
    expected_price = fields.Float(string="Expected Price", required=True, digits=(6,2))
    selling_price = fields.Float(string="Selling Price", required=True, readonly=True, digits=(6,2))
    bedrooms = fields.Integer(string="Number of Bedrooms", required=True, default=2 )
    living_area = fields.Integer(string="Living Area (sqm)", required=True)
    facades = fields.Integer(string="Facades", required=True)
    garage = fields.Boolean(string="Garage", required=True, default=False)
    garden = fields.Boolean(string="Garden Area (sqm)", required=True, default=False)
    garden_area = fields.Integer(string="Garden area (sqm)", required=True)
    garden_orientation =fields.Selection(string="Garden Orientation",
                                         default="east",
                                         required=True,
                                         selection=[('east', 'East'), 
                                                    ('west', 'West'),
                                                    ('south', 'South'),
                                                    ('north', 'North')])
    active = fields.Boolean(string="Active")
    state = fields.Selection(string="Status", 
                             default="new",
                             required=True,
                             selection=[('new', 'New'), 
                                        ('offer received', 'Offer Received'),
                                        ('offer accepted', 'Offer Accepted'),
                                        ('sold', 'Sold'),
                                        ('cancelled', 'Cancelled')])
    
    


