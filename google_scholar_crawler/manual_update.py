#!/usr/bin/env python3
"""
Manual backup script for updating Google Scholar citations
when the automated GitHub Action fails.

Usage: python manual_update.py [scholar_id]
"""
import json
import sys
import os
from datetime import datetime

def manual_update_citations(scholar_id=None, citation_count=None):
    """Manually update citation count when automated crawling fails"""
    
    if scholar_id is None:
        scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'EqemKYsAAAAJ')
    
    if citation_count is None:
        try:
            citation_count = int(input("Enter the current citation count from Google Scholar: "))
        except (ValueError, KeyboardInterrupt):
            print("Invalid input or cancelled.")
            return False
    
    # Create the shield.io data
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations", 
        "message": str(citation_count)
    }
    
    # Create results directory if it doesn't exist
    os.makedirs('results', exist_ok=True)
    
    # Save the data
    with open('results/gs_data_shieldsio.json', 'w') as f:
        json.dump(shieldio_data, f, ensure_ascii=False)
    
    print(f"✓ Manual citation update completed!")
    print(f"Citation count: {citation_count}")
    print(f"Scholar ID: {scholar_id}")
    print(f"Updated at: {datetime.now()}")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
            manual_update_citations(citation_count=count)
        except ValueError:
            # Assume it's a scholar ID
            manual_update_citations(scholar_id=sys.argv[1])
    else:
        manual_update_citations()