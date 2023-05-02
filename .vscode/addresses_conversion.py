# I want one of this addresses converted

# C ADDRESS: 14EWK38NoTu8MDeCf5zWWjXyE7F4xU9S9S

# Or

# UC ADDRESS: 1AfaeyabCd51T45Sg7TdFsYJ2feBxBuJ7X

# to this:

# 2203c6eae793d27105b3ed165ca7fa76360e9d05e2f3
import base58

def bitcoin_to_hex(address):
    version = 0
    # Decode base58 address
    decoded = base58.b58decode(address).hex()
    # Extract public key hash and version bytes
    pubkey_hash = decoded[2:-8]
    verbyte_pubkey_hash = decoded[:2]
    # Check that the decoded version byte matches the expected version byte
    if int(verbyte_pubkey_hash, 16) != version:
        raise ValueError("Invalid version byte")
    return pubkey_hash

c_address = "14EWK38NoTu8MDeCf5zWWjXyE7F4xU9S9S"
uc_address = "1AfaeyabCd51T45Sg7TdFsYJ2feBxBuJ7X"

c_public_key = bitcoin_to_hex(c_address)
uc_public_key = bitcoin_to_hex(uc_address)

print(c_public_key)
print(uc_public_key)
