# -*- coding: utf-8 -*-
from openerp import http

# class ClubBasquet(http.Controller):
#     @http.route('/club_basquet/club_basquet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/club_basquet/club_basquet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('club_basquet.listing', {
#             'root': '/club_basquet/club_basquet',
#             'objects': http.request.env['club_basquet.club_basquet'].search([]),
#         })

#     @http.route('/club_basquet/club_basquet/objects/<model("club_basquet.club_basquet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('club_basquet.object', {
#             'object': obj
#         })