from databases import Database

database = Database("sqlite:///app.db")

async def insert(ssn, first, last, address, assessed_income, balance_of_debt, complaints):
	await database.connect()

	query = "INSERT INTO Customer(ssn, first, last, address, assessed_income, balance_of_debt, complaints) VALUES (:ssn, :first, :last, :address, :assessed_income, :balance_of_debt, :complaints)"
	values = [
		{"ssn": ssn, "first": first, "last": last, "address": address, "assessed_income": assessed_income, "balance_of_debt": balance_of_debt, "complaints": complaints}
	]
	await database.execute_many(query=query, values=values)

async def get1(s):
 	await database.connect()

 	query = "SELECT * FROM Customer WHERE ssn = %s" % s

 	rows = await database.fetch_all(query=query)

 	return rows


