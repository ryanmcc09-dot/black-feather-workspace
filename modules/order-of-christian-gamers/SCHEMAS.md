# Canonical Record Schemas

All JSON schemas for Order of Christian Gamers workflow records.

## Schema Index

| Schema | Owner | File |
|--------|-------|------|
| Research Record | Ezra | `research/records/research-record-schema.json` |
| Article Plan | Abnett | `writing/plans/article-plan-schema.json` |
| Draft Record | Abnett | `writing/drafts/draft-record-schema.json` |
| Writing Handoff | Abnett | `writing/handoffs/writing-handoff-schema.json` |
| Editorial Review | Ed | `editing/reviews/editorial-review-schema.json` |
| Revision Request | Ed | `editing/revision-requests/revision-request-schema.json` |
| Publication Record | Ed | `editing/publications/publication-record-schema.json` |
| Library Article | Ed | `library/articles/library-article-schema.json` |
| Marketing Signal | Robin | `marketing/signals/marketing-signal-schema.json` |
| Social Draft | Robin | `marketing/social-drafts/social-draft-schema.json` |
| Promotion History | Robin | `marketing/promotion-history/promotion-history-schema.json` |

## Record ID Format

Record IDs should be:
- Unique across the system
- URL-safe
- Descriptive when possible

Recommended format: `{type}-{short随机}`

Example: `research-a1b2c3`, `draft-d4e5f6`, `pub-g7h8i9`

## Storage Pattern

Records are stored as individual JSON files in their respective directories.

```
{directory}/{record-id}.json
```

Example: `research/records/research-a1b2c3.json`
