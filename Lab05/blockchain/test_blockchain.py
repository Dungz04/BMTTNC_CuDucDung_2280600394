from blockchain import Blockchain


# Tạo blockchain
my_blockchain = Blockchain()

# Thêm các giao dịch
my_blockchain.add_transaction('Dũng', 'Hiếu', 50)
my_blockchain.add_transaction('Hiếu', 'Jake', 10)
my_blockchain.add_transaction('Jake', 'Dũng', 99)

# Đào block mới
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

# Thưởng cho người đào
my_blockchain.add_transaction('Genesis', 'Miner', 1)

# Tạo block mới
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị toàn bộ blockchain
for block in my_blockchain.chain:
    print(f"\n🧱 Block #{block.index}")
    print("🕒 Thời gian:", block.timestamp)
    print("📦 Giao dịch:", block.transactions)
    print("🧪 Bằng chứng:", block.proof)
    print("🔗 Hash trước:", block.previous_hash)
    print("🔐 Hash hiện tại:", block.hash)
    print("-------")

# Kiểm tra tính hợp lệ
print("\n✅ Chuỗi blockchain hợp lệ" if my_blockchain.is_chain_valid(my_blockchain.chain) else "\n❌ Chuỗi blockchain không hợp lệ.")
