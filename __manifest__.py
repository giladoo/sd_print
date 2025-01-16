{
    'name': 'PDF Report Redirect',
    'version': '15.0.1.0.0',
    'category': 'Tools',
    'summary': 'Directly print reports from the browser',
    'description': """
        This module allows users to print reports directly from the browser and display the print dialog.
    """,
    'website': 'https://giladoo.com',
    'author': 'Arash Homayounfar',
    'depends': ['base', 'web',],
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'sd_print/static/src/js/action_service.js',
        ],
    },

    'installable': True,
    'application': False,
}
