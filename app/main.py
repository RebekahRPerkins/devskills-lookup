import customer_lookup
from typing import Optional
from fastapi import FastAPI
from databases import Database
from rest_client import RestClient
from db_client import DatabaseClient

database = Database("sqlite:///app.db")

app = FastAPI()

# NOTE: Feel free to restructure the code and database schema the way you prefer. This is only an example.

@app.on_event("startup")
async def database_connect():
    await database.connect()

#    query = "DROP TABLE Customer"
#    await database.execute(query=query)

    query = """CREATE TABLE IF NOT EXISTS Customer 
    (id INTEGER PRIMARY KEY, ssn VARCHAR(100), first VARCHAR(100), last VARCHAR(100), address VARCHAR(100), 
    assessed_income INTEGER, balance_of_debt INTEGER, complaints INTEGER)"""
    await database.execute(query=query)

@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

@app.get("/ping")
async def ping():
    return "ping success"

#http://127.0.0.1:8000/credit-data/424-11-9327
@app.get("/credit-data/{ssn}")
async def credit_data(ssn):
    rest_client = RestClient(logger = None)
    db_client = DatabaseClient(logger = None)
    data = await customer_lookup.get(ssn, db_client, rest_client)
    if data:
        return data
    else:    
        return "None found"
