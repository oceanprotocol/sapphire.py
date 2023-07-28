import os
import pytest
from sapphire_wrapper import wrapper

@pytest.fixture
def test_private_key():
    private_key = os.environ.get("TEST_PRIVATE_KEY")
    if not private_key:
        raise Exception("TEST_PRIVATE_KEY environment variable not set.")
    return private_key

def test_send_encrypted_sapphire_tx(test_private_key):
    sender = "0x004524Ed90FF62F0E8198734C8B48F78b5AC608f"
    recipient = "0x0000000000000000000000000000000000000000"
    rpc_url = "https://testnet.sapphire.oasis.dev"
    eth_amount = 1
    gas_limit = 50000
    data = ""

    result = wrapper.send_encrypted_sapphire_tx(
        test_private_key,
        sender,
        recipient,
        rpc_url,
        eth_amount,
        gas_limit,
        data,
    )

    assert isinstance(result, int)
    assert result == 0
