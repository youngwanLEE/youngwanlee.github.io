from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import time
import random
import signal
import sys

# Timeout handler
def timeout_handler(signum, frame):
    print("Crawling timeout occurred")
    raise TimeoutError("Crawling is taking too long")

# Set 10-minute timeout
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(600)  # 10 minutes

def setup_scholarly_with_retry():
    """Setup scholarly with proxy and retry mechanism"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"Setting up proxy (attempt {attempt + 1}/{max_retries})...")
            
            # Try to set up free proxy for bot blocking avoidance
            pg = ProxyGenerator()
            pg.FreeProxies()
            scholarly.use_proxy(pg)
            
            print("Proxy setup completed successfully")
            return True
            
        except Exception as e:
            print(f"Proxy setup failed (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            
    print("All proxy attempts failed, using direct connection")
    return False

def fetch_citation_data(author_id):
    """Fetch citation data with error handling"""
    try:
        print(f"Searching for Google Scholar ID: {author_id}")
        author = scholarly.search_author_id(author_id)
        
        print("Retrieving author information...")
        # Only fetch basic info to improve speed (excluding publications)
        scholarly.fill(author, sections=['basics', 'indices', 'counts'])
        
        name = author['name']
        citations = author.get('citedby', 0)
        
        print(f"Author: {name}, Citations: {citations}")
        return author, citations
        
    except Exception as e:
        error_msg = str(e).lower()
        if any(keyword in error_msg for keyword in ['captcha', 'blocked', 'unusual traffic', 'recaptcha', 'too many requests']):
            print("Google Scholar bot blocking detected")
            raise Exception("CAPTCHA_BLOCKED")
        else:
            print(f"General crawling error: {e}")
            raise

try:
    # Setup with exponential backoff strategy
    setup_scholarly_with_retry()
    
    # Random delay to avoid bot detection (2-10 seconds)
    delay = random.uniform(2, 10)
    print(f"Waiting {delay:.1f} seconds to avoid bot detection...")
    time.sleep(delay)
    
    author_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'EqemKYsAAAAJ')
    
    # Fetch citation data with retry mechanism
    author, citations = fetch_citation_data(author_id)
    
    author['updated'] = str(datetime.now())
    
    os.makedirs('results', exist_ok=True)
    
    # Save complete data
    with open(f'results/gs_data.json', 'w') as outfile:
        json.dump(author, outfile, ensure_ascii=False, indent=2)
    
    # Save badge data for shields.io
    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{citations}",
    }
    
    with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)
    
    print("Citation update completed successfully!")
    
except TimeoutError as e:
    print(f"Timeout error: {e}")
    print("Consider increasing timeout or optimizing the crawling process")
    sys.exit(1)
    
except Exception as e:
    error_msg = str(e)
    print(f"Error during crawling: {error_msg}")
    
    # Detect CAPTCHA or blocking errors
    if "CAPTCHA_BLOCKED" in error_msg or any(keyword in error_msg.lower() for keyword in ['captcha', 'blocked', 'unusual traffic', 'recaptcha']):
        print("Google Scholar bot blocking detected - keeping existing data")
        print("This is expected behavior due to Google's anti-bot measures")
    else:
        print("General crawling error occurred")
    
    sys.exit(1)
    
finally:
    # Clear timeout signal
    signal.alarm(0)
