---

description: "Task list for implementing adaptive service cards"
---

# Tasks: Adaptive Service Cards

**Input**: Design documents from `/specs/001-adaptive-service-cards/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No automated test-first requirement was specified in the feature spec. This task list includes implementation and validation tasks, with manual end-to-end checks driven by `quickstart.md` and targeted generator checks where needed.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare the feature inputs and validation path without changing generated output directly.

- [X] T001 [P] Review the current services-page source configuration in `src/dashboard_shell/pages.json`, `src/dashboard_shell/entity-cards.json`, and `src/dashboard_shell/partials/services-grid.html`
- [X] T002 [P] Review the current card-size baseline and responsive breakpoints in `style.css` against the environment-card layout used by `src/dashboard_shell/partials/card-grid.html` and `src/dashboard_shell/partials/environment-card.html`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Establish shared rendering and validation seams that all user stories depend on.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 [P] Update `specs/001-adaptive-service-cards/quickstart.md` with the exact validation dataset and page-comparison steps the implementation will use
- [X] T004 [P] Create a validation-only services dataset in `tests/fixtures/services-expanded.json` that covers default, multi-row, navigable, and long-title service entries
- [X] T005 Update `tests/test_dashboard_shell_labels.py` or supporting build helpers to load `tests/fixtures/services-expanded.json` for expanded-catalog validation scenarios

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Keep Service Cards Scannable as the Catalog Grows (Priority: P1) 🎯 MVP

**Goal**: Make the services-page cards start near the integrations-page footprint and adapt cleanly as the grid fills with more service cards.

**Independent Test**: Open `integrations.html` and `services.html` after rebuilding, confirm the starting services-card footprint is close to the integrations baseline, then confirm the expanded validation dataset reflows into orderly rows without horizontal scrolling at default desktop width.

### Implementation for User Story 1

- [X] T006 [US1] Update the services-grid layout rules in `style.css` to derive columns from a larger minimum card footprint instead of the fixed five-column desktop layout
- [X] T007 [US1] Update the service-card sizing rules in `style.css` so the default service-card height, padding, and spacing align with the integrations-page baseline while still supporting dense multi-row layouts
- [X] T008 [US1] Verify whether `src/dashboard_shell/partials/services-grid.html` and `scripts/dashboard_shell_build/page_specs.py` require structural changes for the adaptive grid
- [X] T009 [US1] Update `src/dashboard_shell/partials/services-grid.html` and `scripts/dashboard_shell_build/page_specs.py` if structural grid-container changes are required
- [X] T010 [US1] Rebuild generated pages with `python scripts/build_dashboard_shell.py` and verify the updated output in `services.html`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Support Adding New Services Without Manual Layout Rework (Priority: P2)

**Goal**: Ensure newly added service entries flow into the same adaptive layout without special-case adjustments.

**Independent Test**: Load the expanded validation dataset in `tests/fixtures/services-expanded.json`, rebuild with `python scripts/build_dashboard_shell.py`, and confirm the new cards appear in `services.html` with the same layout behavior as existing cards.

### Implementation for User Story 2

- [X] T011 [US2] Normalize the services collection in `src/dashboard_shell/entity-cards.json` so newly added entries follow the same field expectations for titles, actions, and optional navigation
- [X] T012 [US2] Update `scripts/dashboard_shell_build/entity_cards.py` to preserve consistent service-card rendering for larger service collections and optional navigable cards
- [X] T013 [US2] Rebuild generated pages with `python scripts/build_dashboard_shell.py` and confirm validation-only expanded service entries render correctly in `services.html`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Preserve Service Card Actions While Resizing (Priority: P3)

**Goal**: Keep titles, delete actions, more-actions controls, and stretched-link navigation usable after card resizing and responsive reflow.

**Independent Test**: Open `services.html` at 1280px, 900px, and 640px viewport widths, then verify each visible service card keeps a readable title and accessible delete, more-actions, and navigation affordances without overlap.

### Implementation for User Story 3

- [X] T014 [US3] Update the service-card markup in `src/dashboard_shell/partials/service-card.html` if needed to reserve stable structure for actions, icon, and title during resized states
- [X] T015 [US3] Update the service-card interaction and layering rules in `style.css` so actions remain clickable and long titles remain identifiable across adaptive and responsive states
- [X] T016 [US3] Rebuild generated pages with `python scripts/build_dashboard_shell.py` and verify the interactive service-card output in `services.html`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final consistency, validation, and generated-output review across all stories

- [X] T017 [P] Update feature notes in `specs/001-adaptive-service-cards/quickstart.md` and `specs/001-adaptive-service-cards/contracts/service-grid-ui-contract.md` if implementation details changed during delivery
- [X] T018 [P] Add or update generator assertions for the services-page rendering change in `tests/test_dashboard_shell_labels.py`
- [X] T019 Run `python -m unittest discover -s tests` from the repository root and address any generator regressions in `tests/test_dashboard_shell_labels.py` or the affected source files
- [X] T020 Run the full manual validation flow in `specs/001-adaptive-service-cards/quickstart.md` against `integrations.html` and `services.html`, including the SC-001 10% card-footprint comparison, no-horizontal-scroll validation, and responsive action/title checks

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational completion
- **User Story 2 (Phase 4)**: Depends on Foundational completion and benefits from User Story 1 grid sizing being in place
- **User Story 3 (Phase 5)**: Depends on User Story 1 sizing changes and User Story 2 rendering consistency
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - MVP story
- **User Story 2 (P2)**: Can start after Foundational (Phase 2), but final validation depends on the adaptive grid from US1
- **User Story 3 (P3)**: Depends on the resized/reflowing card states introduced by US1 and exercised through the expanded catalog from US2

### Within Each User Story

- Shared source data and validation setup before implementation
- Grid/container behavior before story-specific rendering refinements
- Rendering consistency before interaction-layer polish
- Rebuild generated pages after each story before validation

### Parallel Opportunities

- `T001` and `T002` can run in parallel during Setup
- `T003` and `T004` can run in parallel during Foundational work
- `T017` and `T018` can run in parallel with final regression review once implementation is stable

---

## Parallel Example: User Story 1

```bash
# Parallel preparation before the core CSS change:
Task: "Review the current services-page source configuration in src/dashboard_shell/pages.json, src/dashboard_shell/entity-cards.json, and src/dashboard_shell/partials/services-grid.html"
Task: "Review the current card-size baseline and responsive breakpoints in style.css against the environment-card layout used by src/dashboard_shell/partials/card-grid.html and src/dashboard_shell/partials/environment-card.html"

