#!/bin/bash
# Morning Mission Statement Reminder
# Runs daily at 8:00 AM
# Sends a personalized, unique message each day

MISSION="To build revenue streams that allow full-time devotion to morally-aligned creative work."

# Array of unique morning greetings
GREETINGS=(
  "Rise and shine! 🌅 Time to remember why we're doing this."
  "Good morning! Let's talk about that mission of ours."
  "Morning, Ryan! Here's what we're working toward today."
  "Another day, another chance to build something meaningful."
  "Hey there! Ready for today's mission reminder?"
  "The early bird gets the worm, but the focused one gets the vision."
  "Good morning! Let's make today count."
  "Top of the morning to you! Here's our mission:"
  "Morning! Don't forget what we're building toward."
  "Rise up! Here's our mission to keep us focused:"
)

# Select a random greeting
RANDOM_INDEX=$(($RANDOM % ${#GREETINGS[@]}))
GREETING="${GREETINGS[$RANDOM_INDEX]}"

# Day-of-week themed additions
DAY_OF_WEEK=$(date +%A)
case "$DAY_OF_WEEK" in
  "Monday")    THEMED="Fresh week, fresh momentum. "; EXTRA="🚀" ;;
  "Friday")    THEMED="Almost weekend! Let's push through. "; EXTRA="💪" ;;
  "Saturday")  THEMED="Weekend work mode activated. "; EXTRA="⚡" ;;
  "Sunday")    THEMED="Sunday preparation for the week ahead. "; EXTRA="🙏" ;;
  *)           THEMED=""; EXTRA="✨" ;;
esac

# Build the message
MESSAGE="$GREETING

${THEMED}📋 Mission:
\"$MISSION\"

Let's make it happen today! $EXTRA"

# Send to Telegram
curl -s -X POST "https://api.telegram.org/bot8707884220:AAFwz0ZeTFYwNxa3d88wQ6DIRAmWt60CF6M/sendMessage" \
  -d "chat_id=5960717041" \
  -d "text=$MESSAGE"

echo "$(date): Mission reminder sent - $DAY_OF_WEEK" >> ~/.openclaw/workspace/logs/mission-reminder.log
