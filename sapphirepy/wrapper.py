import os
import ctypes
import platform
import sys

lib = None
bin_dir = os.path.join(sys.prefix, "sapphirepy_bin")
architecture = platform.machine()

if platform.system() == "Darwin":
    if architecture == "x86_64":
        lib_path = os.path.join(bin_dir, "sapphirewrapper-amd64.dylib")
        lib = ctypes.CDLL(lib_path)
    elif architecture == "arm64":
        lib_path = os.path.join(bin_dir, "sapphirewrapper-arm64.dylib")
        lib = ctypes.CDLL(lib_path)
    else:
        raise Exception(f"Unsupported architecture: {architecture}")

if platform.system() == "Windows":
    if architecture == "x86_64" or architecture.lower() == "amd64":
        lib_path = os.path.join(bin_dir, "sapphirewrapper-amd64.dll")
        lib = ctypes.CDLL(lib_path)
    else:
        raise Exception(f"Unsupported architecture: {architecture}")

if platform.system() == "Linux":
    if architecture == "x86_64":
        lib_path = os.path.join(bin_dir, "sapphirewrapper-amd64.so")
        lib = ctypes.CDLL(lib_path)
    elif architecture == "aarch64" or architecture == "amd64":
        lib_path = os.path.join(bin_dir, "sapphirewrapper-arm64.so")
        lib = ctypes.CDLL(lib_path)
    else:
        raise Exception(f"Unsupported architecture: {architecture}")


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


class SendETHTransactionResult(ctypes.Structure):
    _fields_ = [("resultCode", ctypes.c_int), ("resultStr", ctypes.c_char_p)]


# Define return type
lib.SendETHTransaction.restype = SendETHTransactionResult


def send_encrypted_sapphire_tx(
    pk: str,
    sender: str,
    recipient: str,
    rpc_url: str,
    eth_amount: int,
    gas_limit: int,
    data: str,
    gas_cost_gwei: int,
    nonce: int,
) -> tuple:
    result = lib.SendETHTransaction(
        pk.encode("utf-8"),
        sender.encode("utf-8"),
        recipient.encode("utf-8"),
        rpc_url.encode("utf-8"),
        eth_amount,
        gas_limit,
        data.encode("utf-8"),
        gas_cost_gwei,
        nonce,
    )
    return (
        result.resultCode,
        result.resultStr.decode("utf-8") if result.resultStr is not None else None,
    )
