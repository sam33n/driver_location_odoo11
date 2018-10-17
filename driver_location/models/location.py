from odoo import api, fields, models, _

class driver_location(models.Model):
    _name = "driver.location"

    task_id = fields.Many2one('project.task','Task Name')
    emp_id = fields.Many2one('res.partner','Employee Name')
    lon = fields.Float(
        string='Longitude',
        digits=(16, 5))
    lat = fields.Float(
        string='Latitude',
        digits=(16, 5))
    cell_tower = fields.Char('Cell Tower Detials')
    date_time = fields.Datetime('Date', required=True, default=fields.Datetime.now)



 
    