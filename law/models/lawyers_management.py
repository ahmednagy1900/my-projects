from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime, timedelta
from dateutil import relativedelta


class LaweyersManagement(models.Model):
    _name = 'lawyers'
    _description = 'lawyers management'

    name = fields.Char(strring='Name')
    age = fields.Integer(string='Age')
    # lawyer_id = fields.Many2one('res.users', string='Lawyer')
    # company_id = fields.Many2one('res.company', string='Company', related='lawyer_id.company_id', store=True)
    # currency_id = fields.Many2one('res.currency', string='Currency', related='company_id.currency_id')

    # _sql_constraints = [
    #     ('chck_name_field', '(1=1)', "name can not be duplicated"),
    # ]
    # _sql_constraints = [
    #     ('age_check', '(1=1)', "can not be less than 21 years "),
    # ]

# price = fields.Monetary(currency_field='currency_id', string='Price')
# date = fields.Date(string='Date Field', default=date.today())
# time = fields.Datetime(string='Datetime Field', default=datetime.now())
# age = fields.Integer(string='Age', compute='_compute_age', store=True)

# customer_id = fields.Many2one('customers', string='customer')
# refrence = fields.Reference(selection=[('res.company','company') , ('res.currency','currency')] , string='refrence')
# height = fields.Float(string='Height')
# customer_ids = fields.Many2many('customers', string='customer Many')
# customer_ids = fields.One2many('customers','lawyer_id', string='customer Many')


# @api.depends('date')
# def _compute_age(self):
#     for rec in self:
#         current_year = date.today()
#         if rec.date:
#             rec.age = current_year.year - rec.date.year
#         else:
#             rec.age = 1
#
# new_field = fields.char(string='New Field')
#
# ### basic fields type ###
#
# field02 = fields.Text(string='Text Field')
# field03 = fields.Selection([('male', 'Male'), ('female', 'Female')], string='selection Field')
# field04 = fields.Boolean(string='Boolean Field')
# field05 = fields.Html(string='Html Field')
# field06 = fields.Image(string='Image Field')
# field07 = fields.Binary(string='Binary Field')
# field08 = fields.Integer(string='Integer Field')
