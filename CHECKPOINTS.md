# CHECKPOINTS.md

## Black Feather OS - Checkpoint Rules

AI should not run important workflows invisibly.

Complex work must be broken into smaller stages where the system proves its work before proceeding.

## Core Standard

A small digital mistake must not become a real-world problem.

---

## Required Checkpoint Pattern

Each important workflow stage should have:
- clear owner
- clear inputs
- visible status
- visible output record
- next expected step
- blocker/warning field when relevant

---

## Workflow Checkpoints

### Research Checkpoint
**Before Writing begins:**
- research record exists
- record has valid status for writing
- source context is present
- metadata is present
- unresolved warnings are visible

### Writing Checkpoint
**Before drafting begins:**
- approved research exists
- duplication check exists
- article plan exists
- angle/rationale exists
- status allows drafting

### Editing Checkpoint
**Before approval:**
- draft exists
- linked research exists
- review record exists
- factual grounding review is visible
- mission/theology alignment review is visible
- warnings and revision notes are recorded

### Publication Checkpoint
**Before publish:**
- article is approved
- publication record exists
- required metadata exists
- publish status is explicit
- action is visible and recoverable where possible

### Library Checkpoint
**Before archive handoff:**
- publication record exists
- canonical article metadata exists
- linked draft/review/research ids exist

### Marketing Checkpoint
**Before promotional draft creation:**
- published article exists
- linked article id exists
- platform is explicit
- status is explicit

---

## Destructive Change Checkpoints

**Before deleting, overwriting, merging, or replacing:**
- identify target
- identify impact
- preserve rollback path where possible
- prefer reversible actions
- record what changed

---

## Scope Checkpoint for Builders

**Before changing system structure:**
- confirm requested scope
- preserve unrelated working behavior
- avoid cross-module drift
- document assumptions

---

## Human Review Principle

Where actions are public-facing, destructive, or hard to reverse, prefer visible checkpoint records and reviewable state transitions over silent automation.

---

## Failure Rule

If a checkpoint fails:
- stop progression
- preserve current state
- record blocker clearly
- do not fake completion
