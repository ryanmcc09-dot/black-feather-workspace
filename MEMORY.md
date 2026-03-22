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

### Executive Structure
```
YOU (CEO)
└── Poe (Chief of Staff / COO)
    ├── Shepherd (Gaming Network - CMO role)
    │   └── Subagents: Content, Community, Moderation
    ├── Chester (Music - Creative Director)
    │   ├── Christian Linkin Park-style band
    │   └── Runefury (Medieval metal/Dwarf Slayer)
    │       └── Subagents: Audio, Visual, Marketing
    └── Abnett (Novel Proofreading - "Take Your Liberty")
```

### Key Insights from Research

#### Video 1: "OpenClaw Agents vs Sub-Agents"
- **Agents** = persistent workspaces with independent memory, personality, and channels
- **Subagents** = temporary task workers, no persistent memory, auto-archive after task
- **Max spawn depth:** 5 levels, configurable `maxSpawnDepth: 2` for orchestration hierarchies
- **Subagents only receive:** `AGENTS.md` + `TOOLS.md` (no personality files)

#### Video 2: "Build a Multi-Agent Team with OpenClaw"
- **Muddy model:** Executive assistant who always delegates, never cues prompts
- **Departmental agents:** CTO, CMO, CRO with specialized roles
- **Autonomous standups:** Daily meetings between department heads, generate action items
- **Ping CEO only when review needed**

#### Video 3: "I Have 25 AI Agents Working 24/7"
- **Clear Mud's architecture:** CEO → Muddy (COO) → Department heads (Elton/Gary/Warren)
- **Model pairings:** Opus 4.6 + Sonnet 4.5 for content workflows
- **Gateway strategy:** Department heads share one gateway; community bot gets separate gateway
- **Real-time documentation:** Updates as agents operate

### Communication Protocol
- **"Do it now"** — bypasses agent infrastructure, executes immediately under Poe's direct control
- **Delegated task** — fire and forget, report back when done
- **Executive sync meetings** — autonomous standups between agents, summary generated
- **Agent-to-agent communication** — uses `sessions_send` tool

---

## Active Projects

### 1. "Take Your Liberty" (Novel Proofreading)
- **Status:** Manuscript complete (4 years in progress)
- **Agent:** Abnett (dedicated proofreading agent)
- **Workflow:** Chapter-by-chapter review
- **Priority:** First to execute
- **Skill:** `skills/proofreading/` (installed, ready to use)
- **Constraint:** Voice changed between beginning and end chapters — needs style consistency check

### 2. Christian Gaming Network (Shepherd Agent) — FULLY CONFIGURED
- **Purpose:** Reviews, articles, parental resources, content ratings for Christian gaming
- **Agent Name:** Shepherd (Chief Marketing Officer + AI Team Lead)
- **Status:** **✓ WORKSPACE COMPLETE** (2026-03-16)
- **Capabilities:**
  - Lead team of AI sub-agents (reviewer, researcher, editor, publisher, marketing, community)
  - Spawn ephemeral sub-agents for specific tasks
  - Review and approve all content before publishing
  - Manage Discord community (awaiting bot setup)
  - Create faith-aligned game reviews
- **Workspace:** `~/.openclaw/workspace-shepherd/`
- **Configuration:** Added to openclaw.json, launch-ready via `openclaw agent run shepherd`
- **To Launch:** Discord bot token required (see PROJECTS/discord-setup.md)
- **Documentation:**
  - SOUL.md — Expanded with sub-agent leadership framework
  - AGENTS.md — Detailed operational protocols
  - USER.md — Ryan as CEO context
  - TOOLS.md — Review templates, rating system, workflow examples
  - MEMORY.md — Sub-agent framework and decisions
  - PROJECTS/sub-agent-protocol.md — Complete sub-agent lifecycle documentation

