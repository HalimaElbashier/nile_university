from odoo import models, fields, api

class Student(models.Model):
    _name = 'school_management.student'
    _description = 'Student'

    name = fields.Char(string='res.partner', required=True)
    age = fields.Integer(string='Age')
    batch_id = fields.Many2one('school_management.batch', string='Batch')


