import requests

class Request:
		
	base_url = "";
	query_string = {}
	
	def make_request(self):
	
		r = requests.get(self.base_url, params=self.query_string)
		return r.json()