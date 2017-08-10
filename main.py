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
from google.appengine.api import users
from google.appengine.ext import ndb

class Street(ndb.Model):
     email = ndb.StringProperty(required=True)
     password = ndb.StringProperty(required=True)
     repassword = ndb.StringProperty(required=True)

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

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

# class ThirdHandler(webapp2.RequestHandler):
#     def get(self):
#         s_template = jinja_environment.get_template('templates/signup.html')
#         self.response.write(s_template.render())
#     def post(self):
#         p_email = self.request.get('emails')
#         p_pass = self.request.get('psw')
#         p_repass = self.request.get('psw-repeat')
#
#         my_person = Person(email = p_email, password = p_pass, repassword = p_repass)
#
#         person_key = my_person.put()
#         logging.info(person_key.get().email)
#
        # results_template = jinja_environment.get_template('templates/.html')
        # self.response.write(results_template.render())
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
