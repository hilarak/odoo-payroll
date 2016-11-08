# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2016- Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
'name': 'Payroll Employee Fund',
'version': '0.1',
'summary': 'Extends hr.contract with an analytic account for a fund',
'category': 'hr',
'description': """Extends the Employee Contract with an analytic account to be used as a fund. 

""",
'author': 'Vertel AB',
'website': 'http://www.vertel.se',
'depends': ['hr_payroll'],
'data': ['payslip_view.xml'],
'installable': True,
}