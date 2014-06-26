#
# Http client
#

import urllib.parse
import httplib2

class HttpClient:
	'''Http client'''
	def __init__(self):
		self.http = httplib2.Http()

	@classmethod
	def getHeaders(cls):
		return {}

	def request(self, url, headers, formData):
		return self.http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(formData))


# create httpclient instance
httpClient = HttpClient()
def getHtppClient():
	return httpClient