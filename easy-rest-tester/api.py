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

		self.response = None

	def get_methods(self):
		return tuple(self.REQUESTS.keys())

	def set_method(self, method):
		self.method = method

	def set_url(self, url):
		self.url = url

	def set_parameters(self, params):
		self.params = params

	def set_data(self, data):
		self.data = data

	def set_json(self, json):
		self.json = json

	
	def send_request(self, **kwargs):
		self.response = self.get_response(**kwargs)


	def get_response(self, **kwargs):
		if self.method not in self.REQUESTS:
			return 'Error: method requests incompatible.'

		try:
			return self.REQUESTS[self.method](self.url, params=self.params, data=self.data, json=self.json, **kwargs)
		except:
			return 'Error: URL doesn\'t exist.'

	def get_body_response(self):
		if type(self.response)==str:
			return self.response
		return self.response.text

	def get_headers_response(self):
		if type(self.response)==str:
			return self.response
		return self.response.headers

	def get_url(self):
		return self.response.url