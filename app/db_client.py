from databases import Database

class DatabaseClient:
	database = Database("sqlite:///app.db")
	select_query = "SELECT * FROM Customer WHERE ssn = '%s'"

	def __init__(
		self,
		logger
	):
		self.logger = None

	async def insert(self, ssn, customer):
		await self.database.connect()

		query = "INSERT INTO Customer(ssn, first, last, address, assessed_income, balance_of_debt, complaints) VALUES (:ssn, :first, :last, :address, :assessed_income, :balance_of_debt, :complaints)"
		values = [
			{"ssn": ssn, "first": customer['first_name'], "last": customer['last_name'], "address": customer['address'], "assessed_income": customer['assessed_income'], "balance_of_debt": customer['balance_of_debt'], "complaints": customer['complaints']}
		]
		await self.database.execute_many(query=query, values=values)

	async def get(self, s):
	 	await self.database.connect()

	 	query = self.select_query % s
	 	
	 	rows = await self.database.fetch_all(query=query)

	 	return rows
