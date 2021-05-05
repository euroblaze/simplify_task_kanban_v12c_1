# -*- coding: utf-8 -*-
{
    'name': "simplify_task_kanban_v12c_1",

    'summary': """
        Hide Add a Column button on Project Task Kanban View.
    """,

    'description': """
        Hide the button for adding a new column for users, 
        allow access only to the users that have an option to activate the developer/debug mode.
    """,

    'author': "Bojan Anchev",
    'website': "m102@simplify-erp.com",
    'category': 'Project, Task Stage/Type',
    'version': '1.0',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
