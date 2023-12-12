import typing
from fastapi import FastAPI, HTTPException
from solcx import compile_standard, install_solc
from pydantic import BaseModel
from web3 import Web3
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import json
from hexbytes import HexBytes
# State: Init Data
initSuccess = False

# DB Config
db_config = {
"host": "localhost",
"user": "cryptox_dev",
"password": "cos30049",
"database": "cryptox_db"
}

app = FastAPI()

install_solc("0.8.0")

# Account Interface
class Account(BaseModel):
    user_id: typing.Union[int, None] = None
    username: str
    password: typing.Union[str, None] = None
    token: typing.Union[str, None] = None

class BuyModel(BaseModel):
    account_token: typing.Union[str, None] = None
    price: typing.Union[float, None] = None
    asset_id: typing.Union[str, None] = None
    

with open('./data/init_assets.json') as file:
    assets = json.load(file)

connection = mysql.connector.connect(**db_config)

# Server Config
# CORS Config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chain and Web3 config
chain_id=1337
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
cursor = connection.cursor()

# Solidity
# Read Solidity file
with open('./Asset.sol', 'r') as file:
    asset_sol = file.read()
    

# compiled solidity class
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources":{"Asset.sol": {"content": asset_sol}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version = "0.8.0",
)

# JSON Dump
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Get Bytecode and ABI of compiled template
bytecode = compiled_sol["contracts"]["Asset.sol"]["Asset"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["Asset.sol"]["Asset"]["abi"]

AssetSmartContract = w3.eth.contract(abi=abi, bytecode=bytecode)



# For demonstration: This function...
def init():
    """
    0. Connect database
    1. Insert mock data for
        1.1 user
        1.2 Public & Private key table
    2. Read and parse JSON file of mock data (assets) to an array
    3. For each element
        3.1 Deploy a smart contract(price), store abi, receipt, bytecode
        3.2 Set/update asset_id = contract address before insert into assets table
        3.3 Insert contract address, contract_abi to smart_contract table
        3.4 Insert receipt to table
    """

    try:
        # For demonstration only: Clear and re-insert table
        query = "DELETE FROM transaction_receipt;"
        cursor.execute(query)
        query = "DELETE FROM asset;"
        cursor.execute(query)
        query = "DELETE FROM private_key;"
        cursor.execute(query)
        query = "DELETE FROM account;"
        cursor.execute(query)

        # For demonstration: Insert pre-made data
        insertUserDataQuery = '''INSERT IGNORE INTO account (user_id, username, password, token)
        VALUES
        (1, 'cryptox_admin', 'password1', '0xDC54710Fa3527fA5248076D45544be52218d8a0a'),
        (2, 'jane_smith', 'randomPwd', '0x17fF244F87B353db33240526333e0118fA6AD608'),
        (3, 'mark_johnson', 'p@ssw0rd', '0xFc3829DbF2ABf666e3ca53e71eb3049cf4D3498d'),
        (4, 'susan_wilson', 'Secret12', '0x636d56a73D1596238E9D92690F3208b0f8ff68cC'),
        (5, 'michael_brown', 'p@ssw0rd', '0x8cE6008f89e16c90710db852ab3B5fdcc234F9Bd'),
        (6, 'laura_miller', 'SecurePwd', '0xe4AfEBE1A4c12de13b446a1348DD0dDF4a6beb64'),
        (7, 'robert_jones', 'password123', '0x5Ac85206D65abC72cC343E9b1DC8BCFd79D635EC'),
        (8, 'emily_davis', 'myP@ss', '0x4252Fa1Fa52fa2ED86a8f51c3e097D6dB0FC9A07'),
        (9, 'jacob_wilson', 'newPwd', '0x9a9A3B5bc3e1A9082A3A38FE437bC0F51F28563c'),
        (10,'shirogane_miyuki', 'akaakasaka', '0x65DEe591c3FF738cDE5722618e00ce334BE5e814');
        ;'''

        insertPrivateKeyData = '''
            INSERT IGNORE INTO private_key (user_key, user_addr)
            VALUES 
            ('0x9678533528c353461fa8bb664b42b74448df1b7ee4592397c764dc2e443481eb', '0xDC54710Fa3527fA5248076D45544be52218d8a0a'),
            ('0xb9ce1c77952620f5a64f2bed8b04992656eca7591bd7c4010f3d27a0da39ad18','0x17fF244F87B353db33240526333e0118fA6AD608'),
            ('0xccb1142e656e875ca6388cf7c016a31c7b6ee78dc6877713d2c83249868bdd42', '0xFc3829DbF2ABf666e3ca53e71eb3049cf4D3498d'),
            ('0xa1494e6d55d3b16ed92dff28a1cc289bfc596be6d56c7a7abb0d1e31ceb4d2c9', '0x636d56a73D1596238E9D92690F3208b0f8ff68cC'),
            ('0x75702a686ec007f6449dfce768029d5a7842310d7afb94ca0224793a847ae7c5', '0x8cE6008f89e16c90710db852ab3B5fdcc234F9Bd'),
            ('0x3177ffe9dae102cf90fe672e7f0a83aaf8aadcc3dbadfe12c1b1560b63669209', '0xe4AfEBE1A4c12de13b446a1348DD0dDF4a6beb64'),
            ('0xa84ef5b8c793726082b0d26e27184d1ec232bb4592766826b2cb8818d384be72','0x65DEe591c3FF738cDE5722618e00ce334BE5e814'),
            ('0x0f256e808a78d61846346f52cdf8d7066107799854dbed209e5e8d116a3c4526', '0x5Ac85206D65abC72cC343E9b1DC8BCFd79D635EC'),
            ('0x6609e974f7792cdf222fdbae2cd13b28684dc544e4688a938bcd6f0a30630849', '0x4252Fa1Fa52fa2ED86a8f51c3e097D6dB0FC9A07'),
            ('0x18b569fbb9d5a3567732be785f98b8d0775e50273369d2d667e6bc636ef7acac', '0x9a9A3B5bc3e1A9082A3A38FE437bC0F51F28563c');
        '''

        # Create a cursor to execute SQL queries
        cursor.execute(insertUserDataQuery)
        cursor.execute(insertPrivateKeyData)
        connection.commit()

        for asset in assets:
            # Get token from user 
            query = "SELECT t1.token, t2.user_key FROM account AS t1 JOIN private_key AS t2 ON t1.token = t2.user_addr WHERE t1.user_id = " + str(asset['user_id']) + ";"  
            cursor.execute(query)
            result = cursor.fetchone()
            
            if(result != None):
                key = dict(zip(cursor.column_names, result))
                try:
                    nonce = w3.eth.get_transaction_count(key['token'])

                    transaction = AssetSmartContract.constructor(int(float(asset["price"])*(10 ** 18))).build_transaction(
                    {
                        "chainId": chain_id,
                        "gasPrice": w3.eth.gas_price,
                        "from": key['token'],
                        "nonce": nonce,
                    })
                    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=key["user_key"])
                    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
                    contract_address = tx_receipt["contractAddress"]
                    
                    query = "INSERT IGNORE INTO asset (asset_id, name, price, volume, description, category, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                    value = (contract_address, asset["title"], float(asset["price"]), float(asset["volume"]), asset["title"], asset["tag"], asset["user_id"])
                    cursor.execute(query, value)
                    connection.commit()
                    
                    query = "INSERT IGNORE INTO transaction_receipt(contract_address, details) VALUES (%s, %s);"
                    tx_receiptDict = dict(tx_receipt)
                    txnJSON = w3.to_json(tx_receiptDict)
                    value = (contract_address, txnJSON)
                    
                    cursor.execute(query, value)
                    connection.commit()

                except Exception as error:
                    print(error)
        print("Init Success")

        cursor.close()
    except Exception as error:
        print(error)

