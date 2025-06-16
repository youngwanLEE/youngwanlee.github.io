from scholarly import scholarly
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

# Set 8-minute timeout (reduced from 10 minutes)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(480)  # 8 minutes

def setup_scholarly():
    """Setup scholarly with basic configuration"""
    try:
        # For now, skip proxy setup due to API compatibility issues
        # Focus on direct connection with optimized settings
        print("Setting up scholarly for direct connection...")
        
        # Add some basic configuration if needed
        # scholarly could have rate limiting or other settings
        
        print("Scholarly setup completed")
        return True
        
    except Exception as e:
        print(f"Scholarly setup failed: {e}")
        return False

def fetch_citation_data_with_retry(author_id, max_retries=3):
    """Fetch citation data with retry mechanism and exponential backoff"""
    
    for attempt in range(max_retries):
        try:
            print(f"Fetching data (attempt {attempt + 1}/{max_retries})...")
            print(f"Searching for Google Scholar ID: {author_id}")
            
            # Add random delay before each attempt
            if attempt > 0:
                wait_time = (2 ** attempt) + random.uniform(1, 3)
                print(f"Waiting {wait_time:.1f} seconds before retry...")
                time.sleep(wait_time)
            
            # Search for author
            author = scholarly.search_author_id(author_id)
            
            if not author:
                raise Exception("Author not found")
            
            print("Retrieving author information...")
            
            # Only fetch essential data to minimize requests
            scholarly.fill(author, sections=['basics', 'indices'])
            
            name = author.get('name', 'Unknown')
            citations = author.get('citedby', 0)
            
            print(f"Author: {name}, Citations: {citations}")
            
            # Validate the data
            if citations < 0:
                citations = 0
                
            return author, citations
            
        except Exception as e:
            error_msg = str(e).lower()
            print(f"Attempt {attempt + 1} failed: {e}")
            
            # Check for specific blocking errors
            if any(keyword in error_msg for keyword in [
                'captcha', 'blocked', 'unusual traffic', 'recaptcha', 
                'too many requests', 'rate limit', 'cannot fetch'
            ]):
                print("Google Scholar blocking detected")
                if attempt == max_retries - 1:
                    raise Exception("GOOGLE_SCHOLAR_BLOCKED")
            else:
                print("General error occurred")
                if attempt == max_retries - 1:
                    raise Exception(f"GENERAL_ERROR: {e}")
            
            # Wait longer between retries for blocking errors
            if attempt < max_retries - 1:
                wait_time = min(30, (2 ** attempt) * 5)  # Cap at 30 seconds
                print(f"Waiting {wait_time} seconds before next attempt...")
                time.sleep(wait_time)
    
    raise Exception("All retry attempts failed")

try:
    # Setup scholarly
    setup_scholarly()
    
    # Initial random delay to avoid bot detection
    initial_delay = random.uniform(3, 12)
    print(f"Waiting {initial_delay:.1f} seconds to avoid bot detection...")
    time.sleep(initial_delay)
    
    author_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'EqemKYsAAAAJ')
    
    # Fetch citation data with retry mechanism
    author, citations = fetch_citation_data_with_retry(author_id)
    
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
    print(f"Final citation count: {citations}")
    
except TimeoutError as e:
    print(f"Timeout error: {e}")
    print("The operation took too long. This might be due to Google Scholar blocking.")
    print("The existing citation data will be preserved.")
    sys.exit(1)
    
except Exception as e:
    error_msg = str(e)
    print(f"Error during crawling: {error_msg}")
    
    # Handle different types of errors
    if "GOOGLE_SCHOLAR_BLOCKED" in error_msg:
        print("Google Scholar is currently blocking requests")
        print("This is expected behavior due to anti-bot measures")
        print("The existing citation data will be preserved")
    elif "GENERAL_ERROR" in error_msg:
        print("A general error occurred during crawling")
        print("Please check the logs for more details")
    else:
        print("An unexpected error occurred")
    
    print("Exiting gracefully - existing data will be maintained")
    sys.exit(1)
    
finally:
    # Clear timeout signal
    signal.alarm(0)
    print("Cleanup completed")
