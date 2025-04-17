
{
    'name': ' CUSTOMISATION',
    'version': '18.0.0.10',
    'summary': 'This Module for AIED customisations',
    'description': """ This Module for AIED customisations.
    """,
    'category':'CRM',
    'author': ' ZestyBeanz Technologies',
    'website': 'www.zbeanztech.com',
    "license": "LGPL-3",
    'depends': [],
    'data': [
		'security/ir.model.access.csv',
 
            'security/security.xml',
 
            'views/model_one_view.xml',
 

            'views/car_rental_views.xml',
 
            'views/menu.xml'
 

        ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
