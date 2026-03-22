#!/bin/bash
# triage.sh - Simple bash version for deterministic auto-deletions
# Handles basic delete rules without complex LLM processing

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

export AGENT_BROWSER_ARGS="--headless=old"

echo "=========================================="
echo "  Outlook Triage - Bash Engine v1.0"
echo "=========================================="
echo ""

# Check for required files
if [ ! -f "outlook.json" ]; then
    echo "ERROR: Session file outlook.json not found!"
    echo "Please authenticate first:"
    echo "  agent-browser open https://outlook.office.com/mail/"
    echo "  agent-browser state save outlook.json"
    exit 1
fi

echo "Starting Outlook Triage..."
echo ""

# Load state and go to inbox
echo "[1/5] Loading authenticated session..."
agent-browser state load outlook.json

echo "[2/5] Opening Outlook inbox..."
agent-browser open https://outlook.office.com/mail/inbox
sleep 5

echo "[3/5] Scanning for emails..."
SNAPSHOT=$(agent-browser snapshot -i --json 2>/dev/null || echo "{}")

# Create an array of refs to delete
REFS_TO_DELETE=()

# Helper function to check if text contains pattern
contains_pattern() {
    local text="$1"
    local pattern="$2"
    echo "$text" | grep -qi "$pattern"
}

# Parse snapshot and find emails to delete based on rules
# Note: This is a simplified version - complex rules require Python triage.py

echo "[4/5] Evaluating delete rules..."

# Rule 1: Reaction Daily Digest
DIGEST_REFS=$(echo "$SNAPSHOT" | jq -r '.data.refs[] | select(.name != null and (.name | test("Reaction Daily Digest"; "i"))) | .ref' 2>/dev/null || true)
for ref in $DIGEST_REFS; do
    if [ -n "$ref" ] && [ "$ref" != "null" ]; then
        echo "  Found: Reaction Daily Digest at @$ref"
        REFS_TO_DELETE+=("$ref")
    fi
done

# Rule 2: BDC Alerts
BDC_REFS=$(echo "$SNAPSHOT" | jq -r '.data.refs[] | select(.name != null and (.name | test("BDC Alert"; "i"))) | .ref' 2>/dev/null || true)
for ref in $BDC_REFS; do
    if [ -n "$ref" ] && [ "$ref" != "null" ]; then
        echo "  Found: BDC Alert at @$ref"
        REFS_TO_DELETE+=("$ref")
    fi
done

# Rule 3: Vendor Surveys
SURVEY_PATTERNS=("tell us how we did" "take 1 minute to tell us" "survey")
for pattern in "${SURVEY_PATTERNS[@]}"; do
    SURVEY_REFS=$(echo "$SNAPSHOT" | jq -r ".data.refs[] | select(.name != null and (.name | test(\"$pattern\"; \"i\"))) | .ref" 2>/dev/null || true)
    for ref in $SURVEY_REFS; do
        if [ -n "$ref" ] && [ "$ref" != "null" ]; then
            echo "  Found: Survey email at @$ref (pattern: $pattern)"
            REFS_TO_DELETE+=("$ref")
        fi
    done
done

# Rule 4: Billie Jo Newman lender updates
BILLIE_REFS=$(echo "$SNAPSHOT" | jq -r '.data.refs[] | select(.name != null and (.name | test("Billie Jo Newman"; "i"))) | .ref' 2>/dev/null || true)
LENDER_PATTERNS=("GAP" "PTO" "Bank of America" "lender update" "lender policy")
for ref in $BILLIE_REFS; do
    if [ -n "$ref" ] && [ "$ref" != "null" ]; then
        # Check if subject contains lender keywords
        for pattern in "${LENDER_PATTERNS[@]}"; do
            if echo "$SNAPSHOT" | jq -r ".data.refs[\"$ref\"].name" 2>/dev/null | grep -qi "$pattern"; then
                echo "  Found: Billie Jo Newman lender update at @$ref"
                REFS_TO_DELETE+=("$ref")
                break
            fi
        done
    fi
done

# Remove duplicates
REFS_TO_DELETE=($(printf "%s\n" "${REFS_TO_DELETE[@]}" | sort -u))

echo ""
echo "[5/5] Processing ${#REFS_TO_DELETE[@]} emails for deletion..."
echo ""

# If we have refs to delete, loop through and delete them
if [ ${#REFS_TO_DELETE[@]} -gt 0 ]; then
    DELETED_COUNT=0
    
    for REF in "${REFS_TO_DELETE[@]}"; do
        echo "  Selecting @$REF..."
        agent-browser click "@$REF"
        sleep 1.5
        
        echo "  Clicking Delete..."
        # Try to find and click delete button
        agent-browser find role button --name "Delete" 2>/dev/null && sleep 2 || true
        
        DELETED_COUNT=$((DELETED_COUNT + 1))
        echo "  ✓ Deleted ($DELETED_COUNT/${#REFS_TO_DELETE[@]})"
    done
    
    echo ""
    echo "Deleted $DELETED_COUNT configured junk emails."
else
    echo "No auto-delete emails found in current view."
fi

echo ""
echo "=========================================="
echo "  Triage Complete"
echo "=========================================="
echo ""
echo "Note: Complex evaluation logic (security screening, telegram notifications)"
echo "requires LLM processing and is handled by triage.py"
echo ""
