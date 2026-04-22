import time
import random

def show_ledger_transactions():
    print("--- AKP OPEN LEDGER REAL-TIME MONITOR ---")
    print("Connecting to Decentralized Public Ledger...")
    time.sleep(1)
    
    categories = ["EDU_GRANT", "INFRA_REPAIR", "TECH_SUBSIDY", "HEALTH_PREVENTION", "SANITATION"]
    
    print(f"{'TIMESTAMP':<20} | {'CATEGORY':<20} | {'AMOUNT (AKC)':<12} | {'SENDER_DID'}")
    print("-" * 80)
    
    for _ in range(5):
        category = random.choice(categories)
        amount = round(random.uniform(500, 50000), 2)
        did = f"did:akp:{random.getrandbits(64):016x}..."
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"{timestamp:<20} | {category:<20} | {amount:<12} | {did}")
        time.sleep(0.5)

if __name__ == "__main__":
    show_ledger_transactions()
