# -*- coding : utf-8 -*-#
from odoo import models, fields, api, exceptions
from datetime import timedelta


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Name", required=True)
    title = fields.Char(string="Title")
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_title_check', 'check(1=1)',
         "the title of the course should be not be the description"),

        ('name_description_check', 'check(name!=descripton)',
         "the title of the course should be not be the description"),

        ('name_unique', 'unique(name)',
         "the course title must be unique")

    ]


# 'check(name!=descripton)',

# 'unique(name)',

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'open academy sessions'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    active = fields.Boolean(default=True)
    course_id = fields.Many2one('openacademy.course',
                                ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken Seats", compute='_taken_seats')
    end_date = fields.Date(string='End Date', store=True, compute='_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer(string="Attendees Count", compute='_get_attendees_count', store=True)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            r.duration = (r.end_date - r.start_date).days + 1

            #### graph depends function ####

    @api.depends('attendee_ids')
    def _attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "incorrect 'seats' value",
                    'message': "the number of seats may not  be negative",
                },

            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "increase seats or remove exces attendees",
                },

            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("asession instructor can`t be an attendee")

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for rec in self:
            rec.attendees_count = len(rec.attendee_ids)
