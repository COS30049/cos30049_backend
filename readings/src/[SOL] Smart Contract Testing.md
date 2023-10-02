## Main Contents
1. [Solidity Testing](#solidity-testing)
2. [Testing Frameworks](#testing-frameworks)
3. [Ganache](#ganache)

## Solidity Testing

\[[← See all readings](../README.md)\]

> Testing involves checking the correctness, security, and performance of smart contracts

### Contract under test

```solidity
contract MyContract {
	uint256 public myNumber;
	uint356 public mySecondNumber;
	
	function setMyNumber(uint256 _myNumber) public {
		myNumber = _myNumber;
	}

	function setMySecondNumber(uint256 _mySecondNumber) public {
		mySecondNumber = _mySecondNumber;
	}

	function getNumbersSum() public view returns (uint256) {
		return myNumber + mySecondNumber;
	}
}
```

### Unit Tests

- `Def`: validate the behaviour of individual functions or components of a contract. 
- `Purpose`: identify and fix bugs at an early stage, ensuring each function of the contract works as intended

Unit test for `setMyNumber()`function of contract [`MyContract`](#contract-under-test) 
```js
it("should set MyNumber to the correct value", async () => {
	await myContract.setMyNumber(10, { from: accounts[0] });
	const myNumber = await myContract.myNumber();
	assert.equal(myNumber.toString(), "10");
});
```
### Integration Tests

- `Def`: check how multiple contracts interact with each other
- `Purpose`: ensure that contracts can work together seamlessly, identifying and addressing any interoperability issues

Integration test to verify that `setMyNumber()` and `setMySecondNumber()` work together correctly with `getNumbersSum()`
from contract [`MyContract`](#contract-under-test) 
```js
it("should correctly calculate the sum after setting numbers", async () => {
	await myContract.setMyNumber(10, { from: accounts[0] });
	await myContract.setMySecondNumber(20, { from: accounts[0] });
	const sum = await myContract.getNumbersSum();
	assert.equal(sum.toString(), "30");
});
```

## Testing Frameworks

\[[back to top ↑](#main-contents)\] \[[← See all readings](../README.md)\]

>- provide a set of tools and practices designed to help developers test their contracts more effectively.
>- most widely used testing frameworks for Solidity are **Truffle**, **Hardhat**, **Waffle**, and **Remix**

### Truffle Framework

> a popular development framework for Ethereum that provides built-in smart contract compilation, linking, deployment, and binary management, as well as automated contract testing.

#### Installation

**via `npm`**
```bash
npm install -g truffle
```

**Create a new Truffle project**
```bash
truffle init
```

This will create a project with the following directory structure
```txt
.
├── contracts
├── migrations
├── test
└── truffle-config.js

3 directories, 1 file
```

#### Testing

- `Writing`:
	- can be written in `JavaScript`, `Solidity`, or `TypeScript`
	- should be placed in the `test` directory
- `Running`:
	- run command in terminal: `truffle test`

#### Example

##### Project Directory
```txt
.
├── contracts
│	└── SimpleStorage.sol
├── migrations
│	└── 2_deploy_simplestorage.js
├── test
│	└── simplestorage_test.js
└── truffle-config.js
```

##### Create a contract

>directory: `contracts`
>filename: `SimpleStorage.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
	uint256 public storedData;
	
	function set(uint256 x) public {
		storedData = x;
	}
	
	function get() public view returns (uint256) {
		return storedData;
	}
}
```

##### Create Migration File

>directory: `migrations`
>filename: `2_deploy_simplestorage.js`

```js
const SimpleStorage = artifacts.require("SimpleStorage");

module exports = function (deployer) {
	deployer.deploy(SimpleStorage);
};
```
>- `2_deploy_simplestorage.js`: deploys [`SimpleStorage`](#create-a-contract) contract onto the `Ethereum` blockchain or a simulated blockchain environment like `Ganache` for development and testing purposes
>- `artifacts.require()`: a part of `Truffle`'s contract abstraction which helps to fetch the compiled contract artifacts
>- `module.exports` is a `node.js` syntax that exports a function to be used in other files
>	- parameter `deployer`: a `Truffle` object that assists in deploying smart contracts onto the network

##### Write the Test

>directory: `test`
>filename: `simplestorage_test.js`

```js
const SimpleStorage = artifacts.require('SimpleStorage');

contract('SimpleStorage', (accounts) => {
	it('should store the value 89', async () => {
		const simpleStorageInstance = await SimpleStorage.deployed();
		await SimpleStorageInstance.set(89, { from: accounts[0] });
		const storedData = await simpleStorageInstance.get();
		assert.equal(storedData, 89, 'The value 89 was not stored.');
	});
});
```
>- `contract()`: provided by `Truffle` for grouping together a suite of tests pertaining the [`SimpleStorage`](#create-a-contract) contract
>- parameter `accounts`: an array of account addresses available during testing, provided by the `Ethereum client` (like `Ganache`).

##### Run the Test

1. Create a local development blockchain
	```bash
	truffle develop
	```

	You will see something like this
	
	```txt
	Truffle Develop started at http://127.0.0.1:9545/
	
	Accounts:
	(0) 0x[40 hexadecimal characters]
	(1) 0x[40 hexadecimal characters]
	...
	
	Private Keys:
	(0) [64 hexadecimal characters]
	(1) [64 hexadecimal characters]
	...
	```

2. Inside `Truffle` development prompt, run:
	```bash
	migrate
	```

	You will see something like this
	
	```txt
	Using network 'develop'.
	
	Compiling your contracts...
	===========================
	> Everything is up to date, there is nothing to compile.
	
	
	  Contract: SimpleStorage
	    ✔ should store the value 90 (173ms)
	
	
	  1 passing (224ms)
	```

Your test should now run, and if everything is set up correctly, it should pass.

## Ganache

\[[back to top ↑](#main-contents)\] \[[← See all readings](../README.md)\]

> simply an Ethereum blockchain simulator

**Advantages**
- **Ready to use**, quickly start an EVM blockchain network (you can set up miners, block generation time) 
- **Conveniently fork** (branch) an existing blockchain network (without waiting for block synchronization) 
- **Simulate any account** (you can simulate the use of any user's token in the environment without a private key).

### Usage: see [slides](https://swinburne.instructure.com/courses/52786/files/26671054) | [⭳](https://swinburne.instructure.com/courses/52786/files/26671054/download?download_frd=1) (p.17~)
