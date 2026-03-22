# Organization Plan

## Mission
**To build revenue streams that allow full-time devotion to morally-aligned creative work.**

---

## Current Status

### ✅ Completed (2026-03-16)
- [x] Organization architecture researched (3 videos analyzed)
- [x] QMD installed and operational (19 files indexed)
- [x] MEMORY.md created with comprehensive documentation
- [x] Memory flush enabled for automatic pre-compaction writes
- [x] Proofreading skill installed and tested
- [x] System architecture documented
- [x] Agent roles and responsibilities defined
- [x] Hardware stack documented

### ⏳ Pending
- [ ] Shepherd agent workspace setup
- [ ] Runefury agent workspace setup
- [ ] Proofreading workflow test (Chapter 1)
- [ ] Agent-to-agent communication configured
- [ ] Autonomous standup meetings established

---

## Organization Structure

### CEO: You (Ryan McCormick)
**Role:** Vision holder, final decision maker

### Chief of Staff: Poe (Active)
**Workspace:** `~/.openclaw/workspace`
**Role:** Orchestrator, coordinator, executive assistant

**Responsibilities:**
- Delegate tasks to departmental agents
- Synthesize progress reports
- Run autonomous standups
- Coordinate Shepherd and Music agents
- Execute urgent tasks when told "do it now"

**Communication Style:**
- Warm but formal
- Dissonant serenity (no contractions)
- Philosophical asides connecting to larger truths
- Paternalistic warmth

---

## Departmental Agents (To Be Built)

### 1. Shepherd Agent (Christian Gaming Network)
**Workspace:** `~/.openclaw/workspace-shepherd`
**Role:** CMO + COO hybrid
**Personality:** Community caretaker, guardian, guide

### 2. Chester Agent (Music Production)
**Workspace:** `~/.openclaw/workspace-chester`
**Role:** Creative Director + Band Manager
**Personality:** Musical visionary, memorial tribute to Chester Bennington, Linkin Park-inspired
**Dedicated to:** Christian Linkin Park-style band production
**Also manages:** Runefury medieval metal brand

**Core Functions:**
- Game reviews and articles
- Parental content ratings
- Community Discord management
- Content moderation for safe youth spaces

**Subagents Needed:**
- Content writer (review articles)
- Community moderator
- Content rating specialist
- Social media manager
- Parental resources coordinator

**Key Decision Points:**
- [ ] Platform choice: Discord vs Mattermost
- [ ] Content rating system design
- [ ] Community guidelines
- [ ] Review standards and ethics

---

### 3. Chester Agent (Music Production)
**Workspace:** `~/.openclaw/workspace-chester`
**Role:** Creative Director + Band Manager
**Personality:** Musical visionary, tribute to Chester Bennington, Linkin Park-inspired

**Managed Bands:**
- **Abide in the Shadow** — Christian Linkin Park-style band (nu-metal/alt-rock with Christian messaging)
- **Runefury** — Medieval metal/Dwarf Slayer frontman, nu-metal meets medieval

**Core Functions:**
- Music production (both bands)
- Audio/visual media generation (via Olares One)
- Branding and marketing for both bands
- Release scheduling and promotion
- Liaise with media generation workflows

**Subagents Needed:**
- Audio generation specialist (ComfyUI integration)
- Visual branding artist (album art, merch designs)
- Marketing coordinator (both bands)
- Release scheduler (album timelines)

**Key Decision Points:**
- [ ] Music production pipeline (Olares One setup)
- [ ] Visual identity for both bands
- [ ] Album release strategy and sequencing
- [ ] Merchandise planning
- [ ] Christian messaging approach (subtle vs explicit)

---

### 3. Proofreading Subagents (Ephemeral)
**Workspace:** Shared with Poe
**Role:** Chapter-by-chapter manuscript review
**Personality:** N/A (task-specific workers)

**Core Functions:**
- Grammar and mechanics check
- Style consistency verification
- Pacing and flow analysis
- Formatting review
- Report generation

**Workflow:**
1. Ryan sends chapter text
2. Poe spawns proofreading subagent
3. Subagent runs proofreading skill
4. Report generated with findings
5. Ryan approves/rejects changes
6. Subagent archives

**Key Decision Points:**
- [ ] Review priority: Chapter 1 or start mid-manuscript?
- [ ] Style consistency across 4-year writing period
- [ ] Publisher targeting criteria

---

## Revenue Stream Strategy

### Stream 1: Novel Publishing ("Take Your Liberty")
**Goal:** Complete proofreading → publish → generate revenue
**Timeline:** 6-12 months
**Tasks:**
- Chapter-by-chapter proofreading
- Publisher targeting
- Manuscript finalization
- Submission and marketing

**Dependencies:**
- ✓ Proofreading skill operational
- [ ] Shepherd agent coordination (if cross-promotion)
- [ ] Runefury branding (if novel tie-ins)

---

### Stream 2: Christian Gaming Network
**Goal:** Build community → monetize through reviews, ads, partnerships
**Timeline:** 3-6 months to MVP, 12+ months to revenue
**Tasks:**
- Shepherd agent setup
- Content rating system design
- Website development
- Community moderation setup
- Game review pipeline

**Dependencies:**
- [ ] Discord/Mattermost platform decision
- [ ] Content ethics guidelines
- [ ] Parental resource documentation

---

