// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Asset {
    // State Variables
    uint256 priceInWei;

    event receiveMoney(uint value);
    event withdrawnSucess(bytes data);
    event transferOwnerSuccess(address newOwner, address contractAddress);

    // Struct
    struct Owner {
        address payable userAddress;
    }

    // Public State Variables
    Owner[] public owners;

    constructor(uint256 _weiPrice) {
        Owner memory newOwner = Owner(payable(msg.sender));
        owners.push(newOwner);
        priceInWei = _weiPrice;
    }

    // Functions
    function getLatestOwner() public view returns (Owner memory) {
        uint numberOfOwners = owners.length;
        return owners[numberOfOwners - 1];
    }

    function getAllOwner() public view returns (Owner[] memory) {
        return owners;
    }

    function retrieve() public view returns(address) {
        return address(this);
    }

    function getBalance() external view returns (uint) {
        return address(this).balance;
    }

    receive() external payable {
        require(msg.value >= priceInWei, "Not enough money");
        withdraw();
        addNewOwner(msg.sender);
        emit receiveMoney(msg.value);
    }

    function withdraw() public payable {
        (bool sent, bytes memory data) = payable(getLatestOwner().userAddress).call{value: this.getBalance()}("");
        require(sent, "Unable to sent ether");
        emit withdrawnSucess(data);
    }

    function addNewOwner(address _newUserAddress) private  {
        Owner memory newOwner = Owner(payable(_newUserAddress));
        owners.push(newOwner);
    }
}
