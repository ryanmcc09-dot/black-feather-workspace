# SYSTEM-REFERENCE.md

## Black Feather OS - System Reference

Black Feather OS is a local-first, agent-first operating system for managing modular creative and business workflows.

---

## Core Architectural Values

- The filesystem is the integration layer.
- Structured JSON is the source of truth.
- Markdown is the readable handoff layer.
- Shared records follow one-writer, many-readers.
- Memory is layered, not bloated.
- Agents should have narrow roles.
- Mission Control surfaces system health and workflow visibility.
- Important workflows require checkpoints and guardrails.

---

## Current Top-Level Structure

### OS Shell
Shared system layer:
- home page
- central logo hub
- routing
- shared layout
- shared design language
- module entry points

### Modules
- Order of Christian Gamers
- Music Studio
- Game Development Company

Order of Christian Gamers is the first deeply built module.

---

## Order of Christian Gamers - Primary Pages

- Mission Control
- Research
- Writing
- Editing
- Marketing

Secondary page:
- Library (accessed from Editing)

---

## Primary Workflow

Research -> Writing -> Editing/Publishing -> Marketing

---

## Canonical Record Principles

- JSON holds canonical structured records.
- Markdown holds readable summaries, handoffs, and review layers.
- Canonical records must not be duplicated casually.
- Every shared record should have one authoritative writer.

---

## Known Record Ownership

- Research records: Ezra
- Article plans and draft records: Abnett
- Review, publication, and Library records: Ed
- Marketing signals, platform drafts, and promotion history: Robin
- System/orchestration records: Poe

---

## Design Direction

- cyberpunk / matrix-inspired mission control
- neon cyan as shared primary system color
- module-specific neon accents where useful
- high-signal, readable, operational UI
- Lucide icons
- no emojis

---

## Storage Direction

- local-first
- lightweight
- human-readable
- inspectable
- portable
- recoverable

Preferred persistence:
- JSON
- Markdown
- simple local storage patterns before heavier infrastructure

---

## Non-Goals for Early Versions

- no unnecessary cloud dependencies
- no heavy orchestration framework
- no bloated memory/context loading
- no role drift
- no bypassing checkpoints for speed

---

## Current Team

- Poe - orchestrator and builder
- Ezra - research
- Abnett - writing
- Ed - editing/publishing
- Robin - marketing
