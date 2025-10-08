# -*- coding: utf-8 -*-
{
    'name': 'Library Extensions',
    'version': '17.0.1.0',
    'category': 'Extra Tools',
    'summary': 'Adds author and category to books',
    'depends': ['library'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_book_category_views.xml',
    ],
    'installable': True,
    'application': False,
}

