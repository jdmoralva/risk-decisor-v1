# UI Contract: Services Grid and Service Card Behavior

## Scope

This contract defines the expected rendered behavior for the services-page catalog and its service cards.

## Services Grid Contract

- The services page exposes one services-grid region labeled for assistive technology.
- The region renders every service entry provided by the services collection.
- The layout starts from a card footprint visually aligned with the integrations-page environment-card baseline.
- The layout adapts to additional cards by reflowing cards into the available width and subsequent rows instead of depending on a fixed maximum service count.
- The layout must not require horizontal scrolling at the default desktop view.

## Service Card Contract

- Every service card renders a visible service title.
- Every service card renders delete and more-actions controls.
- A card with a destination renders a stretched-link navigation target that does not block card-level actions.
- Card actions remain visible and interactive after grid densification and responsive reflow.
- Long service names remain identifiable and do not visually collide with the actions area.

## Source Contract

- The services-page output is generated from repo source files; generated HTML is not the editing surface.
- Service entries are defined in the `services` collection of `src/dashboard_shell/entity-cards.json`.
- The services page selects the `service-list` page type through `src/dashboard_shell/pages.json`.

## Validation References

- See `../quickstart.md` for end-to-end validation steps.
- See `../data-model.md` for the service entry fields and relationships that feed this contract.
