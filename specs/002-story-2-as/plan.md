
# Implementation Plan: Privacy-Safe Website Implementation

**Branch**: `002-story-2-as` | **Date**: Saturday, October 4, 2025 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/002-story-2-as/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from file system structure or context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code, or `AGENTS.md` for all other agents).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

**IMPORTANT**: The /plan command STOPS at step 7. Phases 2-4 are executed by other commands:
- Phase 2: /tasks command creates tasks.md
- Phase 3-4: Implementation execution (manual or via tools)

## Summary
Implement privacy-safe website measures ensuring no tracking scripts or mechanisms compromise visitor privacy. The implementation will involve removing existing tracking mechanisms, implementing technical controls to prevent future tracking integration, and establishing verification procedures to maintain compliance with privacy standards.

## Technical Context
**Language/Version**: HTML/CSS/JavaScript, Hugo templating (Go-based)  
**Primary Dependencies**: Hugo static site generator, potentially privacy-compliant analytics alternatives  
**Storage**: N/A (static site, no server-side storage needed)  
**Testing**: Hugo built-in testing, HTML/CSS validation tools, privacy scanner tools  
**Target Platform**: Web browsers, GitHub Pages hosting  
**Project Type**: web (static site using Hugo framework)  
**Performance Goals**: Fast loading times, minimal resource usage, privacy-compliant delivery  
**Constraints**: Must not include tracking scripts, cookies for tracking, fingerprinting, or data collection beyond essential server logs
**Scale/Scope**: Personal website/blog with portfolio and weekly AI-generated posts

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on the constitution principles:
- ✅ Clarity First: Solution will be simple and readable
- ✅ Human-in-Loop: AI assists with implementation, human reviews changes
- ✅ Enhanced Transparency: AI assistance documented in implementation
- ✅ Automation: Implementation will use available automation tools
- ✅ Privacy-Safe: Core requirement of this feature - no trackers or data leaks
- ✅ Versioned Truth: All changes via PRs to main branch
- ✅ Security: No secrets stored in repository

## Project Structure

### Documentation (this feature)
```
specs/002-story-2-as/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
hugo.toml                 # Hugo configuration
archetypes/               # Content templates
assets/                   # SCSS, JS, images
config/                   # Site configuration
content/                  # Markdown content (posts, pages)
data/                     # Data files
layouts/                  # Hugo templates
static/                   # Static assets
public/                   # Generated site (gitignored)
scripts/                  # Automation scripts
.specify/                 # Specification framework
.github/                  # GitHub configuration
```

**Structure Decision**: This is a Hugo static site, so we'll update the Hugo templates and configuration to ensure privacy-safe implementation. The core changes will be in layouts/, assets/, and config/ directories to prevent tracking mechanisms.

## Phase 0: Outline & Research
1. **Extract research tasks** from Technical Context above:
   - Research privacy-safe alternatives to common tracking tools
   - Research best practices for Hugo privacy-safe implementations
   - Research tools for verifying absence of tracking mechanisms

2. **Generate and dispatch research agents**:
   ```
   Task: "Research privacy-safe alternatives to Google Analytics for Hugo sites"
   Task: "Find best practices for implementing privacy-safe Hugo sites with no tracking"
   Task: "Research tools and methods to verify tracking mechanisms are not present"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all research consolidated

## Phase 1: Design & Contracts
*Prerequisites: research.md complete*

1. **Extract entities from feature spec** → `data-model.md`:
   - Since this is a privacy-safe website implementation, there are no new data entities needed
   - Document the existing content entities in the Hugo site (posts, pages, etc.)
   - Define the privacy controls and verification mechanisms

2. **Generate verification checks** from functional requirements:
   - For each privacy requirement → verification test
   - Create methods to check for tracking scripts
   - Document compliance verification procedures

3. **Generate verification tests** from requirements:
   - One test per functional requirement
   - Verify absence of tracking mechanisms
   - Tests will initially fail until implementation is complete

4. **Extract test scenarios** from user stories:
   - Each story → integration test scenario
   - Quickstart test = story validation steps
   - Ensure site passes privacy verification tests

5. **Update agent file incrementally** (O(1) operation):
   - Run `.specify/scripts/bash/update-agent-context.sh qwen`
     **IMPORTANT**: Execute it exactly as specified above. Do not add or remove any arguments.
   - If exists: Add only NEW tech from current plan
   - Preserve manual additions between markers
   - Update recent changes (keep last 3)
   - Keep under 150 lines for token efficiency
   - Output to repository root

**Output**: data-model.md, /contracts/*, failing tests, quickstart.md, agent-specific file

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base
- Generate tasks from Phase 1 design docs (verification checks, requirements)
- Each privacy requirement → implementation task [P]
- Each verification test → verification implementation task [P]
- Each site configuration → privacy-safe configuration task
- Implementation tasks to make privacy tests pass

**Ordering Strategy**:
- TDD order: Verification tests before implementation 
- Dependency order: Hugo templates and configurations before content
- Mark [P] for parallel execution (independent files)

**Estimated Output**: 25-30 numbered, ordered tasks in tasks.md

**IMPORTANT**: This phase is executed by the /tasks command, NOT by /plan

## Phase 3+: Future Implementation
*These phases are beyond the scope of the /plan command*

**Phase 3**: Task execution (/tasks command creates tasks.md)  
**Phase 4**: Implementation (execute tasks.md following constitutional principles)  
**Phase 5**: Validation (run tests, execute quickstart.md, performance validation)

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |


## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented

---
*Based on Constitution v2.1.1 - See `/memory/constitution.md`*
