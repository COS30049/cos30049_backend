import typing
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# DB
import mysql.connector

app = FastAPI()

origins = ["*"]

# MySQL database connection configuration
db_config = {
    "host": "localhost",
    "user": "cryptox_dev",
    "password": "cos30049",
    "database": "cryptox_db"
}

# Establish a database connection
connection = mysql.connector.connect(**db_config)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Account(BaseModel):
    user_id: typing.Union[int, None] = None 
    username: typing.Union[str, None] = None
    password: typing.Union[str, None] = None
    token: typing.Union[str, None] = None

@app.post("/login/")
def login(account: Account):
    try:
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        connection.close()

        # Define the SQL query to retrieve data (e.g., all assets)
        query = "SELECT username, password FROM account WHERE username=%s AND password=%s"
        values = (account.username, account.password)

        # Execute the SQL query
        cursor.execute(query, values)

        # Fetch all the rows
        result = cursor.fetchone()
        msg = None

        if (result):
            msg = {"Message": f"Welcome back, {account.username}"}
        else:
            msg = {"Message": f"Sorry, your username '{account.username}' is not found, or your password is incorrect!"}

        # Close the cursor  
        cursor.close()

        return msg 
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}

@app.post("/signup/")
def signup(account: Account):
    try:
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve data (e.g., all assets)
        query = "INSERT INTO account (username, password, token) VALUES (%s, %s, %s)"
        values= (account.username, account.password, account.token)

        # Execute the SQL query
        cursor.execute(query, values)

        # Commit the changes to the database
        connection.commit()

        # Close the cursor
        cursor.close()

        return {"Message": f"Welcome onboard, {account.username}"}
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}

@app.post("/account/")
async def get_account(account: Account):
    try:

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve data (e.g., all assets)
        query = "SELECT username, token FROM account WHERE user_id=" + str(account.user_id)

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows
        result = cursor.fetchone()
        
        if (result == None):
            # Close the cursor
            cursor.close()
            raise HTTPException(status_code=404, detail=f"User with id '{account.user_id}' not found!")
        else:
            # Convert the result to a list of dictionaries
            account = dict(zip(cursor.column_names, result))
            # Close the cursor
            cursor.close()
            return account
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}

@app.get("/assets/")
def get_assets():
    try:
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve data (e.g., all assets)
        query = "SELECT asset_id, name, price, volume, description, category FROM asset"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows
        result = cursor.fetchall()

        # Convert the result to a list of dictionaries
        assets = [dict(zip(cursor.column_names, row)) for row in result]
        
        # Close the cursor and the database connection
        cursor.close()

        if (len(assets) == 0):
            return {"Message": "No assets available!"}
        else:
            return assets
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}
    
@app.get("/assets/{asset_id}")
def get_asset(asset_id: str):
    try:
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve data (e.g., asset with matched asset_id)
        query = "SELECT asset_id, name, price, volume, description, category  FROM asset WHERE asset_id=" + asset_id

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows
        result = cursor.fetchone()

        if (result == None):
            # Close the cursor
            cursor.close()
            return {"Message": f"Asset with id '{asset_id}' not found!"}
        else:
            # Convert the result to a list of dictionaries
            asset = dict(zip(cursor.column_names, result))

            # Close the cursor
            cursor.close()

            return asset
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}
    
# @app.get("/smart_contract/{asset_id}")
# def get_asset(asset_id: str):
#     try:
#         # Create a cursor to execute SQL queries
#         cursor = connection.cursor()

#         # Define the SQL query to retrieve data (e.g., asset with matched asset_id)
#         query = "SELECT asset_id, name, floor_price, volume, description, category  FROM asset WHERE asset_id=" + asset_id

#         # Execute the SQL query
#         cursor.execute(query)

#         # Fetch all the rows
#         result = cursor.fetchall()

#         if (result == None):
#             # Close the cursor
#             cursor.close()
#             raise HTTPException(status_code=404, detail=f"Asset with id '{asset_id}' not found!")
#         else:
#             # Convert the result to a list of dictionaries
#             asset = [dict(zip(cursor.column_names, row)) for row in result]

#             # Close the cursor
#             cursor.close()
#             return asset
#     except mysql.connector.Error as err:
#         return {"error": f"Error: {err}"}