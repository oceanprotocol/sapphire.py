import ctypes
import platform

lib = None

if platform.system() == "Darwin":
    lib = ctypes.CDLL("./go/sapphirewrapper.dylib")

if platform.system() == "Windows":
    raise Exception("Windows is not supported")

if platform.system() == "Linux":
    lib = ctypes.CDLL("./go/sapphirewrapper.so")

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

def send_sapphire_tx(
    pk: bytes,
    sender: bytes,
    recipient: bytes,
    rpc_url: bytes,
    eth_amount: int,
    gas_price: int,
    data: str,
) -> int:
    return lib.SendETHTransaction(
        pk, sender, recipient, rpc_url, eth_amount, gas_price, data.encode("utf-8")
    )
