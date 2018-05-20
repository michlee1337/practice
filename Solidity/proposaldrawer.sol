pragma solidity ^0.4.19;

contract ProposalDrawer {
  event NewProposal(uint proposalId, string name);

  struct Proposal {
    string name;
  }

  Proposal[] public proposals;

  mapping (uint => address) public proposalToOwner;

  function _createProposal(string _name) private {
    uint id = proposals.push(Proposal)(_name)) -1;
    proposalToOwner[id] = msg.sender;
    NewProposal(id, _name);
  }
}
