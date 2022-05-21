import pytest
from brownie import Unrelated
from scripts.tools import get_account


def test_can_successfully_mint():
    account = get_account()
    unrelated_nfts = Unrelated.deploy(
        "Unrelated",
        "URTD",
        "https://arweave.net/i2UasvWWr_eFHYmOXU2yp3JYVn4WHIS9UxJqHit697w/",
        {"from": account},
    )
    tx_mint = unrelated_nfts.mint(10, {"from": account})
    tx_mint.wait(1)

    assert unrelated_nfts.balanceOf(account.address) == 10
    assert (
        unrelated_nfts.baseURI()
        == "https://arweave.net/i2UasvWWr_eFHYmOXU2yp3JYVn4WHIS9UxJqHit697w/"
    )


# images folder link... https://arweave.net/G5xJ3J7eZhOhPVsLsAZ8VFWZDesTuwgnYaLblpdxRS4

# metadata folder link... https://arweave.net/i2UasvWWr_eFHYmOXU2yp3JYVn4WHIS9UxJqHit697w
