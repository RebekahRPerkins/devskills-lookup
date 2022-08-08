import unittest
import asyncio
from rest_client import RestClient
from db_client import DatabaseClient

#get from database. if it returns no record get from external api and insert
async def get(ssn, db_client, rest_client):
    customer = await db_client.get(s=ssn)
    if len(customer) == 0:
        customer = rest_client.get(ssn=ssn)
        if customer:
            await db_client.insert(ssn=ssn, customer=customer)

    return customer

#there are many reasons to not include a unit test in the source code file.
class TestCustomerLookupMethods(unittest.TestCase):
    def test_return_credit_data_response_when_db_returns_None(self):
        rest_client = RestClient(logger = None)
        db_client = DatabaseClient(logger = None)
        db_client.select_query = "SELECT * FROM Customer WHERE ssn = '%s' LIMIT 0"

        actual = asyncio.run(get("424-11-9327", db_client, rest_client))

        self.assertTrue(actual)
        self.assertTrue('first_name' in actual)
        self.assertEqual(actual['first_name'], 'Emma')

if __name__ == '__main__':
    unittest.main()