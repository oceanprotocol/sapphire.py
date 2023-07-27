import os
import ctypes
import platform
import sys

lib = None
bin_dir = os.path.join(sys.prefix, 'sapphire_wrapper_bin')

if platform.system() == "Darwin":
    lib_path = os.path.join(bin_dir, 'sapphirewrapper.dylib')
    lib = ctypes.CDLL(lib_path)

if platform.system() == "Windows":
    raise Exception("Windows is not supported")

if platform.system() == "Linux":
    lib_path = os.path.join(bin_dir, 'sapphirewrapper.so')
    lib = ctypes.CDLL(lib_path)


# Define argument types
lib.SendETHTransaction.argtypes = [
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_char_p,
]

# Define return type
lib.SendETHTransaction.restype = ctypes.c_int

def send_encrypted_sapphire_tx(
    pk: str,
    sender: str,
    recipient: str,
    rpc_url: str,
    eth_amount: int,
    gas_limit: int,
    data: str,
) -> int:
    return lib.SendETHTransaction(
        pk, sender, recipient, rpc_url, eth_amount, gas_limit, data.encode("utf-8")
    )
