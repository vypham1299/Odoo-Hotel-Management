# -*- coding: utf-8 -*-
# from odoo import http


# class HotelManagement(http.Controller):
#     @http.route('/hotel_management/hotel_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_management/hotel_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_management.listing', {
#             'root': '/hotel_management/hotel_management',
#             'objects': http.request.env['hotel_management.hotel_management'].search([]),
#         })

#     @http.route('/hotel_management/hotel_management/objects/<model("hotel_management.hotel_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_management.object', {
#             'object': obj
#         })
