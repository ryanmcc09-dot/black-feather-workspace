# HANDOFFS.md

## Black Feather OS - Handoff Map

This file defines the canonical handoff flow for the Order of Christian Gamers workspace.

---

## Core Rule

Shared records follow one-writer, many-readers.

Every shared record must have:
- one authoritative writer
- clear downstream readers
- explicit status
- explicit next step

---

## Workflow Sequence

Research -> Writing -> Editing/Publishing -> Marketing

Mission Control observes workflow state but does not replace workflow ownership.

---

## Ownership Map

### Ezra - Research
Writes:
- research records
- research summaries
- research status updates
- redundancy/relatedness flags for intake

Readers:
- Abnett
- Ed
- Robin
- Poe
- Hermes

### Abnett - Writing
Writes:
- article plans
- draft records
- draft status updates
- editorial handoff packages

Readers:
- Ed
- Robin
- Hermes
- Poe

### Ed - Editing and Publishing
Writes:
- editorial review records
- revision requests
- publication records
- Library/archive published article records

Readers:
- Robin
- Hermes
- Poe
- future Library/search workflows

### Robin - Marketing
Writes:
- marketing priority signals
- writing-influence records
- platform-specific promotional drafts
- promotion history records

Readers:
- Abnett
- Poe
- future community/distribution workflows

### Poe - Builder/Implementer
Writes:
- system-level build records
- architecture implementations
- workflow feature code
- health visibility structures
- system decisions and checkpoint records

Readers:
- all agents as needed

### Hermes - Orchestration
Writes:
- workflow coordination records
- handoff oversight records
- checkpoint enforcement records
- task routing records

Readers:
- all agents as needed

---

## Canonical Handoffs

### Research to Writing
**Input:**
- approved research records
- source summaries
- metadata
- tags
- status
- related record ids

**Output expected from Writing:**
- article plan
- duplication result
- draft record

### Writing to Editing
**Input:**
- article plan
- draft record
- linked research ids
- linked source summaries
- duplication result
- warnings or unresolved questions

**Output expected from Editing:**
- review record
- revision request or approval state
- publication record when approved

### Editing to Library
**Input:**
- approved publication record
- linked review record
- linked draft id
- linked research ids
- title, slug, excerpt, tags, article metadata

**Output:**
- canonical published article archive record

### Editing to Marketing
**Input:**
- published article record
- publication metadata
- angle summary
- topic/game metadata

**Output expected from Marketing:**
- marketing signal linkage if relevant
- platform draft records
- promotion history

---

## Rules for All Handoffs

Every handoff must include:
- status
- canonical input record ids
- canonical output record ids when created
- timestamp
- warnings/blockers if present
- next expected owner

Do not leave informal or ambiguous handoffs.

---

## Blocked Handoff Rule

If a handoff cannot proceed:
- do not fake completion
- record blocker clearly
- preserve current owner and status
- identify what is needed to resume
