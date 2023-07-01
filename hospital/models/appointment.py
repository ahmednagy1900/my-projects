from odoo import models, fields, api
from datetime import date, datetime, timedelta


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    days_of_doctor = fields.Text(string="days_of_doctor")
    time_of_doctor_work = fields.Text(string='time_of_doctor_work')



