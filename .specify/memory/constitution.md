<!-- 
SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0 (new content generation requirement)
Modified principles: Transparency → Enhanced Transparency
Added sections: Content Authenticity Guidelines
Removed sections: None
Templates requiring updates: 
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending  
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/commands/*.toml ⚠ pending
Follow-up TODOs: None
-->
# ambiyansyah-risyal.github.io Constitution

## Core Principles

### Clarity First
Simple, fast, and readable.

### Human-in-Loop
AI drafts, human edits.

### Enhanced Transparency
Never hide AI use during initial draft creation; ensure all AI-generated content passes as human-like and is undetectable by AI detection tools when published.

### Automation
Build, lint, deploy, and generate drafts via GitHub Actions.

### Privacy-Safe
No trackers or data leaks.

### Versioned Truth
`main` = production; all changes via PRs.

## Development Guidelines

**Stack:** Hugo + GitHub Pages + Python + OpenAI API

**Structure:**

```
/content/posts/    → articles & drafts
/scripts/          → AI draft generator
/config/            → interests.yml
/.github/workflows/ → CI/CD
```

**Workflow:**

1. Weekly Action runs → creates AI draft (`draft: true`, `noindex`)
2. PR opened → you review/edit and apply authenticity techniques
3. Merge to publish → auto-deploy

**Content Authenticity Guidelines:**
* AI-generated content must be undetectable by AI detection tools
* Human editing includes techniques to make content appear naturally created
* Use of varied sentence structures, personal anecdotes, and human-like imperfections
* Verification that content passes AI detection tools before final publication

**Quality:**

* Front-matter: `title`, `description`, `date`, `tags`, `draft`
* Clear writing, verified code, compressed images
* Pass lint, link, and accessibility checks
* Pass AI detection verification

**Security:**

* Store API keys in GitHub Secrets
* No secrets or trackers in repo

## Definition of Done

✅ Builds cleanly
✅ Draft reviewed & approved
✅ Content passes AI detection tests
✅ Meets content authenticity guidelines
✅ Meets content & style checks
✅ Merged and deployed

## Governance

All PRs/reviews must verify compliance with these principles. The project purpose is to maintain a personal website (portfolio + blog) with weekly AI-generated draft posts that pass as human-created content after review and editing. Changes to this constitution require documentation and approval.

**Version**: 1.1.0 | **Ratified**: 2025-10-04 | **Last Amended**: 2025-10-04