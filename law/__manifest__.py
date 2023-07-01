# -*- coding: utf-8 -*-
{
    'name': "law",
    'category' : 'accounting/accounting',
    'summary': """Manage lawyers and customers""",
    'description': """
        lawyers module managing tasks of lawyers 
    """,
    'author': "Ahmed Nagy",
    'website': "http://www.yourcompany.com",
    'version': '0.1',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/lawyers_management.xml',
        'views/Customer_Management.xml',
        'views/inherit_sale.xml',
    ],
    'demo': []

}

