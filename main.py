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

# from person import Person

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/frontpage.html')
        self.response.write(template.render())
#     def post(self):
#
# class SecondHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template('templates/sign-in.html')
#         self.response.write(template.render())
# class ThirdHandler(webapp2.RequestHandler):
#     def get(self):
# class FourthHandler(webapp2.RequestHandler):
#     def get(self):
#         # change the template html
#         main_template = jinja_environment.get_template('templates/sign-in.html')
#         self.response.write(main_template.render())
#     def post(self):
#         p_email = self.request.get('personemail')
#         p_pass = self.request.get('personpass')
#
#         my_person = Person(email = p_email, password = p_p_pass)
#
#         person_key = my_person()
#         logging.info(person_key.get().name)
#
#         results_template = jinja_environment.get_template('templates/results.html')
#         self.response.write(results_template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
