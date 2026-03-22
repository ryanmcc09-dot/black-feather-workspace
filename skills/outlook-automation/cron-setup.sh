#!/bin/bash
# cron-setup.sh - Add Outlook Triage to OpenClaw cron scheduler
# Runs automated triage every 4 hours

set -e

echo "=========================================="
echo "  Outlook Triage - Cron Setup"
echo "=========================================="
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if openclaw command is available
if ! command -v openclaw &> /dev/null; then
    echo "WARNING: openclaw command not found."
    echo "This script requires OpenClaw to be installed."
    echo ""
    echo "To set up cron manually, add this to your crontab:"
    echo ""
    echo "  # Run Outlook Triage every 4 hours"
    echo "  0 */4 * * * cd $SCRIPT_DIR && python3 triage.py >> cron.log 2>&1"
    echo ""
    echo "To edit crontab, run: crontab -e"
    exit 1
fi

echo "Adding outlook-triage to OpenClaw cron..."
echo "Schedule: Every 4 hours"
echo ""

# Create cron job using OpenClaw
openclaw cron add \
    --id outlook-triage \
    --schedule '{ "kind": "every", "everyMs": 14400000 }' \
    --payload '{ "kind": "systemEvent", "text": "Execute Outlook Triage via agent-browser rules." }' \
    --session-target main \
    --name "Outlook Email Triage"

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "  ✓ Cron job created successfully!"
    echo "=========================================="
    echo ""
    echo "The triage will run automatically every 4 hours."
    echo ""
    echo "To manage this cron job:"
    echo "  - List all jobs: openclaw cron list"
    echo "  - Run now:       openclaw cron run outlook-triage"
    echo "  - Pause:         openclaw cron pause outlook-triage"
    echo "  - Resume:        openclaw cron resume outlook-triage"
    echo "  - Remove:        openclaw cron remove outlook-triage"
    echo ""
else
    echo ""
    echo "ERROR: Failed to create cron job."
    echo "Please check OpenClaw installation and try again."
    exit 1
fi