### 3. AI Music Bands (Managed by Chester Agent)
- **Band 1:** Abide in the Shadow (Christian Linkin Park-style band)
- **Band 2:** Runefury (Medieval metal/Dwarf Slayer frontman)
- **Genre:** Medieval metal — blend of metal-core/nu-metal and medieval music
- **Branding:** Needs visual identity, audio generation (Olares One), marketing
- **Status:** Awaiting agent setup
- **Agent:** Chester (Creative Director, memorial tribute to Chester Bennington)

### 4. Organization Infrastructure
- **Mission document:** `PROJECTS/organization-architecture.md`
- **Skills installed:** `proofreading/`, `youtube-transcript/`, `qmd/`
- **QMD Status:** **✓ OPERATIONAL** — 19 files indexed, semantic search working

---

## Decisions Made

### Architecture Decisions
- **Proofreading:** Abnett is dedicated agent (persistent memory for manuscript context)
- **Shepherd:** Full independent agent (needs autonomy, memory, community channel)
- **Chester:** Full independent agent (needs specialized creative workflows for both bands)
- **Gateway:** Poe, Shepherd, Chester share one gateway (collocated); Tode separate (work); tinyNature separate (subscription)

### Work-Home Separation
- **Tode agent:** Dedicated to professional/work matters
- **Poe + Shepherd + Runefury:** Dedicated to creative mission
- **No overlap:** Clear boundary maintained

### Revenue Stream Strategy
- **Novel:** Publish "Take Your Liberty" → proofreading → publishing
- **Gaming:** Build community, reviews, ratings → subscriptions/ads/partnerships
- **Music:** Release albums → merch → licensing → live performances
- **Goal:** Diversified revenue → financial independence from employment

---

## Skills & Tools

### Installed
- **proofreading/** — Chapter-by-chapter manuscript review
- **youtube-transcript/** — Video content extraction (requires WireGuard VPN or manual yt-dlp)
- **qmd/** — Local file indexing and search ✓ **OPERATIONAL**
  - 19 files indexed
  - Vector embeddings created
  - Semantic search working
  - Example: `qmd search "mission revenue streams"` returns 5 relevant results

### CLI Tools
- **clawhub** — Skill repository CLI
- **qmd** — Search workspace docs: `qmd search "query"`

### Configuration
- **maxSpawnDepth:** 1 (default), can be increased to 2 for orchestration
- **Subagent limit:** 5 active subagents per agent, configurable 1-20
- **Total concurrency:** 8 subagents running simultaneously, configurable

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
- Shepherd and Runefury agent personality files (SOUL.md, IDENTITY.md)
- Music branding direction for Runefury
- Novel publishing strategy and publisher targets

---

## New Project: Multi-Agent Dashboard OS (2026-03-21)

**Status:** Master Plan Complete | **Next Phase:** Foundation

**Architecture:**
- Single Next.js dashboard + Convex backend
- 3 OpenClaw Gateways on GMKtek (Music, Blog/Gaming, Poe oversight)
- Convex for structured data (real-time sync, queries, auth)
- GMKtek local storage for large files (audio, video, markdown)

**Key Features:**
- Agent communication hub with chat logs
- Meeting scheduler with transcripts
- Project tracking with visible docs and chatter
- Shepherd Newsroom (research → writing → editing → publishing)
- Chester Studio (lyrics, songs, audio files)
- Marketing Agency workspaces (separate for each business)
- Duplicate prevention (query by gameName + topic before writing)

**Convex Token:** `eyJ2MiI6ImFiNDk0MjhlMDE5YTQ2NjliOWY5MDVhMThkYWQ2Nzk5In0=`

**Documentation:** `PROJECTS/multi-agent-dashboard.md`

**Next Steps:**
1. Initialize Convex project
2. Deploy 3 OpenClaw Gateways on GMKtek
3. Create Convex schema files for 7 collections
4. Build Next.js dashboard frontend

---

*This file is the source of truth for all organizational decisions, architecture, and mission. Update as we build.*
