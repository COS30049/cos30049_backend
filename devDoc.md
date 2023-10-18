<p align="right"><code><a href="/"><b> ✕ CLOSE <br></b></a></code></p>

# 📄 Document

### Implementation Process

#### Set up environement

1. Create environment
   - Locate the project directory, create a folder with name i.e, 'env' 

      ```bash
  	  conda create -p path\to\project\env python=3.9
  	  ```
   - Add the project directory path to `envs_dirs` config (do this once)

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
     
	- `py-solc-x`:
		```bash
  		pip install py-solc-x
  		```
or ...
	<details>
		<summary>Change the <code>prefix</code> value in this file and save this as <code>.yml</code></summary>

```yml
name: env
channels:
  - conda-forge
  - defaults
dependencies:
  - aiohttp=3.8.5=py39h2bbff1b_0
  - aiosignal=1.2.0=pyhd3eb1b0_0
  - anyio=3.7.1=pyhd8ed1ab_0
  - async-timeout=4.0.2=py39haa95532_0
  - attrs=23.1.0=py39haa95532_0
  - ca-certificates=2023.08.22=haa95532_0
  - charset-normalizer=2.0.4=pyhd3eb1b0_0
  - click=8.1.7=win_pyh7428d3b_0
  - colorama=0.4.6=pyhd8ed1ab_0
  - exceptiongroup=1.1.3=pyhd8ed1ab_0
  - fastapi=0.103.2=pyhd8ed1ab_0
  - frozenlist=1.3.3=py39h2bbff1b_0
  - h11=0.14.0=pyhd8ed1ab_0
  - httptools=0.6.0=py39ha55989b_1
  - idna=3.4=pyhd8ed1ab_0
  - multidict=6.0.2=py39h2bbff1b_0
  - openssl=3.0.11=h2bbff1b_2
  - pip=23.2.1=py39haa95532_0
  - pydantic=1.10.12=py39h2bbff1b_1
  - python=3.9.18=h1aa4202_0
  - python-dotenv=1.0.0=pyhd8ed1ab_1
  - python_abi=3.9=2_cp39
  - pyyaml=6.0.1=py39ha55989b_1
  - setuptools=68.0.0=py39haa95532_0
  - sniffio=1.3.0=pyhd8ed1ab_0
  - sqlite=3.41.2=h2bbff1b_0
  - starlette=0.27.0=pyhd8ed1ab_0
  - typing-extensions=4.8.0=hd8ed1ab_0
  - typing_extensions=4.8.0=pyha770c72_0
  - tzdata=2023c=h04d1e81_0
  - ucrt=10.0.22621.0=h57928b3_0
  - uvicorn=0.23.2=py39hcbf5309_1
  - uvicorn-standard=0.23.2=hcbf5309_1
  - vc=14.2=h21ff451_1
  - vc14_runtime=14.36.32532=hdcecf7f_17
  - vs2015_runtime=14.36.32532=h05e6639_17
  - watchfiles=0.20.0=py39hf21820d_2
  - websockets=11.0.3=py39ha55989b_1
  - wheel=0.41.2=py39haa95532_0
  - yaml=0.2.5=h8ffe710_2
  - yarl=1.8.1=py39h2bbff1b_0
  - pip:
      - bitarray==2.8.2
      - certifi==2023.7.22
      - cytoolz==0.12.2
      - eth-abi==4.2.1
      - eth-account==0.9.0
      - eth-hash==0.5.2
      - eth-keyfile==0.6.1
      - eth-keys==0.4.0
      - eth-rlp==0.3.0
      - eth-typing==3.5.0
      - eth-utils==2.2.1
      - hexbytes==0.3.1
      - jsonschema==4.19.1
      - jsonschema-specifications==2023.7.1
      - lru-dict==1.2.0
      - parsimonious==0.9.0
      - protobuf==4.24.3
      - py-solc-x==1.1.1
      - pycryptodome==3.19.0
      - pyunormalize==15.0.0
      - pywin32==306
      - referencing==0.30.2
      - regex==2023.10.3
      - requests==2.31.0
      - rlp==3.0.0
      - rpds-py==0.10.3
      - semantic-version==2.10.0
      - toolz==0.12.0
      - urllib3==2.0.6
      - web3==6.10.0
prefix: [path\to\project\env]
```
</details>

   then run this in Anaconda Prompt

   ```bash
   conda env create -f environment.yml
   ```

### Architecture Design
Doc: https://drive.google.com/file/d/1DnwRQiimq5pku8-QBjmIaTpaFixNiKkW/view?usp=sharing

