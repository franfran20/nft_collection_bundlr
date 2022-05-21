from brownie import accounts, network

# helper function for switching between development and mainnet accounts easily..
def get_account(id=None, index=None):
    if network.show_active() == "development":
        return accounts[0]
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]
