# Quickstart: Adaptive Service Cards Validation

## Prerequisites

- Python 3 available on the command line
- Local workspace checked out at the project root
- A browser capable of opening local `.html` files

## Build Generated Pages

Run from the repository root:

```bash
python scripts/build_dashboard_shell.py
```

Expected outcome:

- The generated root `.html` pages refresh from the current `src/dashboard_shell/` sources.

## Run Automated Generator Checks

Run from the repository root:

```bash
python -m unittest discover -s tests
```

Expected outcome:

- Existing generator tests pass.
- Any added or updated generator assertions for the services page pass.

## Validate the Default Card Baseline

1. Open `integrations.html` and `services.html` side by side.
2. Measure the visible card width and height of one default environment card in `integrations.html` and one default service card in `services.html`.
3. Confirm the default service-card footprint remains within 10% of the environment-card footprint at the default desktop view.
4. Confirm that titles, delete actions, more-actions controls, and navigation remain visible on each service card.

Expected outcome:

- Service cards no longer appear materially smaller than the integrations-page card baseline at the default desktop view.

## Validate Catalog Growth

1. Load the expanded validation dataset in `tests/fixtures/services-expanded.json` used for layout testing.
2. In PowerShell, run `$env:DASHBOARD_SHELL_ENTITY_CARDS_FILE="tests/fixtures/services-expanded.json"; python scripts/build_dashboard_shell.py`.
3. Re-open `services.html`.

Expected outcome:

- Added services appear as new cards in the same grid.
- The grid reflows into additional rows instead of compressing into an unusable fixed layout.
- No cards overlap and no action controls become obscured.

## Validate Responsive Reflow

1. Open `services.html` in browser responsive mode or resize the browser window.
2. Review the layout at 1280px, 900px, and 640px viewport widths.

Expected outcome:

- The number of columns reduces as width narrows.
- Titles remain readable enough to identify the service.
- Card actions remain accessible after each reflow.

## Related Artifacts

- UI contract: `contracts/service-grid-ui-contract.md`
- Data model: `data-model.md`
