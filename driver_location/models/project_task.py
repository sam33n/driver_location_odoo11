from odoo import api, fields, models, tools

class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    vehicle_model = fields.Char('Model Name')
    license_plate = fields.Char('License Plate')
    source_date = fields.Datetime('Source Date')
    destination_date = fields.Datetime('Destination Date')