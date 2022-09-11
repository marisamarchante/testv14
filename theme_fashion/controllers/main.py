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

from odoo import http
from odoo.http import route, request


class JTAbout(http.Controller):
    @http.route('/aboutus', auth='public', type='http', website=True)
    def about(self, **kw):
        return http.request.render('theme_fashion.about_page')


class JTPortfolio(http.Controller):
    @http.route('/portfolio', auth='public', type='http', website=True)
    def portfolio(self, **kw):
        return http.request.render('theme_fashion.portfolio_page')


class JTContact(http.Controller):
    @http.route('/contactus', auth='public', type='http', website=True)
    def contact(self, **kw):
        return http.request.render('theme_fashion.contact_page')


class JTPrivacyPolicy(http.Controller):
    @http.route('/privacy-policy', auth='public', type='http', website=True)
    def privacypolicy(self, **kw):
        return http.request.render('theme_fashion.privacy_policy')


class JTFaq(http.Controller):
    @http.route('/FAQ', auth='public', type='http', website=True)
    def faq(self, **kw):
        return http.request.render('theme_fashion.faq_page')
