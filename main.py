#consists block
#block consist transaction
#blocks are connected through hashing

    #unique digital fingerprint - transacton + previous fingerprint

from Block import Block

blockchain = []

genesis_block = Block("0", ["Satoshi sent 1 BTC to Ivan", "Satoshi sent 5 BTC to Finney"])

second_block = Block(genesis_block.block_hash, ["Ivan sent 55 BTC to Lizz"])

third_block = Block(second_block.block_hash, ["A to D 5 BTC", "Ivan sent 10 BTC"])

print("Block hash:")
print(genesis_block.block_hash)

print("Second hash:")
print(second_block.block_hash)

print("Third hash:")
print(third_block.block_hash)