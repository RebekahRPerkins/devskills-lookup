from databases import Database

database = Database("sqlite:///app.db")

async def insert(ssn, customer):
	await database.connect()

	query = "INSERT INTO Customer(ssn, first, last, address, assessed_income, balance_of_debt, complaints) VALUES (:ssn, :first, :last, :address, :assessed_income, :balance_of_debt, :complaints)"
	values = [
		{"ssn": ssn, "first": customer['first_name'], "last": customer['last_name'], "address": customer['address'], "assessed_income": customer['assessed_income'], "balance_of_debt": customer['balance_of_debt'], "complaints": customer['complaints']}
	]
	await database.execute_many(query=query, values=values)

async def get1(s):
 	await database.connect()

 	query = "SELECT * FROM Customer WHERE ssn = '%s'" % s
 	print(query)

 	rows = await database.fetch_all(query=query)

 	return rows


