import requests

class API():

	def __init__(self):
		self.method = ''
		self.url = ''

		self.params = None
		self.data = None
		self.json = None

		self.REQUESTS = {
			'GET': requests.get,
			'OPTIONS': requests.options,
			'HEAD': requests.head,
			'POST': requests.post,
			'PUT': requests.put,
			'PATCH': requests.patch,
			'DELETE': requests.delete,
		}

	def set_method(self, method):
		self.method = method

	def set_url(self, url):
		self.url = url

	def set_params(self, params):
		self.params = params

	def set_data(self, data):
		self.data = data

	def set_json(self, json):
		self.json = json

	def request(self, **kwargs):
		if self.method not in self.REQUESTS:
			return 'Error: method requests incompatible.'

		if self.url=='':
			return 'Error: URL doesn\'t exist.'

		return self.REQUESTS[self.method](self.url, params=self.params, data=self.data, json=self.json, **kwargs)