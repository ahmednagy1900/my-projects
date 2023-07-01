from odoo import models, fields, api


class CustomersManagement(models.Model):
    _name = 'customers'
    _description = 'Customer Management'
    # _inherits = {'lawyers': 'lawyer_model_id'}

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    # date = fields.Date(string='date')
    # lawyer_model_id = fields.Many2one('lawyers', string='Lawyers')
    # reserved names in fields #####
    # active = fields.Boolean(string= 'Active')
    # another_boolean = fields.Boolean(string='Another_boolean')
    ###enviroment record###
    # created_by_id=fields.Many2one('res.user',string= 'Created_By')

####  recordset example ####
# def compute_age(self):
#     for rec in self:
#         print (">>>>>>>>",rec)


#### environment example ####
# def create_record(self):
#     for rec in self:
#         rec.created_by_id=self.env.user
#
# print (">>>>>>>>>>>>>",self.env.user)


# lawyer_id=fields.Many2one('lawyers')

# @api.Constrsins(age)
# def check_age(self):
#     if self.age < 21:
#         raise ValidationError(_('Age can not be less than required 21'))
