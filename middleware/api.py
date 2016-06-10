import hashlib
import json
import logging

import webapp2


class MainHandler(webapp2.RequestHandler):

    def post(self):
        request_body




app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)