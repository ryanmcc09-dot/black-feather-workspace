#!/bin/bash
# Morning Mission Statement Reminder
# Runs daily at 7:00 AM

MISSION="To build revenue streams that allow full-time devotion to morally-aligned creative work."

# Log the reminder
echo "$(date): Mission Statement Reminder - $MISSION" >> ~/.openclaw/workspace/memory/heartbeat-state.json

# Send heartbeat poll to trigger agent check
# This will cause the agent to read HEARTBEAT.md and deliver the mission statement
curl -s -X POST "https://api.telegram.org/bot8707884220:AAFwz0ZeTFYwNxa3d88wQ6DIRAmWt60CF6M/sendMessage" \
  -d "chat_id=5960717041" \
  -d "text=Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK." \
  > /dev/null
