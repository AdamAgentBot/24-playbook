import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

load_dotenv('.env')

auth = OAuth1(
    os.getenv('X_API_KEY'),
    os.getenv('X_API_SECRET'),
    os.getenv('X_ACCESS_TOKEN'),
    os.getenv('X_ACCESS_SECRET')
)

print("Attempting handshake with X...")
try:
    response = requests.get('https://api.twitter.com/1.1/account/verify_credentials.json', auth=auth)
    if response.status_code == 200:
        print("✅ SUCCESS: X API CONNECTION VERIFIED.")
        print(f"Account: {response.json().get('screen_name')}")
    else:
        print(f"❌ FAILURE: Status Code {response.status_code}")
        print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ ERROR: {e}")
