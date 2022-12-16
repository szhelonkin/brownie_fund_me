from brownie import network, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["ganache-local", "development"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]

def get_account():
	if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
		return accounts[0]
	else:
		return accounts.load("acc1")

def deploy_mocks():
	print(f"The active network is {network.show_active()}")
	print("Deploying Mocks...")
	if len(MockV3Aggregator) == 0:
		mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
	print("Mocks deployed!")
