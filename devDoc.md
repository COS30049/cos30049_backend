<p align="right"><code><a href="/"><b> ✕ CLOSE <br></b></a></code></p>

# 📄 Document

### Implementation Process

## Set up conda environement

1. Create environment
   - Locate the project directory, create a folder with name i.e, 'env' 

      ```bash
  	  conda create -p path\to\project\env
  	  ```
   - Add the project directory path to `envs_dirs` config

	  ```bash
      conda config --add envs_dirs path\to\project
      ```
   - Set the prompt name

  	 ```bash
     conda config --set env_prompt '({name})'
     ```
2. Activate environment
	```bash
	conda activate env
 	```
3. Install packages with `conda`
	
 	- `fastapi`:
		```bash
  		conda install -c conda-forge fastapi
  		```

   		```bash
     	conda install -c "conda-forge/label/cf202003" fastapi
     	```
     
	- `uvicorn`:
		```bash
  		conda install -c conda-forge uvicorn-standard
  		```

4. Install packages with `pip`
	
 	- `web3`:
		```bash
  		pip install web3
  		```

   		```bash
     	conda install -c "conda-forge/label/cf202003" fastapi
     	```
     
	- `py-solc-x`:
		```bash
  		pip install py-solc-x
  		```
	 

### Architecture Design
Doc: https://drive.google.com/file/d/1DnwRQiimq5pku8-QBjmIaTpaFixNiKkW/view?usp=sharing

### Instruction
Explain abt comment structure, src code structure, how it meets core functionality

Professional standards in organization and writing

Effective and pragmatic database design

Use Cases

Instruction for project deployment

## Database
Efficient management and implementation of databases, including schema design, indexing, and querying, ensuring proper data storage, retrieval and manipulation

### Database Design
MYSQL Table
- Table User account
    username & password & id/#
    ```
    # SCHEMA
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    wallet_id VARCHAR(50) NOT NULL
    ```
- Transaction
    - hash
    - from
    - to
    - amount
    - txn fee
    - age
    ```
    # SCHEMA
    hash varchar(50) NOT NULL PRIMARY KEY,
    payer_wId VARCHAR(50) NOT NULL,
    payee_wId VARCHAR(50) NOT NULL,
    amount DOUBLE NOT NULL,
    txn_fee DOUBLE NOT NULL,
    ```
- Assets Table
    - asset information
        - \#
        - title
        - floor price
        - volume
        - description
        - category
        - owner -> user account (wallet)
    ```
    # SCHEMA
    id VARCHAR(50) NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    desc VARCHAR(200) NULL,
    category 
    floor_price DOUBLE NOT NULL,
    volume DOUBLE NOT NULL,
    owner userID NOT NULL,
    FOREIGN KEY owner REFERENCES account(id)   
    ```
- Trading Table
    - assets (foreign key -> assetTable.#)
    - transaction (foreign key -> transaction.#, nullable, be added after successful(status == done))
    - buyer (not sure)
    - seller (not sure, might be duplicate with information in txn)
    - date of trade
    - status? (Done -> Create new row in txn table)
        - Connect with smart contract
- ...

ERD
https://drive.google.com/file/d/1juDInxldOTca9q0uiPiGJEhruoyqZ7tc/view?usp=sharing

## API:
Dùng để viết doc

https://www.notion.so/templates/api-template

template của trường:
**API name and description:** The name of the API and explain what the API provides.

The **Tracking ID API** provides a service to retrieve tracking IDs for shipments. Users can get shipment details using a tracking ID.

**Endpoints:** For each endpoint, details about the URL, HTTP methods (GET, POST, PUT, DELETE, etc.).
```
URL: https://localhost:5000//trackingID/:123456
Method: GET
```

**Request Parameters:** Information about the parameters required for each API request.

```json
{
  "trackingID": "123456"
}
```

**Response Format:** Explanation of the structure and format of API responses, typically in JSON or XML, and description of status codes and their meanings (e.g., 200 OK, 404 Not Found)

```json
{
  "status": "200 OK"
  "content": {
    "trackingID": "123456",
    "shipmentDetail": {
      "origin": "NY, USA",
      ...
    }
  }
}
```

### Postman:
Dùng để test API (Lập tài khoản trước khi dùng)

https://www.postman.com/

## Core Functionalities

## Front-end API interaction
### HTTP Request
Use Axios

### File Upload

### Error Handling

### User-Friendly UI, UX

### Stability
