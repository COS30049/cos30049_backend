---
title: Week 9 - Smart contract vulnerabilities introduction
tags:
  - COS30049/lectures
---
## The DAO Attack

### Background

- **`Before 2015`**: Emergence of the `DAOs` (Decentralized Automated Organizations) concept  among the nascent Ethereum community.
   >***What `DAOs` aimed to achieve was:***
   >- to **facilitate collaboration among individuals** through verifiable code (specifically, smart contracts running on the Ethereum blockchain)
   >- to **make decentralized decisions** through the community's protocols.
- `2016`: a `DAO` was created named, 'The DAO'
   >It was a decentralized investment fund controlled by the community. It raised $150 million worth of Ether (approximately 3.54 million ETH) by selling its own community token.
   >
   >🔎 More about **`DAOs`**? [`Read`](https://ethereum.org/en/dao/)
   >
- `Less than 3 months later`: the DAO was attacked by a 'black hat' hacker. 
>This attack had drained most of the $150 million worth of ETH from The DAO's smart contract and has come to be known as 
>👇
### Re-entrancy Attack

>This is an attack which exploits the execution of a Solidity function, a special construct that gets triggered under certain circumstances.
>This function is called …
>👇
### Fallback function

This function features the following aspects
1. unnamed
2. `external`-y called - cannot be called internally
3. maximum one instance per contract
4. automatically triggered when a contract calls an undefined function of enclosing smart contract
5. triggered if ETH is sent to the fallback’s enclosing contract
	-   there is no accompanying `calldata`
	- there is no `receive()` function declared—in this circumstance, a fallback must be marked payable for it to trigger and receive the ETH.
6. can include arbitrary logic in them

### Attack Process

The attack takes advantage of two features of fallback function. Additionally, it relies on a a certain order of operations in the victim contract.

![[../../resources/l9-reentrancy-attack.png]]
<blockquote>
	<p>Source: <a href="https://blog.chain.link/reentrancy-attacks-and-the-dao-hack/">Reentrancy Attacks and The DAO Hack Explained | Chainlink</a>
	<details>
		<summary>A re-entrancy attack occurs when:
			<ul>
				<li>A function <b>makes an external call to another untrusted contract.</b></li>
				<li>The untrusted contract <b>makes a recursive call back</b> to the original function in an attempt to drain funds.</li>
			</ul>
			<pre><p align="center">Expand to see explanation ▼</p></pre>
		</summary>
		
		<p>The hacker deploys a smart contract that acts as the “investor,” and this contract deposits some ETH into The DAO. This entitles the hacker to later call the <code>withdraw()</code> function in The DAO’s smart contract. When the <code>withdraw()</code> function is eventually called, The DAO’s contract sends ETH to the hacker. But the hacker’s smart contract intentionally does not have a <code>receive()</code> function, so when it receives ETH from the withdraw request, the hacker’s fallback function gets triggered. This fallback function could have been empty and still received the ETH, but instead it has some malicious code in it. </p>
		
		<p>This code, immediately upon execution, calls The DAO’s smart contract’s <code>withdraw()</code> function again. This sets off a loop of calls because at this point the first call to <code>withdraw()</code> is still executing. It will only finish executing when the hacker contract’s fallback function finishes, but that instead has re-called <code>withdraw()</code>, which kicks off a nested cycle of calls between the hacker contract and The DAO’s smart contract.</p>
		
		<p>Each time <code>withdraw()</code> is called, The DAO’s smart contract tries to send the hacker an amount of ETH equivalent to the hacker’s deposit. But, crucially, it does not update the hacker’s account balance until <em>after</em> the ETH-sending transaction finishes. But the ETH sending transaction cannot finish until the hacker’s fallback function finishes executing. So the DAO’s contract keeps sending more and more ETH to the hacker without decrementing the hacker’s balance—thus draining The DAO’s funds.</p>
</details>
</blockquote>
### Code walkthrough

See **slides** (p.9 - 12).

## Uninitialized Storage Pointer Attack

### Storage and Memory

>There are two main places where variables can be stored: `storage` and `memory`.

See [[Lecture 5#Data Storage|Lecture 5, Data Storage]]

- `Solidity` allows you to choose the type of storage with the help of `storage` and `memory` keywords. 
- A `storage` variable stores values **permanently**, whereas memory `variables` are persisted during the lifetime of a transaction. •
- Local variables of `struct`, `array`, or mapping type reference `storage` *by default* if no explicit specification is given inside a function. 
- The function arguments are always in `memory` and the local variables, other than array, struct, or mapping, are stored in the stack.

In `Solidity`, when dealing with complex data types (like structs or arrays), developers can work with either storage or memory variables. **However, if a developer declares a variable without initializing it with a specific data location (`storage` or `memory`)**, it might point to `storage` by default, leading to unexpected behaviours and vulnerabilities.

### Vulnerabilities

>A developer creates a function intending to work with a temporary memory structure, but forgets to explicitly declare the data location as `memory`

1. **`Unintentional Storage Overwrite`**

	The default storage pointer might be used, potentially **overwriting important stored data unintentionally**.

2. **`Manipulating Important Variables`**

	An attacker interacts with the function, providing inputs that manipulate the unintentionally *exposed storage variables*, **altering the contract’s behaviour or state in malicious ways.**

#### Code examples

See **slides** (p.17 - 24).

### Mitigation Strategies

>Understanding and mitigating such vulnerabilities is crucial for developing secure smart contracts and protecting them (and their users) against potential attacks.

- **Always Specify Data Location**: Developers should always specify the data location (`storage` or `memory`) to avoid unintentional default behaviours. 
- **Use a Checker**: Employing automated tools and checkers that can scan the code for common vulnerabilities, including uninitialized storage pointers, can be very helpful. 
- **Testing and Auditing**: Ensure thorough testing and preferably, a professional audit of the smart contract code to identify and fix potential vulnerabilities.