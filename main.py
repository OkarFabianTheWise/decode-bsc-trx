from web3 import Web3
from utils import hash_to_json, to_checksum_address
BSCend_point = "https://bsc-dataseed.binance.org/"
w3Bsc = Web3(Web3.HTTPProvider(BSCend_point))

def encode_data(data):
    # Convert the bytes objects to hexadecimal strings for serialization
    encoded_data = [item.hex() if isinstance(item, bytes) else item for item in data]
    return encoded_data

def multicall_to_json(data):
    # Convert the problematic data to a serializable format
    encoded_data = encode_data(data)

    # Create a dictionary representing the data
    json_data = {
        "data": encoded_data
    }

    # Encode the dictionary to JSON
    json_string = json_data

    return json_string

def bsc_decode(trxhash):
    try:
        contract = w3Bsc.eth.contract(address=pscV3_address, abi=abis.pcs_v3_router_abi)
        input_ = w3Bsc.eth.get_transaction(hash_to_json(trxhash)).input
        result = contract.decode_function_input(hash_to_json(input_))
        data = result[1]['data']
        decode_multicall = multicall_to_json(data)["data"]
        # remove [''] from the data
        extract = ''.join(decode_multicall)
        value = contract.decode_function_input(extract)
        return value
    except Exception as x:
        print("decode error",x)
