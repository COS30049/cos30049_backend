## Main Contents
1. [Modifiers](#modifiers)
2. [Events](#events)
3. [Inheritance](#inheritance)
4. [Libraries](#libraries)
5. [Import](#import)
6. [Error handling](#error-handling)
7. [Overloading](#overloading)

Jump to important links:
1. [ERC](#see-ethereum-request-for-comment-erc-)

## Modifiers

\[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>- a special type of function that declares characteristics that a function possesses.
>- primary use case is to **perform checks** before running a function, such as checking addresses, variables, balances, etc.

```sol
// define modifier
modifier onlyOwner {
   require(msg.sender == owner);
   _;
}

function changeOwner(address _newOwner) external onlyOwner public {
       owner = _newOwner;
   }
```
>**Explanation**
>
>The `onlyOwner` modifier has no parameters and includes a `require` statement that checks that the message sender is the contract owner.
>
>If the message sender is the contract owner, the function will be executed. If the message sender is not the contract owner, the function will not execute.

## Events

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

### Declaration

> Events are declared with the `event` keyword, followed by event name, then the type and name of each parameter to be recorded. 

```sol
// Transfer event from the ERC20 token contract
event Transfer(address indexed from, address indexed to, uint256 value);
```

>Parameters marked with `indexed` will be stored at a special data structure known as **topics** and easily queried by programs

### Emission

>use keyword `emit` followed by an event name defined before that along with parameters if applicable.

```sol
contract Owner {
	address private owner;

	// event for EVM logging
	event OwnerSet(address indexed oldOwner, address indexed newOwner);

	// modifier to check if caller is owner
	modifier isOwner() {
		// If the first argument of 'require' evaluates to 'false', execution terminates and
		// changes to the state and Ether balances are reverted.
		// This used to consume all gas in old EM version, but not anymore
		// It is often a good idea to use 'require' to check if functions are called correctly.
		// As a second argument, you can also provide an explanation about what went wrong
		require(msg.sender == owner, "Caller is not owner");
		_;
	}

	/**
	 * @dev Set contract deployer as owner
	 */
	 constructor() {
		 console.log("Owner contract deployed by:", msg.sender);
		 owner = msg.sender; // 'msg.sender' is sender of current call, contract deployer for a constructor
		 emit OwnerSet(address(0), owner);
	 }
	...
}
```

## Inheritance

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>a mechanism where you can derive a class from another class for a hierarchy of classes that share a set of attributes and methods

```sol
mapping(address => uint256) public override balanceOf;
```

There are two important keywords for inheritance:
- `virtual`: used by functions in parent contracts that are **expected to be overridden** in its child contracts.
- `override`: used by functions in child contracts that are **expected to override** those in their parent contract.

```sol
contract GrandFather {
    event Log(string msg);
	// Apply inheritance to the follwing 3 functions
	function hip() puclic virtual{
		emit Log("Grandfather");
	}
	
	function pop() public virtual{
		emit Log("Grandfather");
	}

	function Grandfather() public virtual{
		emit Log("Grandfather");
	}
}

contract Father is Grandfather{
	// Apply inheritance to the following 2 functions
    function hip() public virtual override{
	    emit Log("Father");
    }
    
	function hip() public virtual override{
	    emit Log("Father");
    }

	function hip() public virtual{
	    emit Log("Father");
    }
}
```

### Multiple Inheritance

\[[back to top ↑](#main-contents)\]

>- When inheriting, you should follow the order from **highest to lowest seniority**.
>- If a function exists in multiple inherited contracts, it must be overridden in the child contract; otherwise, an error will occur.
>- When overriding a function that has the same name in multiple parent contracts, the override keyword should be followed by the names of all parent contracts.

```sol
contract Son is Grandfather, Father{
	function hip() public virtual override(Grandfather, Father){
		emit Log("son");
	}

	function pop() public virtual override(GrandFather, Father){
		emit Log("Son");
	}
}
```

### Call from Parent Contracts

\[[back to top ↑](#main-contents)\]

>`Direct invocation`: directly call a function from a parent contract using the syntax `ParentContractName.functionName()`.
>
>`super keyword`: used to call  a function from the immediate parent contract. 

```sol
function callParent() public {
	Grandfather.pop();
}

function callParaSuper() public{
	// This will call the function from the immediate parent contract.
	super.pop();
}
```

### Abstract

\[[back to top ↑](#main-contents)\]

>- used when there's at least one unimplemented function, otherwise the contract will not compile
>- unimplemented function needs to bel marked as `virtual`

```sol
pragma solidity ^0.8.0;

// Define an abstract contract
abstract contract AbstractContract {
	// Declare an abstract function
	function doWork() public virtual returns(uint);
}

contract ConcreteContract is AbstractContract {

	// Implement the abstract function in the derived contract
	function doWork() public override returns (uint) {
		// Logic of the function
		uint workDone = 10;
		return workDone;
	}	
}
```

### Interface

\[[back to top ↑](#main-contents)\]

>- `semantics`: a skeleton of smart contracts that defines what the contract does and how to interact with them
>- `syntax`: similar to abstract contract but requires no function implementations.

**Rules of Interface**:
- No state variables
- No constructors
- Cannot inherit non-interface contracts
- All functions must be `external`
- Inherited contracts must implement all the functions declared

>if a smart contract implements an interface (like ERC20 or ERC721), other Dapps and smart contracts will know how to interact with it. Because it provides two important pieces of information: 
>- The bytes4 selector for each function in the contract, and the function signatures function name (parameter type). 
>- Interface id (see [EIP165](https://eips.ethereum.org/EIPS/eip-165) for more information)

#### When to use?

>If we know that a contract implements the IERC721 interface, we can interact with it without knowing its detailed implementation.

```sol
contract interactBAYC {
	// Use BAYC address to create interface contract variables (ETH Mainnet)
	IERC721 BAYC IERC721(0xBC4CA0EdA7647A8aB7C2061cE118A18a936f13D);

	// Call BAYC's balanceOf() to query the open interest through the interface
	function balanceOfBAYC(affress owner) external view returns (uint256 balance){
		return BAYC.balanceOf(owner);
	}

	// Safe transfer by calling BAYC's safeTransferFrom() through the interface
	function safeTransferFromBAYC(address from, address to, uint256 tokenId) external{
		BAYC.safeTransferFrom(from, to, tokenId);	
	}
}
```
>The Bored Ape Yacht Club BAYC is an ERC721 NFT, which implements all functions in the IERC721 interface. We can interact with the BAYC contract with the IERC721 interface and its contract address, without knowing its source code. For example, we can use `balanceOf()` to query the BAYC balance of an address, or use `safeTransferFrom()` to transfer a BAYC NFT.
#### See [Ethereum request for comment (ERC)](https://eips.ethereum.org/erc) [\[↑\]](#main-contents)

## Libraries 

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

> - special type of contract, designed to enhance the reusability of Solidity code and reduce gas consumption
> - typically consist of a collection of useful functions

```sol
library Strings {
	bytes16 private constant _HEX_SYMBOLS = "0123456789abcdef";

	/*
	 * @dev Converts a 'uint256' to uts ASCII 'string' decimal representation.
	 */
	 function toString(uint256 value) public pure returns (string memory) {
		// Inspired by OraclizeAPI's implementation - MIT licence

		if (value == 0) {
			return "0";
		}
		uint256 temp = value;
		uint256 digits;
		while (temp != 0) {
			digits++;
			temp /= 10;
		}
		bytes memory buffer = new bytes(digits);
		while (value != 0) {
			digits -= 1;
			buffer[digits] = bytes1(uint8(48 + uint256(value %10)));
		}
		return string(buffer)
	}
	...
}
```

### How to Use

\[[back to top ↑](#main-contents)\]

#### Using the `using for` directive

>The directive 'using A for B;' is used to attach library functions (from library A) to any type (B). After the directive is added, the functions in library A are automatically added as members of the B type variable and can be called directly. ***Note: when called, this variable will be passed as the first argument to the function***

```sol
using Strings for uint256; function getString1(uint256 _number) public pure returns(string memory){ 
	return _number.toHexString(); 
}
```

#### Calling library functions through the library contract's name

>You can also call a library function directly using the name of the library contract. In this case, you would use the name of the library, followed by the function you want to call.”

```sol
function getString2(uint256 _number) public pure returns(string memory){ 
	return Strings.toHexString(_number); 
}
```
## Import

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>Use `import` to import contracts from other source codes, making development more modular. Syntax is pretty much the same as `JS`

- **import by *using the relative position* of the source file**
	```sol
	import './father.sol';
	```

-  **import contracts *from the internet* by using the source file's URL**
	```sol
	import 'https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/Address.sol’;
	```

- **import via *the npm directory***
	```sol
	import '@openzeppelin/contracts/access/Ownable.sol';
	```

- **import specific contracts via *global symbols*** 
	```sol
	import {father} from './father.sol';
	```

## Error Handling

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

### `error`
>- a new feature in solidity 0.8 that saves gas and informs users why the operation failed
>- recommended way to throw error in solidity
>- Custom errors are defined using the `error` statement, which can be used inside and outside of contracts.
>- ⚠️ In functions, `error` must be used together with `revert` statement.

```sol
error TransferNotOwner(); // custom error revert TransferNotOwner();
```

### `require`
>most commonly used method for error handling prior to solidity 0.8

```sol
require(condition, "error message");
```


### `assert`
>generally used for debugging purposes

```sol
assert(condition);
```

## Overloading

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>- **functions** can be overloaded only
>- **modifiers** cannot be overloaded

```sol
pragma solidity ^0.8.4

contract OverloadingExample {
	// First saySomething function with no paramters
	function saySomething() public pure returns(string memory) {
		return "Nothing";
	}

	// Overloaded saySomething function that takes a string parameter
	function saySomething(string memory _message) public pure returns(string memory) {
		return _message;
	}

}
```
