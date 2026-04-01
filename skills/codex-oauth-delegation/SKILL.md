---
name: codex-oauth-delegation
description: Delegate coding tasks to OpenAI Codex using OAuth authentication. Use when a task involves software engineering work that benefits from repository inspection, code modification, test generation, debugging, or terminal-based execution. Codex is the coding specialist; you are the coordinator.
---

# Codex OAuth Delegation

## When to Use This Skill

Delegate to Codex when the task would benefit from:
- Repository inspection
- Code modification
- Test generation
- Debugging
- Refactoring
- Terminal-based software execution

**Do NOT use Codex for:**
- General conversation
- Non-code research (unless directly supporting a coding task)
- Broad autonomous changes without clear scoped objectives
- Destructive actions without explicit approval

## Operating Model

1. **Interpret** the user's request
2. **Decide** if it is a coding task
3. **If coding task:** Delegate implementation to Codex
4. **Give Codex** tightly scoped instructions with exact task, files/folders, constraints, success criteria
5. **Ask Codex** to make the smallest correct change
6. **Have Codex** run relevant tests/checks/validation
7. **Review** Codex's output before presenting
8. **Return** a clean summary to the user

## Delegation Rule

Only invoke Codex when the task requires code analysis or modification. If the user asks for planning only, use Codex for analysis but do not apply changes. If the user asks for implementation, let Codex propose and execute the change.

## Instruction Template

When delegating to Codex, use this format:

```
[CODEX TASK START]
Repository/context:
{{repo_or_workspace}}

User goal:
{{user_goal}}

Task:
{{specific_task}}

Constraints:
* Make the smallest possible correct change
* Do not modify unrelated files
* Preserve existing behavior unless the task requires changes
* Prefer minimal dependencies
* Follow the existing code style and architecture
* Ask for clarification only if absolutely blocked by ambiguity

Validation:
* Run the most relevant tests/checks available
* If no tests exist, perform the safest available validation
* Report any commands run

Return format:
1. Summary
2. Files changed
3. Key implementation notes
4. Validation performed
5. Risks or follow-ups
[CODEX TASK END]
```

## Behavior Requirements

- Never hand Codex a vague request when a precise one can be formed first
- Break large coding requests into smaller Codex tasks when appropriate
- Prefer targeted edits over repo-wide rewrites
- If the task is high-risk, ask for confirmation before destructive or irreversible actions

## Output Style to User

After Codex completes work, explain:
- What was done
- Where it was done
- How it was validated
- Anything the user should review next

## Example Routing

| User Request | Action |
|--------------|--------|
| "Fix this bug in the auth flow" | Use Codex |
| "Add tests for this module" | Use Codex |
| "Refactor this function without changing behavior" | Use Codex |
| "Explain what this file does" | Codex may inspect, then you summarize |
| "Brainstorm product ideas" | Do NOT use Codex |

## Authentication

Codex uses **OAuth authentication** (not API key). The OAuth setup is configured through OpenClaw's interface. Your API key is for your vision model only, not Codex.

## Default Principle

Codex is the coding specialist. You are the coordinator. Use Codex for implementation and verification, then translate the result into a clear answer for the user.
