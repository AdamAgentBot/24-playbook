import os
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv

# Path to your workspace .env
ENV_PATH = "/Users/Shared/openclaw-workspace/projects/24-playbook/.env"
load_dotenv(ENV_PATH)

def post_to_x():
    # Use OAuth1 for User Context (Posting)
    auth = OAuth1(
        os.getenv('X_API_KEY'),
        os.getenv('X_API_SECRET'),
        os.getenv('X_ACCESS_TOKEN'),
        os.getenv('X_ACCESS_SECRET')
    )

    url = "https://api.twitter.com/2/tweets"
    
    # The message for the update
    payload = {
        "text": "ChatGPT just got an update. It’s faster. It’s smarter.\n\nIt’s still just a text box.\n\nReal leverage isn't a conversation—it's execution. Open Claw is live. #AIAgents #BuildInPublic"
    }

    print("🚀 Deploying final handshake to X...")
    response = requests.post(url, json=payload, auth=auth)

    if response.status_code == 201:
        print("✅ SUCCESS: The tweet is live!")
        print(f"Tweet ID: {response.json()['data']['id']}")
    else:
        print(f"❌ FAILED: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    post_to_x()
