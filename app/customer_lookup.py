import db_client
import unittest
import asyncio
from rest_client import RestClient
from unittest.mock import MagicMock

async def get2(ssn):
    customer = await db_client.get1(ssn)
    print("=================From db:============")
    print(customer)#[(1, '424-11-9327', 'Emma', 'Gautrey', '9896 Westend Terrace', 60668, 11585, 1)] 
    if len(customer) == 0:
        print("=========getting from external api============")
        rest_client = RestClient()
        customer = rest_client.get(ssn)
        print(customer)
        await db_client.insert(ssn, customer)

    return customer


#the plan here is to mock the 2 client module methods, so they return values based on the input
#there are many reasons to not include a unit test in the source code file.

class TestCustomerLookupMethods(unittest.TestCase):
    def test_return_credit_data_response_when_not_in_db(self):
        mock_db = MagicMock(db_client.get1)
        mock_db["424-11-9327"] = 'fish'
        actual = asyncio.run(get2("424-11-9327"))
        #expected = '[{"id":1,"ssn":"424-11-9327","first":"Emma","last":"Gautrey","address":"9896 Westend Terrace","assessed_income":60668,"balance_of_debt":11585,"complaints":1}]'
        expected = "fish"
        self.assertEqual(actual, expected)

    # def test_return_db_record(self):
    #     expected = '[{"id":1,"ssn":"424-11-9327","first":"Emma","last":"Gautrey","address":"9896 Westend Terrace","assessed_income":60668,"balance_of_debt":11585,"complaints":1}]'
    #     self.assertEqual('foo'.upper(), 'FOO')

    def test_error(self):
        self.assertEqual('foo'.upper(), 'FOO')

# python3 test_customer_lookup.py
if __name__ == '__main__':
    unittest.main()