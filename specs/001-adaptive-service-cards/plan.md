# Implementation Plan: Adaptive Service Cards

**Branch**: `mvp-v0.1.0` | **Date**: 2026-07-03 | **Spec**: [`specs/001-adaptive-service-cards/spec.md`](./spec.md)

**Input**: Feature specification from `/specs/001-adaptive-service-cards/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Align the services-page cards with the larger integrations-page visual baseline, then let the services grid adapt to growing card counts without relying on a fixed column count tuned only for the current three services. The implementation should stay within the existing generated static-dashboard architecture by updating the shared source data, service-card rendering surface, and shared stylesheet rather than hand-editing generated HTML.

## Technical Context

**Language/Version**: HTML5, CSS3, small inline browser JavaScript, and Python 3 build scripts

**Primary Dependencies**: Browser-native HTML/CSS/JS, Python standard-library build pipeline, local font/icon assets

**Storage**: Static JSON source files in `src/dashboard_shell/`

**Testing**: Python `unittest` for generator assertions plus manual browser validation of responsive layout and card usability

**Target Platform**: Desktop-first static browser prototype opened directly from generated `.html` files, with responsive behavior for narrower screens

**Project Type**: Generated static multi-page web prototype

**Performance Goals**: Keep the services catalog readable without horizontal scrolling at default desktop widths, preserve visible card actions and titles after reflow, and rebuild generated pages through one local command

**Constraints**: Do not hand-edit generated page output as source of truth; preserve the existing service-card actions and navigation; keep the implementation compatible with the existing generator and shared stylesheet; avoid a layout tuned to a hard maximum service count

**Scale/Scope**: One service-catalog screen within a seven-page prototype, shared across the existing `ServiceListPage` rendering path and expected to support a growing multi-row services collection

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- The current constitution file is still an unfilled template with placeholder sections and no ratified, enforceable project principles.
- No active constitution gates block this feature at plan time.
- Plan remains aligned with the repo's documented generator-first structure in `README.md` and `CONTEXT.md`: update source assets, renderer inputs, and shared styling rather than editing generated HTML directly.
- Post-design re-check: Pass. The planned artifacts keep the change surface small, reuse the existing `ServiceListPage` and `EntityCard` seams, and do not introduce new architectural layers.

## Project Structure

### Documentation (this feature)

```text
specs/001-adaptive-service-cards/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
```text
assets/
├── fonts/
├── icons/
└── js/
   ├── controllers/
   └── pages/

src/
└── dashboard_shell/
   ├── entity-cards.json
   ├── header-addons.json
   ├── icon-sprite.html
   ├── pages.json
   ├── template.html
   ├── tree-menus.json
   └── partials/
      ├── card-grid.html
      ├── environment-card.html
      ├── service-card.html
      ├── services-grid.html
      └── services-toolbar.html

scripts/
├── build_dashboard_shell.py
└── dashboard_shell_build/
   ├── context.py
   ├── entity_cards.py
   ├── header_addons.py
   ├── output_writer.py
   ├── page_specs.py
   ├── shell.py
   └── tree_menus.py

specs/
└── 001-adaptive-service-cards/
   ├── spec.md
   ├── plan.md
   ├── research.md
   ├── data-model.md
   ├── quickstart.md
   └── contracts/

tests/
└── test_dashboard_shell_labels.py

style.css
```

**Structure Decision**: Use the existing single-project static prototype structure. Implement the feature through source data and generator seams under `src/dashboard_shell/` and `scripts/dashboard_shell_build/`, with layout changes centralized in `style.css` and verification through the existing Python test directory plus manual page review.

## Complexity Tracking

No constitution violations require justification for this feature.