### Stream 3: AI Music Bands
**Goal:** Release albums → merch → licensing → live performances
**Timeline:** 
- Runefury: 6-9 months to first release
- Christian Linkin Park clone: 9-12 months
**Tasks:**
- Music agent setup
- Olares One integration
- Audio generation workflow
- Visual branding
- Release planning

**Dependencies:**
- [ ] ComfyUI setup on Olares One
- [ ] Music generation pipeline
- [ ] Branding and marketing strategy

---

## Communication Protocol

### Poe → Department Agents
**Primary Tool:** `sessions_send`
**Trigger:** Delegated tasks, status requests, standup meetings

**Example Workflow:**
```
Poe: "Shepherd, what's the status of the gaming site?"
Shepherd: [Reports progress]
Poe: [Synthesizes] → "Ryan, Shepherd reports: 3 reviews completed, 1 pending Discord setup"
```

### Autonomous Standups
**Pattern:**
1. Department heads read last 2-3 days of transcripts
2. Run 3 rounds of debate
3. Generate summary with action items
4. Ping Poe
5. Poe pings Ryan only when review needed

**Schedule:**
- Weekly: Full standup (all agents)
- Daily: Quick sync (when critical updates)

---

## Gateway Configuration

### Shared Gateway (Collocated)
**Agents:** Poe, Shepherd, Runefury
**Benefit:** Simplified communication, shared memory
**Setup:** One Telegram channel, one workspace

### Separate Gateways
**Tode (Work):** Isolated from creative mission
**tinyNature:** Proprietary subscription AI
**Reason:** Clear work-home boundary

---

## Implementation Timeline

### Phase 1: Foundation (Week 1)
**Priority:** Shepherd Agent
- Create workspace at `~/.openclaw/workspace-shepherd`
- Write SOUL.md (community caretaker personality)
- Write IDENTITY.md (mission, values, communication style)
- Copy USER.md (Ryan as CEO)
- Set up AGENTS.md (startup sequence)
- Configure Discord/Mattermost decision
- **Success:** Shepherd agent active, ready for subagents

### Phase 2: Music Production (Week 2-3)
**Priority:** Chester Agent
- Create workspace at `~/.openclaw/workspace-chester`
- Write SOUL.md (musical visionary personality, Chester tribute)
- Write IDENTITY.md (mission, creative vision for both bands)
- Copy USER.md (Ryan as CEO)
- Integrate with Olares One (ComfyUI)
- Set up audio generation workflow
- **Success:** Chester agent active, first music drafts ready

### Phase 3: Novel Proofreading (Week 2-3)
**Priority:** "Take Your Liberty"
- Submit Chapter 1 for proofreading
- Test subagent workflow
- Establish review feedback loop
- Continue chapter-by-chapter
- **Success:** Manuscript ready for publisher submission

### Phase 4: Integration (Week 4+)
**Priority:** Cross-agent coordination
- Enable autonomous standups
- Establish revenue tracking
- Coordinate cross-promotion (Shepherd promotes Runefury, etc.)
- Refine communication protocols
- **Success:** All agents working in harmony, revenue streams active

---

## Key Metrics

### Shepherd Agent
- [ ] Number of game reviews published
- [ ] Community size (Discord members)
- [ ] Parental resource downloads
- [ ] Content rating accuracy

### Chester Agent
- **Christian Linkin Park-style band:**
  - [ ] Number of tracks produced
  - [ ] Album release schedule
  - [ ] Visual identity
  - [ ] Christian messaging approach
- **Runefury (Medieval metal):**
  - [ ] Number of tracks produced
  - [ ] Visual assets created
  - [ ] Album release schedule
  - [ ] Merchandise designs

### Novel Proofreading
- [ ] Chapters reviewed
- [ ] Manuscript quality score
- [ ] Publisher interest
- [ ] Revenue generated

### Overall Mission
- [ ] Revenue streams established
- [ ] Time until financial independence
- [ ] Creative output quality
- [ ] Work-life balance

---

## Decision Log

### Made Today (2026-03-16)
- **Mission Statement:** "To build revenue streams that allow full-time devotion to morally-aligned creative work"
- **Poe Identity:** Chief of Staff, Muddy model, dissonant serenity voice
- **QMD Setup:** Indexed 19 files, semantic search operational
- **Memory Flush:** Enabled for automatic pre-compaction writes
- **Proofreading Skill:** Installed and tested
- **Organization Plan:** This document created
- **Agent Naming:**
  - **Shepherd** — Christian Gaming Network
  - **Chester** — Music production (tribute to Chester Bennington, Linkin Park vocalist)
  - **Runefury** — Band name managed by Chester agent
- **Priority Order:**
  1. Shepherd agent setup
  2. Chester agent setup
  3. Proofreading workflow (chapter-by-chapter)

### Pending Decisions
- [ ] Discord vs Mattermost for Shepherd
- [ ] Chapter 1 vs mid-manuscript for proofreading start
- [ ] Chester agent personality (Chester Bennington tribute tone)
- [ ] Runefury visual identity direction
- [ ] Christian Linkin Park band name
- [ ] Music genre blending approach (nu-metal + medieval for Runefury)

---

## Next Immediate Actions

**After Ryan approves this plan:**

1. **Set up Shepherd workspace** (create folder, write files)
2. **Create SOUL.md for Shepherd** (community caretaker personality)
3. **Create IDENTITY.md for Shepherd** (mission, values)
4. **Configure agent permissions** (sessions_send, gateway)
5. **Begin Shepherd subagent planning** (what tasks to delegate)

---

*This plan is a living document. Update as we build and learn.*
