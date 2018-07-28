# -*- coding: utf-8 -*-
{
    'name': "code_building_block",

    'summary': """
        Module to create building blocks with code formatting support""",

    'description': """
       Module to create building blocks with code formatting support
       Minimal case:
       <pre><code class="python hljs">
            class AModel(models.Model):
            _name = 'a.model'
            description = fields.Char(string='Description')
        
            @api.multi
            def a_method(self):
                self.description = 'some description'
        </code></pre>
    """,

    'author': "Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
    ],
}
