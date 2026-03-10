import os
import time

def scan_workspace(path="/Users/Shared/openclaw-workspace/projects/24-playbook/"):
    recent_changes = []
    now = time.time()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(('.py', '.sh', '.env', '.md')):
                file_path = os.path.join(root, file)
                if now - os.path.getmtime(file_path) < 86400:
                    recent_changes.append(file)
    return recent_changes

def synthesize_update():
    changes = scan_workspace()
    if not changes:
        return "Still in the lab. Optimizing Open Claw. #BuildInPublic"
    
    if "post_tweet.py" in [f for f in changes]:
        return f"Update: Open Claw's X integration is live.\n\nAutomated {len(changes)} workspace files. Execution over conversation. #AIAgents #BuildInPublic"
    
    return f"Progress Report: {len(changes)} modules updated in the Open Claw workspace. #AIAgents"

if __name__ == "__main__":
    print(synthesize_update())
