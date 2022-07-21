import rest_client
import db_client

async def get2(ssn):
    customer = await db_client.get1(ssn)
    # if customer is None:
    #     #do this again later with bad data, does it work
    #     print("None")
    # else:
    #     print("CUSTOMER!!!!!!!!!!!!!!!!!!!!!!!")
    #     print(customer)
    #     print(type(customer))
    customer = rest_client.get(ssn)
    #print(customer)

    return customer