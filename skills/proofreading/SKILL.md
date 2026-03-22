# Proofreading Skill

## Purpose
Systematically review manuscript chapters for:
- Grammar, spelling, and punctuation
- Style consistency (voice, tense, perspective)
- Pacing and flow
- Clarity and readability
- Formatting issues

## Mission Alignment
Support the author's goal: **To build revenue streams that allow full-time devotion to morally-aligned creative work.**

## Workflow

### Input Required
1. Chapter text (markdown or plain text)
2. Chapter number/title
3. Any specific concerns (e.g., "check dialogue," "verify pacing")

### Processing Steps

**Step 1: Grammar & Mechanics**
- Check spelling, punctuation, grammar
- Flag inconsistent usage (e.g., em dashes vs. en dashes)
- Verify proper noun consistency

**Step 2: Style & Voice**
- Check for consistency in:
  - Narrative voice (first/third person)
  - Tense (past/present)
  - Tone (serious, humorous, etc.)
  - Character speech patterns
- Note deviations that break immersion

**Step 3: Flow & Pacing**
- Identify sections that drag
- Flag abrupt transitions
- Note potential pacing issues

**Step 4: Formatting**
- Check paragraph structure
- Verify dialogue formatting
- Note scene break clarity

**Step 5: Report Generation**
- Compile findings into structured report
- Prioritize critical issues vs. suggestions
- Format for easy author review

### Output Format

```
## Chapter [X]: [Title] - Proofreading Report

### Critical Issues (Must Fix)
- [Issue 1]
- [Issue 2]

### Style Consistency
- [Voice/tense/perspective notes]

### Grammar & Mechanics
- [Spelling/grammar flags]

### Pacing & Flow
- [Slow sections, abrupt transitions]

### Formatting
- [Paragraph/dialogue issues]

### Recommendations
1. [Action item 1]
2. [Action item 2]

### Overall Assessment
[Brief summary of chapter quality]
```

## Integration Notes

### For Subagent Use
This skill is designed to be called by subagents spawned for chapter-by-chapter proofreading.

**Constraints:**
- No persistent memory needed between chapters (each chapter is standalone)
- Focus on current chapter quality
- Flag recurring issues for author awareness
- Keep report concise (under 2000 words)

### For Persistent Agent Use
If a dedicated Proofreading Agent is later created:
- Maintain style guide across all chapters
- Track recurring issues
- Build vocabulary consistency database
- Learn author's preferences over time

## Example Usage

**Author sends:**
> "Here's Chapter 3. Main concerns: check the dialogue tags, make sure the pacing doesn't drag in the middle."

**Skill processes:**
1. Reviews dialogue tag consistency
2. Identifies slow section (paragraphs 12-18)
3. Checks for em dash overuse (per Ryan's preference)
4. Generates report

**Output:**
> Proofreading Report: Chapter 3
> 
> **Critical Issues:** 2
> **Style Notes:** 3 deviations from Chapter 1-2 voice
> **Pacing:** Chapter slows at paragraph 14, suggest tightening dialogue
> **Dialogue Tags:** Consistent, but overuse of "he said/she said" at paragraph 9
> **Recommendation:** Vary dialogue tags, trim slow section

## Settings

### Style Preferences (Configurable)
- **Em dashes:** Avoid (per author preference)
- **Contractions:** Accept (natural dialogue) or avoid (formal narrative)
- **Tense:** [auto-detected] or [force consistency]
- **Perspective:** [auto-detected] or [enforce consistency]

### Report Level
- **Quick:** 500 words max, critical issues only
- **Standard:** 1000-1500 words, full coverage
- **Detailed:** 2000+ words, with examples and alternatives

## Author Guidelines

### What the Skill Will Do
- Find errors and inconsistencies
- Suggest improvements for clarity
- Flag pacing issues
- Maintain style consistency

### What the Skill Won't Do
- Rewrite your voice
- Change your story
- Decide plot direction
- Replace human editor judgment

### Author Review
All suggestions must be reviewed and approved by author. Skill provides options, not mandates.

## Version
v1.0 - 2026-03-16
