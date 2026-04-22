import json

def calculate_vote_weight(citizen_did_path, law_scope):
    with open(citizen_did_path, 'r') as f:
        citizen_data = json.load(f)
    
    base_weight = 1.0
    merit_bonus = 0.0
    
    # Check if citizen has competencies in the law's scope
    for competence in citizen_data.get('competencies', []):
        if competence['field'] == law_scope:
            merit_bonus = competence['weight'] - 1.0
            print(f"[FOUND] Competence in {law_scope}: +{merit_bonus:.2f} weight bonus.")
            break
            
    total_weight = base_weight + merit_bonus
    print(f"Citizen DID: {citizen_data['did']}")
    print(f"Law Scope: {law_scope}")
    print(f"Final Vote Weight: {total_weight:.2f}x")
    return total_weight

if __name__ == "__main__":
    # Mock Citizen with Expertise in Economy
    mock_citizen = {
        "did": "did:akp:7f8e9a...abc123",
        "merit_score": 450,
        "competencies": [
            {"field": "ECONOMY", "weight": 2.5, "verified_by": "AKP-ECON-MODULE"},
            {"field": "TECH", "weight": 1.2, "verified_by": "UNIVERSITY-GLOBAL"}
        ]
    }
    
    # Save mock citizen temporarily
    with open('citizen_mock.json', 'w') as f:
        json.dump(mock_citizen, f)
        
    calculate_vote_weight('citizen_mock.json', 'ECONOMY')
    calculate_vote_weight('citizen_mock.json', 'JUSTICE') # No expertise here
