#!/usr/bin/env python3
"""Validate providers.yml schema and integrity."""

import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

def validate_data():
    data_file = ROOT / "data" / "providers.yml"
    if not data_file.exists():
        print(f"ERROR: {data_file} not found")
        sys.exit(1)
    
    with open(data_file, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except Exception as e:
            print(f"ERROR: YAML parsing failed: {e}")
            sys.exit(1)
            
    providers = data.get("providers", [])
    if not providers:
        print("ERROR: No providers found in data file")
        sys.exit(1)
        
    print(f"[OK] Successfully loaded {len(providers)} providers from {data_file.name}")
    
    required_fields = ["id", "name", "category", "line_type", "protocols", "price_starting", "aff_url", "score"]
    errors = []
    
    for i, p in enumerate(providers, 1):
        for field in required_fields:
            if field not in p or not p[field]:
                errors.append(f"Provider #{i} ({p.get('name', 'Unknown')}) missing required field: '{field}'")
                
    if errors:
        print(f"Validation FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
        
    print("[PASS] All provider data schemas validated successfully with 0 errors!")

if __name__ == "__main__":
    validate_data()
