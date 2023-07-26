package main

// #cgo CFLAGS: -I.
// #cgo LDFLAGS: -L. -lsapphirewrapper
// #include "sapphirewrapper.h"
// #include <stdlib.h>

import (
	"C"
	"context"
	"math/big"

	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/ethclient"
	sapphire "github.com/oasisprotocol/sapphire-paratime/clients/go"
)
import (
	"encoding/hex"
	"fmt"
)

//export SendETHTransaction
func SendETHTransaction(keyHexC *C.char, myAddrC *C.char, toAddrC *C.char, rpcUrl *C.char, valueC C.int, gasLimitC C.int, dataC *C.char) C.int {
	keyhex := C.GoString(keyHexC)
	myAddrStr := C.GoString(myAddrC)
	toAddrStr := C.GoString(toAddrC)
	rpcUrlStr := C.GoString(rpcUrl)
	gasLimit := uint64(gasLimitC)
	datahex := C.GoString(dataC)

	value := big.NewInt(int64(valueC))
	value = value.Mul(value, big.NewInt(1000000000)) // convert gwei to wei

	c, err := ethclient.Dial(rpcUrlStr)
	if err != nil {
		return -1
	}

	key, err := crypto.HexToECDSA(keyhex)
	if err != nil {
		return -2
	}

	myAddr := common.HexToAddress(myAddrStr)
	toAddr := common.HexToAddress(toAddrStr)

	nonce, err := c.PendingNonceAt(context.Background(), myAddr)
	if err != nil {
		return -3
	}

	chainId, err := c.NetworkID(context.Background())
	if err != nil {
		return -4
	}

	var data []byte
	if datahex == "" {
		data = nil
	} else {
		// remove 0x if it exists
		if datahex[:2] == "0x" {
			datahex = datahex[2:]
		}

		data, err = hex.DecodeString(datahex)
		if err != nil {
			return -42
		}
		cipher, _ := sapphire.NewCipher(chainId.Uint64())
		data = cipher.EncryptEncode(data)
	}

	fmt.Println("data", data)

	gasPrice, err := c.SuggestGasPrice(context.Background())
	tx := types.NewTx(
		&types.LegacyTx{
			Nonce:    nonce,
			To:       &toAddr,
			Value:    value,
			Data:     data,
			Gas:      gasLimit,
			GasPrice: gasPrice,
		},
	)

	signedTx, err := types.SignTx(tx, types.LatestSignerForChainID(chainId), key)
	if err != nil {
		return -5
	}

	err = c.SendTransaction(context.Background(), signedTx)
	if err != nil {
		fmt.Println(err)
		return -6
	}

	return 0
}

func main() {}
