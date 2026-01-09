import hashlib, time 
 
# Stakeholder Registration 
stakeholders = {"farmer": "KYC123", "supplier": "KYC456", "retailer": "KYC789"} 
 
# Product Tagging 
product = {"batch_id": "BATCH1001", "history": []} 
 
# Blockchain basics 
blockchain = [] 
 
def create_hash(data, prev_hash="0"): 
    block_string = str(data) + prev_hash + str(time.time()) 
    return hashlib.sha256(block_string.encode()).hexdigest() 
 
def add_transaction(stakeholder, action): 
    # Verify stakeholder 
    if stakeholder not in stakeholders: 
        raise Exception("Unverified stakeholder!") 
 
    transaction = { 
        "time": time.ctime(), 
        "stakeholder": stakeholder, 
        "action": action, 
        "batch_id": product["batch_id"] 
    } 
    # Create hash + link to chain 
    prev_hash = blockchain[-1]["hash"] if blockchain else "0" 
    block = {"transaction": transaction, "prev_hash": prev_hash} 
    block["hash"] = create_hash(transaction, prev_hash) 
    blockchain.append(block) 
    product["history"].append(transaction) 
 
# Consensus Simulation 
def is_chain_valid(): 
    for i in range(1, len(blockchain)): 
        if blockchain[i]["prev_hash"] != blockchain[i-1]["hash"]: 
            return False 
    return True 
 
# Demo run 
add_transaction("farmer", "Harvested crop") 
add_transaction("supplier", "Transported to warehouse") 
add_transaction("retailer", "Placed on shelf") 
 
for block in blockchain: 
    print(block) 
 
print("Is blockchain valid?", is_chain_valid()) 
