# sapphirepy

Python wrapper for sending encrypted transactions on Oasis Sapphire network

## Installation

To install the package, you can either use PyPI or install from source:

### PyPI

To install from PyPI, you can simply run the following command:

```shell
pip install sapphirepy
```

### From Source

Alternatively, to install from the source, clone the repository and navigate into the directory:

```shell
git clone https://github.com/oceanprotocol/sapphirepy.git
cd sapphirepy
```

Then, you can install it using pip:

```shell
pip install .
```

## Usage

To use the package, you need to import the `wrapper` module and call the `send_encrypted_sapphire_tx` function.

```python
from sapphirepy import wrapper

response = wrapper.send_encrypted_sapphire_tx(
    pk,        # Your private key as a string
    sender,    # Sender's address as a string
    recipient, # Recipient's address as a string
    rpc_url,   # RPC URL for the network as a string
    eth_amount,# Amount of GWEI to send as an integer
    gas_limit, # Gas limit for the transaction as an integer
    data,      # Transaction data as a string
)
```

### Return Value

The function `send_encrypted_sapphire_tx` will return 0 if the transaction has been successfully sent, otherwise it will return an error code corresponding to the issue encountered.