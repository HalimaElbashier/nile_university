from odoo import models, fields, api

class StudentBatchWizard(models.TransientModel):
    _name = 'school_management.student_batch_wizard'
    _description = 'Student Batch Wizard'

    batch_id = fields.Many2one('school_management.batch', string='Batch', required=True)
    student_ids = fields.Many2many('school_management.student', string='Students')

    @api.multi
    def assign_students_to_batch(self):
        self.ensure_one()
        for student in self.student_ids:
            student.batch_id = self.batch_id
