import http.client
import json
import os

def get(ssn):
	conn = http.client.HTTPSConnection('infra.devskills.app')

	debt = get_data(conn, "/api/credit-data/debt/%s" % ssn) #balance_of_debt complaints
	assessed_income = get_data(conn, "/api/credit-data/assessed-income/%s" % ssn) #assessed_income
	personal_details = get_data(conn, "/api/credit-data/personal-details/%s" % ssn) #first_name last_name address
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

def get_data(conn, url):
	conn.request("GET", url)
	res = conn.getresponse()
	data = res.read()
	return json.loads(data.decode('utf-8'))