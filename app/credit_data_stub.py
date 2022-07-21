import rest_client
import db_client

async def get2(ssn):
    customer = await db_client.get1(ssn)
    print("=================From db:============")
    print(customer)
    if len(customer) == 0:
        print("=========getting from external api============")
        customer = rest_client.get(ssn)
        print(customer)
        await db_client.insert(ssn, customer)

    return customer