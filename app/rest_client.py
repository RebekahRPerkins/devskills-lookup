import http.client
import json
import os

class RestClient:

	BASE_URL = "infra.devskills.app"
	DEBT_URL = "/api/credit-data/debt/%s"
	ASSESSED_INCOME_URL = "/api/credit-data/assessed-income/%s"
	PERSONAL_DETAILS_URL = "/api/credit-data/personal-details/%s"

	def __init__(
		self,
		logger
	):
		self.logger = None

	#fetch from external api
	def get(self, ssn):
		conn = http.client.HTTPSConnection(self.BASE_URL)

		debt = self.get_data(conn, self.DEBT_URL % ssn) #balance_of_debt complaints
		assessed_income = self.get_data(conn, self.ASSESSED_INCOME_URL % ssn) #assessed_income
		personal_details = self.get_data(conn, self.PERSONAL_DETAILS_URL % ssn) #first_name last_name address
		
		customer = self.map(debt, assessed_income, personal_details)

		conn.close()

		return customer

	def get_data(self, conn, url):
		conn.request("GET", url)
		res = conn.getresponse()
		data = res.read()
		return json.loads(data.decode('utf-8'))

	def map(self, debt, assessed_income, personal_details):
		customer = {}
		if 'error' not in debt:
			customer['balance_of_debt'] = debt['balance_of_debt']
			customer['complaints'] = debt['complaints']
			customer['assessed_income'] = assessed_income['assessed_income']
			customer['first_name'] = personal_details['first_name']
			customer['last_name'] = personal_details['last_name']
			customer['address'] = personal_details['address']
		return customer
