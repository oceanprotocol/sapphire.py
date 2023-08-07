import os
import pytest
from sapphirepy import wrapper
from web3 import Web3

web3 = Web3()

@pytest.fixture
def test_private_key():
    private_key = os.environ.get("TEST_PRIVATE_KEY")
    if not private_key:
        raise Exception("TEST_PRIVATE_KEY environment variable not set.")
    return private_key


def test_send_encrypted_sapphire_tx(test_private_key):
    print(web3)
    account = web3.eth.account.from_key(test_private_key)

    sender = account.address
    recipient = "0x0000000000000000000000000000000000000000"
    rpc_url = "https://testnet.sapphire.oasis.dev"
    eth_amount = 1
    gas_limit = 50000
    data = ""

    result, tx_hash = wrapper.send_encrypted_sapphire_tx(
        test_private_key, sender, recipient, rpc_url, eth_amount, gas_limit, data, 0, 0
    )

    assert isinstance(result, int)
    assert result == 0
