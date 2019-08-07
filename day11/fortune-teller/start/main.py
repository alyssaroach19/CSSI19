#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
import os
import random


def get_fortune():
    # Add a list of fortunes to the empty fortune_list array
    fortune_list=['A beautiful, smart, loving person will be coming your way',
     'A dubious friend may be an enemy in camoflage',
     'A faithful friend is a strong defense',
     'Life is just a trip, relax and have fun',
     'A fresh start will put you on your way',
    ]
    # Use the random library to return a random element from the array
    # instead of "None"
    i = random.randint(0, len(fortune_list)-1)
    random_fortune = fortune_list[i]
    return random_fortune


# Remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = "insert jinja2 environment variable here"

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        x = get_fortune()
        self.response.write(x)
    # Add a post method
    # def post(self):

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write( 'My response is Goodbye World')


# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    ('/bye', GoodbyeHandler)
], debug=True)
