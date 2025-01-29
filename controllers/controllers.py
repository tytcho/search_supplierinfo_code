# -*- coding: utf-8 -*-
# from odoo import http


# class SearchSupplierinfoCode(http.Controller):
#     @http.route('/search_supplierinfo_code/search_supplierinfo_code', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/search_supplierinfo_code/search_supplierinfo_code/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('search_supplierinfo_code.listing', {
#             'root': '/search_supplierinfo_code/search_supplierinfo_code',
#             'objects': http.request.env['search_supplierinfo_code.search_supplierinfo_code'].search([]),
#         })

#     @http.route('/search_supplierinfo_code/search_supplierinfo_code/objects/<model("search_supplierinfo_code.search_supplierinfo_code"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('search_supplierinfo_code.object', {
#             'object': obj
#         })
