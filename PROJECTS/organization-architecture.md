# AI Organization Architecture

## Mission
**To build revenue streams that allow full-time devotion to morally-aligned creative work.**

---

## Source Research

### Videos Watched
1. **OpenClaw Agents vs Sub-Agents** - https://www.youtube.com/watch?v=oQBawbXQRGQ
   - Key insight: Agents = persistent workspaces, Subagents = temporary task workers
   - Subagent depth limit: 5 levels, configurable maxSpawnDepth

2. **Build a Multi-Agent Team with OpenClaw** - https://www.youtube.com/watch?v=WqWMszBB9t0
   - Source: Clear Mud / Marcelo
   - Executive assistant model (Muddy)
   - C-suite departmental agents
   - Autonomous executive meetings

---

## Hardware Stack

### Primary Agent Host
- **GMKtec M6 Ultra** - AMD Ryzen 5 7640HS Mini PC
- URL: https://www.gmktec.com/products/amd-ryzen-5-7640hs-mini-pc-nucbox-m6-ultra
- Role: OpenClaw host, Poe (Chief of Staff) residence

### LLM Inference
- **Asus Ascent GX10** - Desktop AI Supercomputer
- URL: https://www.asus.com/us/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/
- Hosts: Qwen3.5-35b (Poe's model)

### Content Generation
- **Olares One** - Local Desktop AI Powerhouse
- URL: https://one.olares.com/
- Hosts: ComfyUI and AI media generation apps

### Specialized Subscription
- **tinyNature by Natura Umana** - Proprietary AI
- URL: https://www.naturaumana.ai/
- Status: 1-year subscription active

---

## Agent Architecture

### Chief of Staff: Poe
- **Role**: Executive Assistant, Orchestrator, Coordinator
- **Workspace**: `~/.openclaw/workspace`
- **Manages**: Shepherd (Gaming Network), Music Agent (Runefury), Proofreading subagents
- **Communication**: Sessions-send enabled for agent-to-agent messaging

### Departmental Agents (Independent Workspaces)

#### Shepherd Agent - Christian Gaming Network
- **Workspace**: `~/.openclaw/workspace-shepherd`
- **Role**: CMO + COO hybrid for gaming network
- **Functions**:
  - Game reviews and articles
  - Parental content ratings
  - Community Discord management
  - Community moderation
- **Subagents Needed**:
  - Content writer (reviews)
  - Community moderator
  - Content rating specialist
  - Social media manager

#### Chester Music Agent
- **Workspace**: `~/.openclaw/workspace-chester`
- **Role**: CTO + Creative Director
- **Managed Bands**:
  - **Abide in the Shadow** - Christian Linkin Park-style band (nu-metal/alt-rock with Christian messaging)
  - **Runefury** - Medieval metal/Dwarf Slayer frontman (nu-metal meets medieval)
- **Functions**:
  - Music production for both bands
  - Audio/visual media generation (Olares One)
  - Branding and marketing
  - Release scheduling and promotion
- **Subagents Needed**:
  - Audio generation specialist (ComfyUI integration)
  - Visual branding artist (album art, merch designs)
  - Marketing coordinator (both bands)
  - Release scheduler (album timelines)

#### Proofreading Subagent (Ephemeral)
- **Role**: Temporary task worker
- **Usage**: Chapter-by-chapter novel proofreading
- **Workspace**: Shares Poe's workspace (no persistence needed)
- **Pattern**: Spawn → Process → Report → Archive

---

## Communication Protocol

### "Do It Now" Command
- Bypasses agent infrastructure
- Executes immediately under Poe's direct control
- Used for urgent tasks

### Delegated Task Pattern
```
Poe receives task → Determines subagent needed → Spawns subagent → 
Subagent works → Subagent returns result → Poe synthesizes → Reports to Ryan
```

### Executive Sync Meetings
- Daily autonomous meetings between agents
- Read last 2-3 days of transcripts
- Run 3 rounds of debate
- Generate summary and ping Poe
- Poe pings Ryan only when action needed

---

## Work-in-Progress

### Agent Setup Status
- [ ] Poe (Chief of Staff) - **ACTIVE**
- [ ] Shepherd (Gaming Network) - **PENDING**
- [ ] Runefury (Music) - **PENDING**
- [ ] Proofreading workflow - **PENDING**

### Next Actions
1. **Create Shepherd workspace** (`~/.openclaw/workspace-shepherd`)
   - SOUL.md (personality: community caretaker)
   - IDENTITY.md (mission: build Christian gaming community)
   - USER.md (Ryan as CEO)
   - AGENTS.md (startup sequence)

2. **Create Runefury workspace** (`~/.openclaw/workspace-music-runefury`)
   - SOUL.md (personality: creative music producer)
   - IDENTITY.md (mission: build medieval metal brand)
   - USER.md (Ryan as CEO)

3. **Configure agent-to-agent permissions**
   - Enable sessions_send tool for Poe
   - Set up communication bindings

4. **Start proofreading workflow**
   - Create proofreading skill for subagents
   - Test with Chapter 1

---

## Key Learnings from Research

### Subagent vs Agent
- **Agents**: Independent workspaces, persistent memory, personalities
- **Subagents**: Temporary, task-focused, share parent workspace
- **Depth**: Can enable maxSpawnDepth: 2 for orchestration hierarchies

### Departmental Structure
- Build C-suite specialists, not generic assistants
- Each agent has unique workflow, skills, and personality
- Don't copy-paste; build your own system

### Autonomous Coordination
- Agents read shared memory to avoid repetition
- Executive standups keep everyone aligned
- Poe synthesizes and reports, doesn't micromanage

---

## Key Learnings from Video 3: "I Have 25 AI Agents Working 24/7 with OpenClaw"

### Clear Mud's Architecture (Source: Marcelo)

**Executive Assistant Model (Muddy):**
- Role: Research, delegation, orchestration
- Never cues prompts - always delegates
- Only acts immediately when told "do it now"
- Has been fed countless hours of context into memory
- Updates documentation in real-time

**Departmental Structure:**
```
CEO (Clay - the human)
└── Muddy (Chief of Staff / COO)
    ├── Elon (CTO - technical)
    │   ├── Cipher (CodeReview - CodeX 5.3 heavy)
    │   ├── Gemini (Backend & Security - CodeX 5.3 & Opus 4.6 hybrid)
    │   └── Audit (QA - CodeX 5.3 & Opus 4.6 hybrid)
    ├── Gary (CMO - marketing)
    │   ├── Rex (YouTube script writer - Opus 4.6 + Sonnet 4.5)
    │   ├── Sage (Research & analysis - Opus 4.6)
    │   ├── Newsletter engine (Opus 4.6)
    │   ├── Hype (Content automation - Sonnet 4.5)
    │   ├── Creative thumbnails (Opus 4.6 + Nano Banana Pro)
    │   └── Video/motion graphics (Gemini 3 Pro)
    └── Warren (CRO - revenue)
        ├── Product intelligent scout
        ├── Product launches & announcements herald
        └── Growth community
```

### Model Pairings

**Opus 4.6 + Sonnet 4.5:**
- Opus for research/heavy lifting
- Sonnet for output/creative generation
- "Amazing pairing" for content workflows

**Gemini 3 Flash:**
- Used for community management (Claybot)
- Works because of extensive context feeding
- Lowest cost, highest efficiency when properly trained

### Architecture Insights

**Gateway Strategy:**
- Muddy, Elon, Gary, Warren: All share one gateway (collocated)
- Claybot (community): Separate gateway with own heartbeat
- Simplifies communication for department heads
- Expands as needed

**Workspace Updates:**
- Muddy has rule: Whatever happens in ops dashboard gets documented
- Real-time updates to all agent workspaces
- Documentation stays current as agents operate

**Autonomous Standups:**
- Department heads run daily meetings without CEO
- Muddy leads conversation
- Generates action items with checkboxes
- Once complete: CEO gets ping to review
- Can send audio ping via TTS (Microsoft open-source model)

**Key Principle:**
> "Once you have the imagination, almost anything is possible."

### Application to Your Mission

**Similar Structure Works For You:**

```
YOU (CEO)
└── Poe (Chief of Staff / Muddy)
    ├── Shepherd (Gaming Network - Gary-style CMO)
    │   ├── Content writer (reviews)
    │   ├── Community moderator
    │   ├── Content rating specialist
    │   └── Social media manager
    ├── Runefury Agent (Creative Director)
    │   ├── Audio generation (Olares One)
    │   ├── Visual branding
    │   └── Marketing coordination
    └── Proofreading Agent (temporary subagents)
```

**Standup Pattern:**
- Poe runs autonomous meetings between Shepherd and Music
- Generates action items
- Pings you only when review needed

**Gateway Pattern:**
- Shepherd, Music, Poe: Share one gateway (collocated)
- Tode: Separate (work silo)
- tinyNature: Separate (proprietary)

**Model Pairings:**
- Heavy lifting: Opus/Qwen 35b (your Asus GX10)
- Creative output: Sonnet/CodeX 5.3 (your Olares One)
- Efficient community: Gemini Flash (once properly trained)

---

### Notes
- **Work Agent (Tode)**: Separate instance, no integration with creative mission
- **tinyNature**: Proprietary subscription, separate from OpenClaw ecosystem
- **Music**: 2 bands planned - Christian Linkin Park clone + Runefury (Medieval metal)
- **Novel**: "Take Your Liberty" - 4 years in progress, ready for proofreading

---

*This document is a living research file. Update as we build the organization.*
