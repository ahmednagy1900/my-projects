# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': """Manage patients and doctors relation""",

    'description': """
        hospital module that control on all things inside hospital clinics
    """,

    'author': "Ahmed Nagy",
    'sequence': -100,
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/appointment.xml',
        'views/hospital.xml',
        'security/ir.model.access.csv'

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
}
