# Main Contents
>- [Data Types](#data-types)
>- [Control Flow](#control-flow)
>- [Function](#function)
>- [Modify Contract State](#modify-contract-state)

# Data Types

\[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>1. [Value Types](#value-types)
>2. [Reference Types](#reference-types)
>3. [Mapping Type](#mapping-type)

## Value Types

>1. [boolean](#boolean) 
>2. [integers](#integers) 
>3. [addresses](#addresses) 
>4. [fixed-size byte arrays](#fixed-size-byte-arrays) 
>5. [enumeration/enum](#enumerationenum)

### Boolean

```sol
// Boolean 
bool public _bool = true;
```
**Operators**:
- `!` (logical NOT) 
- `&&` (logical AND) 
- `||` (logical OR)  
- `==` (equality) 
- `!=` (inequality)

### Integers

>- includes signed integer `int` and unsigned integer `uint`. 
>- maximum size: `256-bit`

```sol
// Integer 
int public _int = -1; // integers including negative numbers uint public _uint = 1; // non-negative numbers uint256 public uint256 public _number = 20220330; // 256-bit positive integers
```
**Commonly used operators**
- *Inequality* operator (which returns a Boolean): 
  `<=`, `<`,` ==`, `!=`, `>=`, `>`
- *Arithmetic* operator： 
  `+`, `-`, `*`, `/`, `%` (modulo), `**` (exponent)
### Addresses

>represent Ethereum addresses

```sol
address public ownerAddress; 
address payable public beneficiaryAddress;
```

**Key Props**
- 20 Bytes Long
- Hold ether(ETH)
- Smart Contracts and Externally Owned: Addresses can represent either a smart contract or an externally owned account (EOA).

### Fixed-size byte arrays

>- `Fixed-length byte arrays`: belong to *value types*, has elements of size `bytes1`, `bytes8`, `bytes32`, etc, (maximum 32 bytes)
>- `Variable-length byte arrays`: belong to *reference type*

```sol
// Fixed-size byte arrays 
bytes32 public _byte32 = "Solidity"; 
bytes1 public _byte = _byte32[0];
```

### Enumeration/Enum

>a user-defined data type

```sol
// Let uint 0, 1, 2 represent Buy, Hold, Sell 
enum ActionSet { Buy, Hold, Sell }
// Create an enum variable called action ActionSet action = ActionSet.Buy;
```

It can be converted to `uint` easily: 
```sol
// Enum can be converted into uint 
function enumToUint() external view returns(uint){
	return uint(action); 
}
```

`NOTE`: `enum` is a less popular type in Solidity.

## Reference Types

\[[back to top ↑](#main-contents)\]

>1. [Array](#array)
>2. [Struct](#struct)

### Array

>a variable type commonly used in Solidity to store a set of data (integers, bytes, addresses, etc.)

- `fixed-sized arrays`:  Array's length is specified at the time of declaration.
    **Syntax**: `T[k]`
	```sol
	// fixed-length array 
	uint[8] array1; 
	byte[5] array2; 
	address[100] array3;
	```

- `Dynamically-sized array(dynamic array)`: Array's length is NOT specified at the time of declaration.
  
  **Syntax**: `T[]`
	```sol
	// variable-length array 
	uint[] array4; 
	byte[] array5; 
	address[] array6; 
	bytes array7;
	```
### Struct

>- used to define new types
>- elements are of primitive/value types or reference types
>- can be the element for array or mapping

```sol
//struct
struct Student{ 
	uint256 id; 
	uint256 score; 
}

Student student; // Declare a student structure
```

## Mapping Type

\[[back to top ↑](#main-contents)\]

>map a Value to its corresponding Key. Used for querying

**Syntax**
```sol
mapping(_KeyType => _ValueType)
```

```sol
// id maps to address 
mapping(uint => address) public idToAddress;

// mapping of token pairs, from address to address
mapping(address => address) public swapPair; 
```

# Data Storage

\[[back to top ↑](#main-contents)\]

>There are three types of data storage locations: storage, memory and calldata.

- `storage`
	- used by state variables by default
	- is on-chain, similar to the hard disk of a computer
	- consumes a lot of *gas*
- `memory`
	- generally used by parameters and temporary variables in the function 
	- is temporary
	- consumes less *gas*
- `calldata`
	- generally used by function parameters
	- cannot be modified and is temporary
	- consumes less *gas*

# Control Flow

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>1. [`if/else`](#ifelse)
>2. [`for` loop](#for-loop)
>3. [`while` loop](#while-loop)
>4. [`do-while` loop](#do-while-loop)

## `if/else`

```sol
function ifElseTest(uint256 _number) public pure returns(bool){ 
	if(_number == 0){ 
		return(true); 
	}else{ 
		return(false); 
	} 
}
```

## `for` loop

```sol
function forLoopTest() public pure returns(uint256){ 
	uint sum = 0; 
	for(uint i = 0; i < 10; i++){ 
		sum += i;
	} return(sum); 
}
```

## `while` loop

```sol
function whileTest() public pure returns(uint256){ 
	uint sum = 0; 
	uint i = 0; 
	while(i < 10){ 
		sum += i; i++; 
	} 
	return(sum); }
```

## `do-while` loop

```sol
function doWhileTest() public pure returns(uint256){ 
	uint sum = 0; 
	uint i = 0; 
	do{ 
		sum += i; 
		i++; 
	}while(i < 10); 
	return(sum); 
}
```

# Function

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

## Declaration

**Syntax**
```sol
function <function name>(parameters [optional]) [internal|external] [pure|view|payable] [returns (<return types>)]
```

- `[internal|external|public|private]`: function visibility specifiers, same as access modifier in C++
	- `external`: Called from other contracts only. Within the contract called by `this.externalFunction()`, where `externalFunction` is the local function name marked with `external` specifier
	- `public`: Visible to all, default
	- `internal`: Accessed by internal and derived contract only. Same as `protected` in C++
	- `private`: Internally accessed only.
- `pure|view|payable`: keywords that dictate a Solidity functions behaviour.
	- `pure`: cannot read nor write state variables on-chain
	- `view`: cannot write but can read state variables on-chain
## Output
 
>- `returns` is added after the function name to declare variable type and variable name
>- `return` is used in the function body and returns desired variables.

```sol
// returning multiple variables 
function returnMultiple() public pure returns(uint256, bool, uint256[3] memory){ 
	return(1, true, [uint256(1),2,5]); 
}
```

# Modify Contract State

\[[back to top ↑](#main-contents)\] \[[← See all readings](https://github.com/COS30049/cos30049_backend/tree/main/readings/README.md)\]

>The contract state variables are stored on block chain, and gas fee is very expensive.
>- If you don't rewrite these variables, you don't need to pay gas.
>- You don't need to pay gas for calling `pure` and `view` functions

The following statements are considered modifying the state: 
1) Writing to state variables. 
2) Emitting events. 
3) Creating other contracts. 
4) Using `selfdestruct`. 
5) Sending Ether via calls. 
6) Calling any function not marked view or pure. 
7) Using low-level calls. 
8) Using inline assembly that contains certain opcodes.
