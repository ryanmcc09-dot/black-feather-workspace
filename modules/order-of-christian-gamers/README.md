# Order of Christian Gamers - Module Records

This directory contains the canonical JSON record storage for the Order of Christian Gamers workflow.

## Folder Structure

```
modules/order-of-christian-gamers/
├── research/          - Ezra's domain
│   ├── records/       - Canonical research JSON records
│   └── summaries/    - Human-readable research summaries
├── writing/           - Abnett's domain
│   ├── plans/        - Article plan JSON records
│   ├── drafts/       - Draft JSON records
│   └── handoffs/    - Writing-to-Editing handoff packages
├── editing/           - Ed's domain
│   ├── reviews/      - Editorial review JSON records
│   ├── publications/ - Publication JSON records
│   └── revision-requests/ - Revision request records
├── library/           - Published articles archive
│   └── articles/    - Canonical published article records
└── marketing/        - Robin's domain
    ├── signals/      - Marketing signal JSON records
    ├── social-drafts/ - Platform-specific social draft records
    └── promotion-history/ - Promotion history records
```

## Record Naming Convention

JSON files should be named with the record ID and a `.json` extension:

```
{record-id}.json
```

Example: `research-abc123.json`

## Schema Location

Each subdirectory contains a `-schema.json` file defining the canonical schema for records in that directory.

## Ownership

| Directory | Owner | Record Type |
|-----------|-------|-------------|
| research/records | Ezra | Research records |
| writing/plans | Abnett | Article plans |
| writing/drafts | Abnett | Draft records |
| writing/handoffs | Abnett | Handoff packages |
| editing/reviews | Ed | Editorial reviews |
| editing/publications | Ed | Publication records |
| editing/revision-requests | Ed | Revision requests |
| library/articles | Ed | Published articles |
| marketing/signals | Robin | Marketing signals |
| marketing/social-drafts | Robin | Social drafts |
| marketing/promotion-history | Robin | Promotion history |

## One-Writer, Many-Readers

Each directory is owned by one agent. Other agents may read but not write to records they do not own.

## Status Fields

All records include:
- `createdAt` - ISO 8601 timestamp
- `updatedAt` - ISO 8601 timestamp (records with updates)

Status-enum records include explicit status transitions documented in each schema.
