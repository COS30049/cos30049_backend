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
	<summary>Change the prefix value in this file and save this as <code>.yml</code></summary>

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
