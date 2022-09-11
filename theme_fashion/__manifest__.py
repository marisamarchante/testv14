# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-Today Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>).
#    Author: Anil R. Kesariya(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Theme Fashion',
    'summary': 'Fashion E-commerce theme is a multi-page responsive theme.',
    'version': '14.0.0.1',
    'category': 'Theme/Ecommerce',
    'author': 'Jupical Technologies Pvt. Ltd.',
    'maintainer': 'Jupical Technologies Pvt. Ltd.',
    'contributors':['Anil Kesariya <anil.r.kesariya@gmail.com>'],
    'website': 'https://www.jupical.com',
    'live_test_url': 'https://www.youtube.com/watch?v=E0sPSH9IpCE',
    'depends': ['website_blog', 'website_crm', 'website_sale_wishlist', 'website_sale_stock', 'website_mass_mailing', 'website'],
    'data': [
        'template/assets.xml',
        'template/layout.xml',
        'template/homepage.xml',
        'template/about_page.xml',
        'template/portfolio_page.xml',
        'template/contact_page.xml',
        'template/privacy_policy.xml',
        'template/faq_page.xml',
        'template/blog_page_inherit.xml',
        'template/snippets.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'images': ['static/description/banner.gif', 'static/description/theme_screenshot.gif'],
    'price': 99.00,
    'currency': 'USD',
}
