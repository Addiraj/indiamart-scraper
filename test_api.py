#!/usr/bin/env python3
"""
Test script for IndiaMart Scraper API
"""

import requests
import json
import time

def test_local_api():
    """Test the API running locally"""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing IndiaMart Scraper API locally...")
    
    # Test health endpoint
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"    Health check failed: {e}")
        return
    
    # Test root endpoint
    print("\n2. Testing root endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"    Root endpoint failed: {e}")
        return
    
    # Test search endpoint
    print("\n3. Testing search endpoint...")
    search_data = {
        "query": "jewellery",
        "city": "Mumbai",
        "pages": 1
    }
    
    try:
        print(f"   Searching for: {search_data}")
        start_time = time.time()
        
        response = requests.post(
            f"{base_url}/search",
            json=search_data,
            headers={"Content-Type": "application/json"}
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"   Status: {response.status_code}")
        print(f"   Duration: {duration:.2f} seconds")
        
        if response.status_code == 200:
            result = response.json()
            print(f"   Success: {result['success']}")
            print(f"   Total Results: {result['total_results']}")
            print(f"   Message: {result['message']}")
            
            if result['data']:
                print(f"\n   Sample Results:")
                for i, business in enumerate(result['data'][:3]):
                    print(f"{i+1}. {business['name']}")
                    print(f"Phone: {business['phone_number']}")
                    print(f"URL: {business['title_url'][:50]}...")
                    print()
            
            print(" API test completed successfully!")
            
        else:
            print(f"Search failed: {response.text}")
            
    except Exception as e:
        print(f"Search test failed: {e}")

def test_railway_api(railway_url):
    """Test the API deployed on Railway"""
    print(f"Testing IndiaMart Scraper API on Railway: {railway_url}")
    
    # Test health endpoint
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{railway_url}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
        return
    
    # Test search endpoint
    print("\n2. Testing search endpoint...")
    search_data = {
        "query": "restaurants",
        "city": "Delhi",
        "pages": 1
    }
    
    try:
        print(f"   Searching for: {search_data}")
        start_time = time.time()
        
        response = requests.post(
            f"{railway_url}/search",
            json=search_data,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"Status: {response.status_code}")
        print(f"Duration: {duration:.2f} seconds")
        
        if response.status_code == 200:
            result = response.json()
            print(f"   Success: {result['success']}")
            print(f"   Total Results: {result['total_results']}")
            print(f"   Message: {result['message']}")
            
            if result['data']:
                print(f"\nSample Results:")
                for i, business in enumerate(result['data'][:3]):
                    print(f"{i+1}. {business['name']}")
                    print(f"Phone: {business['phone_number']}")
                    print()
            
            print("Railway API test completed successfully!")
            
        else:
            print(f"Search failed: {response.text}")
            
    except Exception as e:
        print(f"Railway test failed: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Test Railway deployment
        railway_url = sys.argv[1]
        test_railway_api(railway_url)
    else:
        # Test local deployment
        test_local_api()
        
        print("\n" + "="*50)
        print("To test Railway deployment, run:")
        print("python test_api.py https://your-app.railway.app")
