import sys

def count_pages(pdf_path):
    with open(pdf_path, 'rb') as f:
        content = f.read()
    
    # Check for /Count in /Pages object
    import re
    match = re.search(rb'/Count\s+(\d+)', content)
    if match:
        return int(match.group(1))
    return 0

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '/Users/ozagent/.openclaw/workspace/projects/24-playbook/blueprint.pdf'
    print(count_pages(path))
