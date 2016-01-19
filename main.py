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

from google.appengine.api import users
from google.appengine.ext import ndb
import logging
import os
import jinja2

# import datastore1 as userDS
# import datastore2 as boopDS
# import datastore3 as messageInfoDS

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(open("index.html").read())

class SendNewMessageHandler(webapp2.RequestHandler):
    def get(self):
        userid = self.request.get('userid')
        recipientUserid = self.request.get('recipientUserid')
        message = self.request.get('message')

        userEntry = ndb.Key(urlsafe = self.request.get('id')).get()
        userEntry.numberSent += 1
        recipientEntry = ndb.Key(urlsafe = self.request.get('id')).get()
        # 

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/send', SendNewMessageHandler),
], debug=True)
