# Copyright 2016 Google Inc.
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

import webapp2

form="""
<form method="post">
	What is your birthday?
	<br>
	<label>
		Month 
		<input type="text" name="month" ">
	</label>
	<label>
		Day 
		<input type="text" name="day" ">
	</label>
	<label>
		Year 
		<input type="text" name="year" ">
	</label>
	<div></div>
	<input type="submit" name="">

</form>

"""


class MainPage(webapp2.RequestHandler):
#	def write_form(self, error="", month="", day="", year=""):
	#	self.response.out.write(form % {"error": error,
	#									"month": month,
	#									"day": day,
	#									"year": year})
 #   def get(self):
      #  self.response.headers['Content-Type'] = 'text/plain'
     #   self.response.out.write(form)
  #  def post(self):
    #	user_month = valid_month(self.request.get('month'))
    #	user_day = valid_day(self.request.get('day'))
    #	user_year = valid_year(self.request.get('year'))

    #	if not (user_month and user_day and user_year):
    #		self.response.out.write(form)
    #	else:
    #		self.response.out.write("thanks!  that's a valid day")	

    #	self.response.out.write("thanks!  That's a totally valid day")
    
   # def valid_month(month):
    #	if month:
    #		cap_month = month.capitalize()
    #		if cap_month in months:
    #			return cap_month	
    #def valid_year(year):
    #	if year and year.isdigit():
     #   	year = int(year)
      #  if year >= 1900 and year <= 2020:
       #     return year
    #def valid_day(day):
    #	if day <= 31 & day > 0:
     # 		print day
    #	if day > 31 | day <  0: 
     #   	print none


class TestHandler(webapp2.RequestHandler):
	def post(self):
		#q = self.request.get("q")
		#self.response.out.write(q)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage), ('/testform', TestHandler)
], debug=True)
