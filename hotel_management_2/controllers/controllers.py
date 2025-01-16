# -*- coding: utf-8 -*-
# from odoo import http


# class HotelManagement2(http.Controller):
#     @http.route('/hotel_management_2/hotel_management_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_management_2/hotel_management_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_management_2.listing', {
#             'root': '/hotel_management_2/hotel_management_2',
#             'objects': http.request.env['hotel_management_2.hotel_management_2'].search([]),
#         })

#     @http.route('/hotel_management_2/hotel_management_2/objects/<model("hotel_management_2.hotel_management_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_management_2.object', {
#             'object': obj
#         })
