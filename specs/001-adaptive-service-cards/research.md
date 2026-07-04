# Phase 0 Research: Adaptive Service Cards

## Decision 1: Use responsive CSS grid sizing for the services catalog

- **Decision**: Keep the services page on a grid layout, but size the grid from a reference card footprint and let columns auto-fit available space instead of fixing the default desktop layout to five narrow columns.
- **Rationale**: The services page already represents a catalog of repeated cards, so grid remains the best fit. Deriving layout from a minimum usable card width preserves the larger starting presentation while still allowing the page to reflow as more services are added. This avoids coupling the layout to the current count of three services.
- **Alternatives considered**:
  - Flexbox with wrapping: workable, but less consistent for multi-row column alignment and more fragile with varying card content.
  - Fixed breakpoint column counts: simple, but brittle because they assume a narrow range of service counts and require repeated tuning.
  - Horizontal scroll row: preserves card size, but conflicts with the goal of supporting a growing service catalog without degrading scanning.

## Decision 2: Treat generator sources as the only editable source of truth

- **Decision**: Apply the feature through `src/dashboard_shell/`, `scripts/dashboard_shell_build/`, and `style.css`, then rebuild generated HTML.
- **Rationale**: The repo explicitly documents the root `.html` files as generated outputs. The existing page architecture already routes the services page through `pages.json`, `page_specs.py`, `entity_cards.py`, and HTML partials. Keeping changes in those inputs preserves the build flow and reduces drift between source and generated output.
- **Alternatives considered**:
  - Editing `services.html` directly: faster once, but breaks the documented generator-first workflow.
  - Creating a separate runtime-only layout script: unnecessary complexity for a static prototype whose current card rendering is data- and stylesheet-driven.

## Decision 3: Preserve service-card usability during denser layouts

- **Decision**: Keep service-card actions, stretched-link navigation, and readable service naming as non-negotiable layout constraints while cards adapt.
- **Rationale**: The services card is not only a visual tile; it is a management surface with delete, more-actions, and optional navigation affordances. Layout adaptation is acceptable only if these controls remain accessible and visually separated from the card title.
- **Alternatives considered**:
  - Shrinking cards aggressively without content guards: risks unreadable names and blocked controls.
  - Moving actions out of the card: would change the service management interaction model and expand scope beyond this feature.

## Decision 4: Validate through generator tests plus manual browser review

- **Decision**: Use existing Python `unittest` coverage for generator behavior and pair it with manual validation of the generated pages at desktop and responsive widths.
- **Rationale**: Current automated tests assert generated HTML content, not browser geometry. This feature affects layout behavior more than rendering semantics, so manual review of the generated pages is still required even if a small generator test is added or updated.
- **Alternatives considered**:
  - Relying on automated tests alone: insufficient for visual sizing and reflow behavior.
  - Browser automation as a prerequisite: possible later, but not required to define the implementation approach for this small prototype change.
