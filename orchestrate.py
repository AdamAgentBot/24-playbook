import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import brain

# 1. Load the "Handshake" (Auth)
ENV_PATH = "/Users/Shared/openclaw-workspace/projects/24-playbook/.env"
load_dotenv(ENV_PATH)

def run_autonomous_post():
    # 2. Ask the "Brain" what we did today
    print("🧠 Open Claw Brain is scanning the workspace...")
    message = brain.synthesize_update()
    
    print(f"\n📝 Proposed Post:\n\"{message}\"\n")
    
    # 3. Setup the Auth
    auth = OAuth1(
        os.getenv('X_API_KEY'),
        os.getenv('X_API_SECRET'),
        os.getenv('X_ACCESS_TOKEN'),
        os.getenv('X_ACCESS_SECRET')
    )

    # 4. The Final Execution
    confirm = input("🚀 Deploy to X? (y/n): ")
    if confirm.lower() == 'y':
        url = "https://api.twitter.com/2/tweets"
        payload = {"text": message}
        response = requests.post(url, json=payload, auth=auth)
        
        if response.status_code == 201:
            print(f"✅ SUCCESS: Post is live! ID: {response.json()['data']['id']}")
        else:
            print(f"❌ FAILED: {response.status_code}")
            print(response.json())
    else:
        print("🛑 Orchestration paused.")

if __name__ == "__main__":
    run_autonomous_post()
