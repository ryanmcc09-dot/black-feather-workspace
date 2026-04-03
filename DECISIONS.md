# DECISIONS.md

## Black Feather OS - Architecture Decisions

Use this file to record finalized decisions that should persist across sessions.

Each entry should be short and structured.

---

## Template

### [YYYY-MM-DD] Decision Title
- Decision:
- Reason:
- Impact:
- Related files/modules:

---

### [2026-03-31] Build OS before agents
- Decision: Build Black Feather OS structure before fully activating the agent team.
- Reason: Stable architecture should exist before deep skills, autonomy, and project assignments are added.
- Impact: Current work prioritizes shell, modules, workflows, and records before full agent activation.
- Related files/modules: OS Shell, Order of Christian Gamers, agent scaffolding

### [2026-03-31] Order of Christian Gamers is the first deep module
- Decision: Build Order of Christian Gamers as the first mature module pattern.
- Reason: It is the furthest defined workflow and can serve as the template for later modules.
- Impact: Music Studio and Game Development Company remain lighter placeholders for now.
- Related files/modules: Order of Christian Gamers, OS Shell

### [2026-03-31] Library is downstream of Editing
- Decision: Library is a secondary page reached from Editing, not a top-level primary workflow tab.
- Reason: Library stores published articles for posterity and search after editorial approval and publication.
- Impact: Editing owns the handoff into Library/archive.
- Related files/modules: Editing, Library

### [2026-03-31] Editing owns publication
- Decision: Editing/Publishing is the only workflow allowed to move articles into published status.
- Reason: Publication should sit behind the final quality and alignment checkpoint, not under Marketing or Writing.
- Impact: Marketing reads published content but does not publish canonical blog articles.
- Related files/modules: Editing, Library, Marketing

### [2026-03-31] Filesystem-first architecture
- Decision: The filesystem is the integration layer; JSON is source truth and Markdown is readable handoff.
- Reason: This supports local-first operation, agent clarity, inspectability, and recoverability.
- Impact: Module and workflow design should favor clear files, records, and handoffs over hidden orchestration.
- Related files/modules: all modules, storage design

### [2026-03-31] Horizontal layout for home page icons
- Decision: Replaced radial spoke layout with horizontal row of icons.
- Reason: Radial CSS positioning with trigonometry was unreliable across viewports.
- Impact: Icons now use flexbox for consistent horizontal alignment.
- Related files/modules: OS Shell, Home Page

### [2026-03-31] Five-agent team structure
- Decision: Created five-agent team: Poe (orchestrator), Ezra (research), Abnett (writing), Ed (editing), Robin (marketing).
- Reason: Narrow roles prevent role drift and clarify ownership.
- Impact: Each agent owns their records; one-writer-many-readers enforced.
- Related files/modules: Agent framework, HANDOFFS.md

### [2026-04-03] Hermes as orchestrator, Poe as builder
- Decision: Hermes becomes primary orchestrator; Poe becomes builder/implementer.
- Reason: Clear role separation between workflow coordination (Hermes) and system building (Poe).
- Impact: Hermes handles coordination, handoffs, and task routing. Poe handles implementation, architecture, and module building.
- Related files/modules: SOUL.md, IDENTITY.md, SYSTEM-REFERENCE.md, HANDOFFS.md, BOUNDARIES.md

---

*Decisions are finalized choices, not brainstorming. Update only when a decision is truly settled.*
