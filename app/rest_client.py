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

	def get_data(conn, url):
		conn.request("GET", url)
		res = conn.getresponse()
		data = res.read()
		return json.loads(data.decode('utf-8'))

	def get(ssn):
		conn = http.client.HTTPSConnection(BASE_URL)

		debt = get_data(conn, DEBT_URL % ssn) #balance_of_debt complaints
		assessed_income = get_data(conn, ASSESSED_INCOME_URL % ssn) #assessed_income
		personal_details = get_data(conn, PERSONAL_DETAILS_URL % ssn) #first_name last_name address
		#should after wiring up db, decide if I make a new python object and call its constructor or this dict
		customer = {}
		customer['balance_of_debt'] = debt['balance_of_debt']
		customer['complaints'] = debt['complaints']
		customer['assessed_income'] = assessed_income['assessed_income']
		customer['first_name'] = personal_details['first_name']
		customer['last_name'] = personal_details['last_name']
		customer['address'] = personal_details['address']

		conn.close()

		return customer
