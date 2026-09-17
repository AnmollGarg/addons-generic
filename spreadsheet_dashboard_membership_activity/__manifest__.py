# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Spreadsheet dashboard for membership activity",
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Spreadsheet',
    'description': 'Spreadsheet',
    'depends': ['spreadsheet_dashboard','spreadsheet_dashboard_membership','membership_activity', 'membership'],
    'data': [
        "data/dashboards.xml",
    ],
    'auto_install': ['membership'],
    'license': 'LGPL-3',
}
