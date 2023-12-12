-- SET UP USERS

-- Create users
CREATE USER 'cryptox_dev'@'localhost' IDENTIFIED BY 'cos30049';
CREATE USER 'cryptox_client'@'localhost' IDENTIFIED BY 'swinburne';
 
-- Grant privileges to users
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, 
FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, 
LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW 
VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, CREATE TABLESPACE ON * . * 
TO 'cryptox_dev'@'localhost';
GRANT SELECT ON *.* TO 'cryptox_client'@'localhost';
 
-- Review users' privileges
SHOW GRANTS FOR 'cryptox_dev'@'localhost';
SHOW GRANTS FOR 'cryptox_client'@'localhost';


-- SET UP DATABASE AND TABLES
 
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
-- Create TABLE "asset" if not exists
CREATE TABLE IF NOT EXISTS asset (
    asset_id VARCHAR(128) NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(30, 18) NOT NULL DEFAULT 0.000000000000000000,
    volume DECIMAL(30, 18) NOT NULL DEFAULT 0.000000000000000000,
    description TEXT NOT NULL,
    category ENUM('Music', 'Game', 'Anime', 'DC', 'Sports') NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES account(user_id) );

-- Create TABLE "transaction_receipt" if not exists
CREATE TABLE IF NOT EXISTS transaction_receipt (
    receipt_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    contract_address VARCHAR(256) NOT NULL,
    details TEXT NOT NULL,
    txn_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(contract_address) REFERENCES asset(asset_id)
);

-- Current tables
SHOW TABLES;

-- Show all columns of tables
DESCRIBE account;
DESCRIBE private_key;
DESCRIBE transaction_receipt;
DESCRIBE asset;
