from odoo import models, fields, api
from datetime import date, datetime, timedelta


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital patient details"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    status = fields.Text(string="Status")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor of this patient")


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "hospital doctor details"
    _inherits = {'hospital.patient': 'patient_id'}

    name = fields.Char(string="Name")
    specialist = fields.Text(string="Specialist")
    doctor_times = fields.Datetime(string="Doctor_Times")
    doctor_department = fields.Text(string="Department")
    patient_ids = fields.One2many('hospital.patient', 'doctor_id', string="doctor Patients")
    status = fields.Text(string="Status")
    patient_id = fields.Many2one('hospital.patient', string="Patient")
