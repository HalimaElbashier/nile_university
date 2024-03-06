from odoo import models, fields, api

class Batch(models.Model):
    _name = 'school_management.batch'
    _description = 'Batch'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    student_ids = fields.One2many('school_management.student', 'batch_id', string='Students')

