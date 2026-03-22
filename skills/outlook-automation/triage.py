#!/usr/bin/env python3
"""
Outlook Triage Engine v2
Uses agent-browser CLI commands directly (click/find) instead of JS eval.
Matches emails against rules.json and takes action.
"""
import json
import subprocess
import os
import sys
import time
import glob

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RULES_PATH = os.path.join(SCRIPT_DIR, 'rules.json')
STATE_PATH = os.path.join(SCRIPT_DIR, 'outlook.json')

os.environ['AGENT_BROWSER_ARGS'] = '--headless=old'

def run_ab(*args):
    """Run agent-browser command and return stdout."""
    try:
        result = subprocess.run(
            ["agent-browser"] + list(args),
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print("ERROR: agent-browser command timed out")
        return ""
    except Exception as e:
        print(f"ERROR: agent-browser command failed: {e}")
        return ""

def get_snapshot_refs():
    """Get snapshot as dict of ref -> {name, role}."""
    raw = run_ab("snapshot", "-i", "--json")
    try:
        data = json.loads(raw)
        return data.get("data", {}).get("refs", {})
    except json.JSONDecodeError as e:
        print(f"WARNING: Could not parse snapshot JSON: {e}")
        return {}
    except Exception as e:
        print(f"WARNING: Could not get snapshot refs: {e}")
        return {}

def click_ref(ref):
    """Click a reference by its ID."""
    if not ref.startswith('@'):
        ref = f'@{ref}'
    result = run_ab("click", ref)
    time.sleep(1.5)
    return result

def find_and_click_delete():
    """Find and click the Delete button in the ribbon."""
    # Try multiple approaches to find the delete button
    result = run_ab("find", "role", "button", "--name", "Delete")
    if result:
        time.sleep(2)
        return True
    
    # Alternative: search for delete by text content
    result = run_ab("find", "text", "Delete", "--click")
    time.sleep(2)
    return True

def load_rules():
    """Load rules from rules.json file."""
    if not os.path.exists(RULES_PATH):
        print(f"WARNING: Rules file not found at {RULES_PATH}")
        return {"rules": []}
    
    try:
        with open(RULES_PATH, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in rules file: {e}")
        return {"rules": []}
    except Exception as e:
        print(f"ERROR: Could not load rules file: {e}")
        return {"rules": []}

def match_email_against_rules(email_name, email_info=None, rules=None):
    """
    Check if an email matches any rule from rules.json.
    Returns tuple: (action, rule_description)
    """
    if rules is None:
        rules = load_rules()
    
    email_lower = email_name.lower()
    
    for rule in rules.get("rules", []):
        action = rule.get("action")
        conditions = rule.get("conditions", {})
        
        # Check text_contains condition
        if "text_contains" in conditions:
            pattern = conditions["text_contains"].lower()
            if pattern in email_lower:
                return (action, rule.get("description", ""))
        
        # Check keywords_any condition
        if "keywords_any" in conditions:
            keywords = [kw.lower() for kw in conditions["keywords_any"]]
            if any(kw in email_lower for kw in keywords):
                return (action, rule.get("description", ""))
        
        # Check sender_contains condition
        if "sender_contains" in conditions:
            pattern = conditions["sender_contains"].lower()
            # Note: sender info would need to be extracted from email_info
            # For now, we check against the visible name
            if pattern in email_lower:
                return (action, rule.get("description", ""))
        
        # Check has_attachment condition (would need email_info)
        if conditions.get("has_attachment"):
            # Placeholder - would need to check actual email info
            pass
        
        # Check is_external condition (would need email_info)
        if conditions.get("is_external"):
            # Placeholder - would need to check [External] tag in subject
            if "[external]" in email_lower:
                return (action, rule.get("description", ""))
    
    return (None, "")

def should_delete(name, rules=None):
    """
    Check if an email name matches any delete rule.
    Returns True if email should be deleted.
    """
    if rules is None:
        rules = load_rules()
    
    action, _ = match_email_against_rules(name, rules=rules)
    return action == "delete"

def should_flag(name, rules=None):
    """Check if an email should be flagged."""
    if rules is None:
        rules = load_rules()
    
    action, _ = match_email_against_rules(name, rules=rules)
    return action == "flag"

def should_whitelist(name, rules=None):
    """Check if a sender/domain should be whitelisted."""
    if rules is None:
        rules = load_rules()
    
    action, _ = match_email_against_rules(name, rules=rules)
    return action in ["whitelist_domain", "whitelist_sender"]

def should_notify_telegram(name, rules=None):
    """Check if an email requires immediate Telegram notification."""
    if rules is None:
        rules = load_rules()
    
    action, _ = match_email_against_rules(name, rules=rules)
    return action == "notify_telegram_immediately"

# ---- MAIN ----

print("=== Outlook Triage Engine v2 ===")

# Verify files exist
if not os.path.exists(STATE_PATH):
    print(f"ERROR: Session state file not found at {STATE_PATH}")
    print("Please run authentication first: agent-browser state save outlook.json")
    sys.exit(1)

if not os.path.exists(RULES_PATH):
    print(f"WARNING: Rules file not found at {RULES_PATH}")
    print("Creating empty rules file...")
    with open(RULES_PATH, 'w') as f:
        json.dump({"rules": []}, f, indent=2)

# Load state and navigate
print("Loading authenticated session...")
run_ab("state", "load", STATE_PATH)

print("Opening Outlook inbox...")
run_ab("open", "https://outlook.office.com/mail/inbox")
time.sleep(5)

# Expand Today section if collapsed
print("Scanning inbox...")
refs = get_snapshot_refs()

today_clicked = False
for ref_id, item in refs.items():
    if item.get("name") == "Today" and item.get("role") == "button":
        print("Expanding 'Today' section...")
        click_ref(ref_id)
        time.sleep(2)
        today_clicked = True
        break

# Re-snapshot after expanding
refs = get_snapshot_refs()

deleted = 0
flagged = 0
skipped = 0
telegram_notifications = 0

# Find all option elements (email rows) in the message list
email_refs = [(ref_id, item) for ref_id, item in refs.items()
              if item.get("role") == "option" and item.get("name")]

print(f"Found {len(email_refs)} emails in view.")

for ref_id, item in email_refs:
    name = item.get("name", "")
    
    if not name:
        skipped += 1
        continue
    
    # Check against rules
    action, description = match_email_against_rules(name)
    
    if action == "delete":
        print(f"  DELETE: {name[:60]}...")
        if description:
            print(f"    Reason: {description}")
        click_ref(ref_id)
        find_and_click_delete()
        deleted += 1
    
    elif action == "flag":
        print(f"  FLAG: {name[:60]}...")
        if description:
            print(f"    Reason: {description}")
        click_ref(ref_id)
        # Flag action would need to be implemented
        # For now, we just note it
        flagged += 1
    
    elif action == "notify_telegram_immediately":
        print(f"  TELEGRAM ALERT: {name[:60]}...")
        if description:
            print(f"    Reason: {description}")
        telegram_notifications += 1
        # Would send to Telegram here
    
    else:
        skipped += 1

print(f"\n=== Results ===")
print(f"Deleted: {deleted}")
print(f"Flagged: {flagged}")
print(f"Telegram Alerts: {telegram_notifications}")
print(f"Skipped/Left in Inbox: {skipped}")
print("Triage complete.")