# Init endpoint (call on webpage start)

@app.post("/buy")
async def buy(buyModel : BuyModel):
    """
    1. Transfer money
    2. Take receipt from smart contract
    3. Store and push receipt of transaction to receipt table
    """
    cursor = connection.cursor()

    query = "SELECT user_key FROM private_key WHERE user_addr='"+ buyModel.account_token + "';" 
    cursor.execute(query)
    result = cursor.fetchone()
    if(result != None):
        try:
            key = dict(zip(cursor.column_names, result))
            transaction = {
                'nonce': w3.eth.get_transaction_count(account=buyModel.account_token),
                'gasPrice': w3.eth.gas_price, 
                'gas': 3000000,
                'to': buyModel.asset_id,
                'value': w3.to_wei(buyModel.price,'ether')
            }
            signed_txn = w3.eth.account.sign_transaction(transaction, key["user_key"])
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            tx_receiptDict = dict(tx_receipt)
            tx_receiptDict["value"] = buyModel.price
            txnJSON = w3.to_json(tx_receiptDict)
            value = (buyModel.asset_id, txnJSON)
            query = "INSERT IGNORE INTO transaction_receipt(contract_address, details) VALUES (%s, %s);"
            cursor.execute(query, value)
            connection.commit()
            return tx_receiptDict["status"]
        
            cursor.close()
        except Exception as err:
            print(err)
            return err

@app.post("/login/")
def login(account: Account):
    try:
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve data (e.g., all assets)
        query = "SELECT username, password FROM account WHERE username=%s AND password=%s"
        values = (account.username, account.password)

        print(account.username)
        print(account.password)

        # Execute the SQL query
        cursor.execute(query, values)

        # Fetch all the rows
        result = cursor.fetchone()
        msg = None

        if (result):
            msg = {"message": f"Welcome back, {account.username}"}
        else:
            msg = {"error": f"Sorry, your username '{account.username}' is not found, or your password is incorrect!"}

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

        return {"message": f"Welcome onboard, {account.username}"}
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}

@app.post("/account/")
async def get_account(account: Account):
    try:

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve data (e.g., all assets)
        query = "SELECT username, token FROM account WHERE username='" + account.username + "';"

        print(query)

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows
        result = cursor.fetchone()
        
        if (result == None):
            # Close the cursor
            cursor.close()
            raise HTTPException(status_code=404, detail=f"User with username '{account.username}' not found!")
        else:
            # Convert the result to a list of dictionaries
            account = dict(zip(cursor.column_names, result))
            # Close the cursor
            cursor.close()
            return account
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}

@app.get("/assets")
def get_assets():
    try:
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve data (e.g., all assets)
        query = "SELECT asset_id, name, price, volume, description, category FROM asset;"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows
        result = cursor.fetchall()

        # Convert the result to a list of dictionaries
        assets = [dict(zip(cursor.column_names, row)) for row in result]
        
        # Close the cursor and the database connection
        cursor.close()

        
        if (len(assets) == 0):
            return {"message": "No assets available!"}
        else:
            return assets
    except mysql.connector.Error as err:
        return {"error": f"Error: {err}"}
    

@app.get("/transactionsHistory")
async def getHistory() :
    try:
        cursor = connection.cursor()

        query = "SELECT details, txn_time from transaction_receipt order by txn_time desc;"
        cursor.execute(query)
        
        result = cursor.fetchall()

        history = [dict(zip(cursor.column_names, row)) for row in result]

        for txn in history:
            txn["details"] = json.loads(txn["details"])

        return history
    except Exception as err:
        print(err)

    return 
init()