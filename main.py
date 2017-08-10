#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
import time
from google.appengine.api import users
from google.appengine.ext import ndb

class Street(ndb.Model):
    #  first = ndb.StringProperty(require=True)
    #  last = ndb.StringProperty(require=True)
     street = ndb.StringProperty(required=True)
     time = ndb.StringProperty(required=True)

# class CoordsRequest(ndb.Model):
#     lat = ndb.StringProperty(required = True)
#     lon = ndb.StringProperty(required = True)
#     timestamp = ndb.DateTimeProperty(auto_now_add = True)
#
# class AddressRequest(ndb.Model):
#     address = ndb.StringProperty(required = True)
#     timestamp = ndb.DateTimeProperty(auto_now_add = True)

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.path)
        logout_url = users.create_logout_url(self.request.path)

        context = {
            'user': user,
            'login_url': login_url,
            'logout_url': logout_url
        }

        template = jinja_environment.get_template('templates/frontpage.html')
        self.response.write(template.render(context))

class SecondHandler(webapp2.RequestHandler):
    def get(self):
        r_template = jinja_environment.get_template('templates/main-page.html')
        self.response.write(r_template.render())

    def post(self):
        street_name = self.request.get('street')
        time_lapse = self.request.get('time')
        #if
        my_neigh = Street(street=street_name, time= time_lapse)
        neigh_key = my_neigh.put()

        stuff = {
            'street_name' : street_name
        }

        logging.info(neigh_key.get().street)
        r_template = jinja_environment.get_template('templates/map-page.html')
        self.response.write(r_template.render(stuff))

# class RecordRequestHandler(webapp2.RequestHandler):
#     def post(self):
#         logging.info(self.request)
#         if self.request.get('type') == "coords":
#             new_record = CoordsRequest(lat = self.request.get('lat'),
#                                        lon = self.request.get('lon'))
#             new_record.put()
#         elif self.request.get('type') == "address":
#             new_address_record = AddressRequest(address = self.request.get('address'))
#             new_address_record.put()
#         else:
#             logging.error("Malformed Request!")

# class FourthHandler(webapp2.RequestHandler):
#     def get(self):
#         t_template = jinja_environment.get_template('templates/success.html')
#         self.response.write(t_template.render())

# class MainPage(ndb.Model):
    # name = ndb.StringProperty(required=True)
    # word = ndb.StringProperty(required=True)

# class FifthHandler(webapp2.RequestHandler):
#     def get(self):
        # user_name = self.request.get('user_name')
        # user_word = int(self.request.get('pass_word'))
        #
        # existing_user_query = MainPage.query(MainPage.name == user_name)
        # existing_user = existing_user_query.get()


        # m_template = jinja_environment.get_template('templates/main-page.html')
        # self.response.write(m_template.render())




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/main-page', SecondHandler)
    # ('/signup', ThirdHandler),
    # ('/success', FourthHandler),
    # ('/main-page', FifthHandler)

], debug=True)
