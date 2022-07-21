import credit_data_stub
from typing import Optional

from fastapi import FastAPI

from databases import Database

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
    query = "SELECT name,score FROM HighScores"
    rows = await database.fetch_all(query=query)
    return {"rows": rows}

#http://127.0.0.1:8000/credit-data/424-11-9327 for now
@app.get("/credit-data/{ssn}")
async def credit_data(ssn):
    data = await credit_data_stub.get2(ssn)
    return data