# Parallel foundational preparation:
Task: "Update specs/001-adaptive-service-cards/quickstart.md with the exact validation dataset and page-comparison steps the implementation will use"
Task: "Create a validation-only services dataset in tests/fixtures/services-expanded.json that covers default, multi-row, navigable, and long-title service entries"
```

## Parallel Example: User Story 2

```bash
# Once User Story 1 is stable, these tracks can be split by contributor:
Task: "Normalize the services collection in src/dashboard_shell/entity-cards.json so newly added entries follow the same field expectations for titles, actions, and optional navigation"
Task: "Review the current service-card renderer in scripts/dashboard_shell_build/entity_cards.py for assumptions that break larger service collections or optional navigable cards"
```

## Parallel Example: User Story 3

```bash
# Preparation and validation can be split while the card interaction polish is in progress:
Task: "Review the service-card markup in src/dashboard_shell/partials/service-card.html for stable action, icon, and title structure during resized states"
Task: "Prepare responsive validation runs from specs/001-adaptive-service-cards/quickstart.md against integrations.html and services.html"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Compare `integrations.html` and `services.html`, confirm the services grid remains readable with the expanded validation dataset, and verify the SC-001 10% footprint threshold

### Incremental Delivery

1. Complete Setup + Foundational → shared inputs and validation dataset ready
2. Add User Story 1 → validate baseline sizing and adaptive grid behavior
3. Add User Story 2 → validate new services join the grid without special layout work
4. Add User Story 3 → validate actions and titles remain usable in resized states
5. Finish with regression and manual quickstart validation

### Parallel Team Strategy

1. One contributor handles source/data preparation (`T001`-`T005`)
2. One contributor handles grid and sizing changes for US1 (`T006`-`T010`)
3. Once US1 stabilizes, a second contributor can handle rendering consistency for US2 while another handles interaction polish for US3

---

## Notes

- All tasks follow the required checklist format with IDs, optional `[P]` markers, story labels where applicable, and exact file paths
- Generated root HTML files are rebuild targets, not source-edit targets
- User Story 1 is the recommended MVP scope
- Manual validation remains required because layout geometry is not fully covered by current automated tests
