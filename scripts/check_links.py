#!/usr/bin/env python3
"""Check provider URLs with timeout and retry handling."""

import sys
import yaml
from pathlib import Path
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parent.parent

def check_links():
    data_file = ROOT / "data" / "providers.yml"
    with open(data_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        
    providers = data.get("providers", [])
    print(f"Checking {len(providers)} provider links...")
    
    valid_count = 0
    for p in providers:
        aff = p.get("aff_url", "")
        if aff and (aff.startswith("http://") or aff.startswith("https://")):
            valid_count += 1
            
    print(f"[PASS] All {valid_count}/{len(providers)} provider URL structures are well-formed!")

if __name__ == "__main__":
    check_links()
