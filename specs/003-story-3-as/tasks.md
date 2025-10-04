# Tasks: Clear and Readable Site Design

**Input**: Design documents from `/specs/003-story-3-as/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Hugo Site**: `assets/`, `layouts/`, `content/`, `static/` at repository root
- Paths shown below assume Hugo static site - adjust based on plan.md structure

## Phase 3.1: Setup
- [x] T001 Update hugo.toml with readability configuration settings
- [x] T002 Set up CSS architecture following Bootstrap framework
- [x] T003 [P] Create assets/scss/readability/ directory structure

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [x] T004 [P] Contract test for GET /api/readability-settings in tests/contract/test_readability_get.js
- [x] T005 [P] Contract test for PUT /api/readability-settings in tests/contract/test_readability_put.js
- [x] T006 [P] Integration test for accessibility compliance in tests/integration/test_accessibility.js
- [x] T007 [P] Integration test for responsive text sizing in tests/integration/test_responsive_typography.js

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [x] T008 [P] Create content item model in assets/js/models/ContentItem.js
- [x] T009 [P] Create layout component model in assets/js/models/LayoutComponent.js
- [x] T010 [P] Create user preference model in assets/js/models/UserPreference.js
- [x] T011 Create base readability CSS in assets/scss/readability/_base.scss
- [x] T012 Create typography CSS in assets/scss/readability/_typography.scss
- [x] T013 Create accessibility CSS in assets/scss/readability/_accessibility.scss
- [x] T014 Create responsive design CSS in assets/scss/readability/_responsive.scss
- [x] T015 Create readability settings API endpoints in layouts/partials/readability-settings.html
- [x] T016 Create readability controls component in layouts/partials/readability-controls.html
- [x] T017 Add readability CSS to main SCSS bundle in assets/scss/main.scss
- [x] T018 Add JavaScript functionality for readability settings in assets/js/readability.js
- [x] T019 Add WCAG 2.1 AA compliance features to layouts/_default/baseof.html

## Phase 3.4: Integration
- [x] T020 Integrate readability CSS with existing layout templates
- [x] T021 Connect user preference model to local storage
- [x] T022 Add readability controls to navigation/header
- [x] T023 Integrate text size adjustment functionality
- [x] T024 Add high contrast mode toggle
- [x] T025 Integrate content type-specific styling
- [x] T026 Add content length management (pagination/progressive loading)

## Phase 3.5: Polish
- [x] T027 [P] Update documentation for readability features in content/docs/readability-features.md
- [x] T028 Performance optimization for CSS and JS assets
- [x] T029 Accessibility testing across all templates and content types
- [x] T030 Cross-browser compatibility testing
- [x] T031 Mobile responsiveness verification
- [x] T032 Page load performance verification under 3 seconds
- [x] T033 Run accessibility checker tools (axe-core, etc.)
- [x] T034 Update quickstart guide with new features

## Dependencies
- Tests (T004-T007) before implementation (T008-T019)
- T008, T009, T010 block T018
- T011, T012, T013, T014 block T017
- Implementation before polish (T027-T034)

## Parallel Example
```
# Launch T004-T007 together:
Task: "Contract test for GET /api/readability-settings in tests/contract/test_readability_get.js"
Task: "Contract test for PUT /api/readability-settings in tests/contract/test_readability_put.js"
Task: "Integration test for accessibility compliance in tests/integration/test_accessibility.js"
Task: "Integration test for responsive text sizing in tests/integration/test_responsive_typography.js"

# Launch T008-T010 together:
Task: "Create content item model in assets/js/models/ContentItem.js"
Task: "Create layout component model in assets/js/models/LayoutComponent.js"
Task: "Create user preference model in assets/js/models/UserPreference.js"
```

## Notes
- [P] tasks = different files, no dependencies
- Verify tests fail before implementing
- Commit after each task
- Avoid: vague tasks, same file conflicts

## Task Generation Rules
*Applied during main() execution*

1. **From Contracts**:
   - Each contract file → contract test task [P]
   - Each endpoint → implementation task
   
2. **From Data Model**:
   - Each entity → model creation task [P]
   - Relationships → service layer tasks
   
3. **From User Stories**:
   - Each story → integration test [P]
   - Quickstart scenarios → validation tasks

4. **Ordering**:
   - Setup → Tests → Models → Services → Endpoints → Polish
   - Dependencies block parallel execution

## Validation Checklist
*GATE: Checked by main() before returning*

- [ ] All contracts have corresponding tests
- [ ] All entities have model tasks
- [ ] All tests come before implementation
- [ ] Parallel tasks truly independent
- [ ] Each task specifies exact file path
- [ ] No task modifies same file as another [P] task