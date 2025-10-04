# Tasks: Initialize and Set Up Hugo Site

**Input**: Design documents from `/specs/001-story-1-as/`
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
- **Single project**: `config/_default/`, `content/`, `layouts/`, `static/`, `themes/` at repository root
- **Hugo site**: Following standard Hugo directory structure
- Paths shown below assume Hugo site structure - adjust based on plan.md structure

## Phase 3.1: Setup
- [ ] T001 Install Hugo v0.120.0 or latest stable
- [ ] T002 Initialize Hugo site structure with proper directory layout
- [ ] T003 [P] Initialize Git repository for the Hugo site
- [ ] T004 [P] Configure .gitignore for Hugo project

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T005 [P] Contract test for site configuration in tests/contract/test_site_config.py
- [ ] T006 [P] Contract test for blog post structure in tests/contract/test_blog_post.py
- [ ] T007 [P] Contract test for portfolio item structure in tests/contract/test_portfolio.py
- [ ] T008 [P] Integration test for site build process in tests/integration/test_build.py
- [ ] T009 [P] Integration test for mobile responsiveness in tests/integration/test_responsiveness.py
- [ ] T010 [P] Integration test for accessibility compliance in tests/integration/test_accessibility.py

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T011 [P] Create site configuration in config/_default/config.toml
- [ ] T012 [P] Create site parameters in config/_default/params.toml
- [ ] T013 [P] Create navigation menu in config/_default/menu.toml
- [ ] T014 [P] Create blog post archetype in archetypes/posts.md
- [ ] T015 [P] Create portfolio item archetype in archetypes/portfolio.md
- [ ] T016 Install and configure Ananke theme as submodule
- [ ] T017 [P] Create content directory structure (content/posts/, content/portfolio/)
- [ ] T018 [P] Create example blog post in content/posts/my-first-post.md
- [ ] T019 [P] Create example portfolio item in content/portfolio/my-project.md
- [ ] T020 [P] Create basic layout templates in layouts/
- [ ] T021 [P] Create static assets directories (static/css/, static/js/, static/images/)

## Phase 3.4: Integration
- [ ] T022 Configure GitHub Pages deployment workflow in .github/workflows/deploy.yml
- [ ] T023 Add accessibility features to HTML templates
- [ ] T024 Optimize images for web in static/images/
- [ ] T025 Implement responsive design in static/css/

## Phase 3.5: Polish
- [ ] T026 [P] Create README.md with project documentation
- [ ] T027 [P] Create .github/CODEOWNERS file
- [ ] T028 [P] Create development documentation in docs/development.md
- [ ] T029 [P] Create content creation guidelines in docs/content-guidelines.md
- [ ] T030 [P] Create .github/ISSUE_TEMPLATE/feature_request.md
- [ ] T031 Run accessibility validation using aXe or Lighthouse
- [ ] T032 Verify mobile responsiveness on different screen sizes
- [ ] T033 Run Hugo build with minification to verify performance targets
- [ ] T034 Verify all links are working correctly

## Dependencies
- T001 blocks T002 (Hugo needed to initialize site)
- T002 blocks T011-T021 (site structure needed before configuration)
- T011-T013 blocks T016 (configuration needed before theme)
- T016 blocks T020 (theme needed for templates)
- Tests (T005-T010) before implementation (T011-T021)
- T011-T021 before integration (T022-T025)
- Integration before polish (T026-T034)

## Parallel Example
```
# Launch T005-T010 together (contract and integration tests):
Task: "Contract test for site configuration in tests/contract/test_site_config.py"
Task: "Contract test for blog post structure in tests/contract/test_blog_post.py"
Task: "Contract test for portfolio item structure in tests/contract/test_portfolio.py"
Task: "Integration test for site build process in tests/integration/test_build.py"
Task: "Integration test for mobile responsiveness in tests/integration/test_responsiveness.py"
Task: "Integration test for accessibility compliance in tests/integration/test_accessibility.py"
```

# Launch T011, T012, T013, T014, T015, T017, T018, T019, T020, T021 together (independent files):
Task: "Create site configuration in config/_default/config.toml"
Task: "Create site parameters in config/_default/params.toml"
Task: "Create navigation menu in config/_default/menu.toml"
Task: "Create blog post archetype in archetypes/posts.md"
Task: "Create portfolio item archetype in archetypes/portfolio.md"
Task: "Create content directory structure (content/posts/, content/portfolio/)"
Task: "Create example blog post in content/posts/my-first-post.md"
Task: "Create example portfolio item in content/portfolio/my-project.md"
Task: "Create basic layout templates in layouts/"
Task: "Create static assets directories (static/css/, static/js/, static/images/)"
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
   - Each configuration element → implementation task
   
2. **From Data Model**:
   - Each entity → content structure task [P]
   - Each directory → creation task [P]
   
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