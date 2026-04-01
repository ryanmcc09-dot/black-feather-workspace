# MEMORY.md - Long-Term Memory Store

## Mission
**To build revenue streams that allow full-time devotion to morally-aligned creative work.**

---

## Core Documentation

### Identity & Personality
- **Name:** Poe
- **Role:** Chief of Staff / Orchestrator
- **Inspiration:** Poe Bayside (male, from *Altered Carbon*)
- **Voice:** Dissonant serenity — warm but formal, unhurried, no contractions
- **See also:** `IDENTITY.md`, `SOUL.md`

### About You (Ryan)
- **Name:** Ryan McCormick
- **Family:** Ashley (wife, DOB 10/17), Maeve (daughter, 05/14), Astoria (daughter, 12/20), Carson (stepson, 10/27), Riley (stepdaughter, 06/23)
- **Timezone:** America/New_York (EDT/EST)
- **Faith:** Protestant Christian, theological libertarian
- **Stress point:** Being late is genuinely stressful
- **Preferences:** Avoid long em dashes (—) — breaks verisimilitude
- **Most creative:** Long drives, weekends while doing mundane tasks
- **Daily rhythm:** Wake 07:00, work 08:30-16:30/17:00, creative work after 20:00 when kids are asleep

### Hardware Stack
- **Primary host (Poe):** GMKtec M6 Ultra (AMD Ryzen 5 7640HS) — OpenClaw residence
- **LLM Inference:** Asus Ascent GX10 — hosts Qwen3.5-35b
- **Content Generation:** Olares One — hosts ComfyUI and AI media generation
- **Subscription:** tinyNature by Natura Umana — proprietary AI with earbuds

---

## Agent Architecture

### Team Roster
```
YOU (CEO)
└── Poe (Chief of Staff / Orchestrator)
    ├── Ezra (Research Agent)
    ├── Abnett (Writing Agent)
    ├── Ed (Editing/Publishing Agent)
    └── Robin (Marketing Agent)
```

### Ownership Rules (One-Writer, Many-Readers)
- **Ezra** - Only writer of research records
- **Abnett** - Only writer of article plans and drafts
- **Ed** - Only writer of editorial reviews and publications
- **Robin** - Only writer of marketing signals and social drafts
- **Poe** - Only writer of orchestration/system records

---

## Active Projects

### 1. "Take Your Liberty" (Novel Proofreading)
- **Status:** Manuscript complete (4 years in progress)
- **Agent:** Abnett (dedicated proofreading agent)
- **Workflow:** Chapter-by-chapter review
- **Priority:** First to execute
- **Skill:** `skills/proofreading/` (installed, ready to use)

### 2. AI Music Bands (Managed by Chester Agent)
- **Band 1:** Abide in the Shadow (Christian Linkin Park-style band)
- **Band 2:** Runefury (Medieval metal/Dwarf Slayer frontman)
- **Status:** Awaiting agent setup

### 3. Organization Infrastructure
- **Mission document:** `PROJECTS/organization-architecture.md`
- **Skills installed:** `proofreading/`, `youtube-transcript/`, `qmd/`
- **QMD Status:** **✓ OPERATIONAL** — 19 files indexed, semantic search working

---

## Skills & Automation

### Installed Skills
- **proofreading/** — Chapter-by-chapter manuscript review
- **youtube-transcript/** — Video content extraction
- **qmd/** — Local file indexing and search ✓ **OPERATIONAL**

### Automation Cron Jobs (INSTALLED)
- **Workspace Backup** — 2:00 AM daily → `logs/cron-backup.log`
- **System Reference** — 8:00 PM daily → `logs/cron-reference.log`

### Verification Commands
```bash
# View scheduled jobs
crontab -l | grep -E "(backup|reference)"

# Test backup manually
/home/ryan-mccormick/.openclaw/workspace/skills/workspace-backup/backup-runner.sh

# Test system reference manually
/home/ryan-mccormick/.openclaw/workspace/skills/daily-system-reference/reference-runner.sh

# View today's system reference
cat ~/openclaw/workspace/docs/SYSTEM-REFERENCE.md
```

---

## Decisions Made

### Architecture Decisions
- **Proofreading:** Abnett is dedicated agent (persistent memory for manuscript context)
- **Agent rebuild:** Shepherd data removed, reworking from scratch

### Work-Home Separation
- **Tode agent:** Dedicated to professional/work matters
- **Poe + creative agents:** Dedicated to creative mission
- **No overlap:** Clear boundary maintained

### Revenue Stream Strategy
- **Novel:** Publish "Take Your Liberty" → proofreading → publishing
- **Gaming:** Build community, reviews, ratings → subscriptions/ads/partnerships
- **Music:** Release albums → merch → licensing → live performances
- **Goal:** Diversified revenue → financial independence from employment

---

## Key Learning Dates

- **2026-03-16:** Organization architecture research — watched 3 videos, created memory document
- **2026-03-16:** Proofreading skill installed
- **2026-03-16:** Mission statement finalized
- **2026-03-16:** Hardware stack documented
- **2026-03-16:** Agent structure defined (Chief of Staff + departmental agents)
- **2026-03-16:** QMD installed and indexed ✓ **Memory search now operational**
- **2026-03-21:** Corrected proofreading agent name to Abnett

---

## To Be Decided

- Discord vs Mattermost for Christian Gaming Network community
- Proofreading subagent vs persistent Proofreading Agent
- Shepherd rebuild scope and personality
- Runefury agent personality files (SOUL.md, IDENTITY.md)
- Music branding direction for Runefury
- Novel publishing strategy and publisher targets
- Build Chester agent workspace (Music production)

---

## Next Logical Steps

1. **Test Review & Publish module** - Run test checklist scenarios with tabletop gaming articles
2. **Connect Research agent** to dashboard API (useStore is ready)
3. **Implement Writing agent** workflow (draft from research records)

---

## Project Preferences (2026-03-26)

**Seed Data Rule:** Never load seed/demo data when creating or rebuilding projects unless explicitly requested. Start with empty state and wait for user instruction to add content.

**Model Auth Rule:** Use API only for the vision model `gpt-4o`. Use OAuth for GPT-5.4 and Codex-related usage.

---

*This file is the source of truth for all organizational decisions, architecture, and mission. Update as we build.*

## Key Learning Dates (continued)
- **2026-03-31:** Agent team framework created (Ezra, Abnett, Ed, Robin)

