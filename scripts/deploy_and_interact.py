from brownie import Unrelated
from scripts.tools import get_account


def deploy():
    account = get_account(id="Your id")
    unrelated_nfts = Unrelated.deploy(
        "Unrelated",
        "URTD",
        "https://arweave.net/i2UasvWWr_eFHYmOXU2yp3JYVn4WHIS9UxJqHit697w/",
        {"from": account},
    )


def mint():
    account = get_account(id="Your id")
    unrelated_nfts = Unrelated[-1]
    tx_mint = unrelated_nfts.mint(7, {"from": account})
    tx_mint.wait(1)


def main():
    deploy()
    mint()
