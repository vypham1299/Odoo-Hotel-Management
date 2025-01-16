# -*- coding: utf-8 -*-
# from odoo import http


# class HotelManagementInvoice(http.Controller):
#     @http.route('/hotel_management_invoice/hotel_management_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_management_invoice/hotel_management_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_management_invoice.listing', {
#             'root': '/hotel_management_invoice/hotel_management_invoice',
#             'objects': http.request.env['hotel_management_invoice.hotel_management_invoice'].search([]),
#         })

#     @http.route('/hotel_management_invoice/hotel_management_invoice/objects/<model("hotel_management_invoice.hotel_management_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_management_invoice.object', {
#             'object': obj
#         })