![image](https://github.com/COS30049/cos30049_backend/assets/139601671/35a9f402-20f3-4577-8359-14b0407f3634)

### Instruction
Explain abt comment structure, src code structure, how it meets core functionality

Professional standards in organization and writing

Effective and pragmatic database design

Use Cases

Instruction for project deployment

## Database
Efficient management and implementation of databases, including schema design, indexing, and querying, ensuring proper data storage, retrieval and manipulation

### Database Design/Deployment

#### ERD 

https://drive.google.com/file/d/1juDInxldOTca9q0uiPiGJEhruoyqZ7tc/view?usp=sharing

### Set up users
Copy & Paste to the MySQL CLI:
```sql
-- Create users
CREATE USER 'cryptox_dev'@'localhost' IDENTIFIED BY 'cos30049';
CREATE USER 'cryptox_client'@'localhost' IDENTIFIED BY 'swinburne';

-- Grant privileges to users
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, CREATE TABLESPACE ON * . * TO 'cryptox_dev'@'localhost';
GRANT SELECT ON *.* TO 'cryptox_client'@'localhost';

-- Review users' privileges
SHOW GRANTS FOR 'cryptox_dev'@'localhost';
SHOW GRANTS FOR 'cryptox_client'@'localhost';

```

#### Set up database and tables
Copy & Paste to the MySQL CLI:
```sql
-- Create DATABASE "cryptox_db" if not exists
CREATE DATABASE IF NOT EXISTS cryptox_db;

-- Select/Use DATABASE "cryptox_db"
USE cryptox_db;

-- Create TABLE "account" if not exists
CREATE TABLE IF NOT EXISTS account (
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    token VARCHAR(50) NOT NULL UNIQUE );

/* 
 * <!> THIS IS FOR DEMONSTRATION PURPOSE ONLY BECAUSE
 * ONLY USERS HAVE OWNERSHIPS OF THEIR KEYS <!>
 */

-- Create TABLE "private_key" if not exists
CREATE TABLE IF NOT EXISTS private_key (
    user_key VARCHAR(256) NOT NULL UNIQUE,
    user_addr VARCHAR(50) NOT NULL UNIQUE,
    FOREIGN KEY (user_addr) REFERENCES account(token)
);

-- Populate private keys and address to table "private_key"
INSERT INTO private_key (user_key, user_addr)
VALUES 
  ('0x9678533528c353461fa8bb664b42b74448df1b7ee4592397c764dc2e443481eb', '0xDC54710Fa3527fA5248076D45544be52218d8a0a'),
  ('0xb9ce1c77952620f5a64f2bed8b04992656eca7591bd7c4010f3d27a0da39ad18','0x17fF244F87B353db33240526333e0118fA6AD608'),
  ('0xccb1142e656e875ca6388cf7c016a31c7b6ee78dc6877713d2c83249868bdd42', '0xFc3829DbF2ABf666e3ca53e71eb3049cf4D3498d'),
  ('0xa1494e6d55d3b16ed92dff28a1cc289bfc596be6d56c7a7abb0d1e31ceb4d2c9', '0x636d56a73D1596238E9D92690F3208b0f8ff68cC'),
  ('0x75702a686ec007f6449dfce768029d5a7842310d7afb94ca0224793a847ae7c5', '0x8cE6008f89e16c90710db852ab3B5fdcc234F9Bd'),
  ('0x3177ffe9dae102cf90fe672e7f0a83aaf8aadcc3dbadfe12c1b1560b63669209', '0xe4AfEBE1A4c12de13b446a1348DD0dDF4a6beb64'),
  ('0x0f256e808a78d61846346f52cdf8d7066107799854dbed209e5e8d116a3c4526', '0x5Ac85206D65abC72cC343E9b1DC8BCFd79D635EC'),
  ('0x6609e974f7792cdf222fdbae2cd13b28684dc544e4688a938bcd6f0a30630849', '0x4252Fa1Fa52fa2ED86a8f51c3e097D6dB0FC9A07'),
  ('0x18b569fbb9d5a3567732be785f98b8d0775e50273369d2d667e6bc636ef7acac', '0x9a9A3B5bc3e1A9082A3A38FE437bC0F51F28563c');

-- Create TABLE "smart_contract" if not exists
CREATE TABLE IF NOT EXISTS smart_contract (
    contract_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    contract_addr VARCHAR(256) NOT NULL,
    contract_abi TEXT NOT NULL,
    FOREIGN KEY(contract_addr) REFERENCES asset(asset_id) );

-- Create TABLE "transaction_receipt" if not exists
CREATE TABLE IF NOT EXISTS transaction_receipt (
    receipt_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    smartcontract_id INT NOT NULL,
    details TEXT NOT NULL,
    FOREIGN KEY(smartcontract_id) REFERENCES smart_contract(contract_id) );

-- Create TABLE "asset" if not exists
CREATE TABLE IF NOT EXISTS asset (
    asset_id VARCHAR(128) NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    floor_price DECIMAL(30, 18) DEFAULT 0.000000000000000000,
    volume DECIMAL(30, 18) DEFAULT 0.000000000000000000,
    description TEXT NOT NULL,
    category ENUM('Music', 'Game', 'Anime', 'DC', 'Sports') NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES account(user_id) );

-- Current tables
SHOW TABLES;

-- Show all columns of tables
DESCRIBE account;
DESCRIBE smart_contract;
DESCRIBE transaction_receipt;
DESCRIBE asset;

```

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
