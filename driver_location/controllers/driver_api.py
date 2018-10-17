# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import OrderedDict
from operator import itemgetter

from odoo import http, _
from odoo.http import request
from odoo.tools import groupby as groupbyelem
import json
from odoo.osv.expression import OR


class DriverApi(http.Controller):
	@http.route(['/api/driver_location/'],type='json',auth='user')
	def driver_location_create(self,task_id,emp_id,lon,lat):
		#print(request.session())
		print(request.env['ir.http'].session_info()['session_id'])
		print(request.httprequest.headers['session_id'])
		driver_location_created = request.env['driver.location'].create({
    		'task_id':task_id,
    		'emp_id':emp_id,
    		'lon':lon,
    		'lat':lat
    		})
		return driver_location_created
