# Data Model: Adaptive Service Cards

## Service Card

- **Purpose**: Represents one service entry displayed in the services catalog.
- **Source**: `src/dashboard_shell/entity-cards.json` under the `services` collection.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Service name rendered as the card heading. |
| `deleteLabel` | string | Yes | Accessible label for the delete action. |
| `moreLabel` | string | Yes | Accessible label for the overflow or options action. |
| `href` | string | No | Destination for services that open a dedicated page. |
| `linkLabel` | string | Required when `href` exists | Accessible label for the stretched-link navigation target. |

### Validation Rules

- `title` must be present for every service entry because the title is the main visible identifier.
- `deleteLabel` and `moreLabel` must be present for every service entry because service cards always expose those actions.
- If `href` is present, `linkLabel` must also be present so the navigable card remains accessible.
- Long titles must still render within the card without colliding with actions.

## Services Grid

- **Purpose**: Layout container that arranges all service cards for the services page.
- **Source**: `src/dashboard_shell/partials/services-grid.html` and `style.css`.

### Fields / Derived Properties

| Property | Type | Description |
|----------|------|-------------|
| `ariaLabel` | string | Accessible label for the services-grid section. |
| `items` | collection of Service Card | Ordered service entries to render. |
| `initialCardFootprint` | derived layout rule | Starting card size aligned with the integrations-page card baseline. |
| `adaptiveColumns` | derived layout rule | Reflow behavior that determines how many cards fit per row. |

### Validation Rules

- The grid must support both small and growing card counts without overlap.
- The grid must reflow into additional rows when the available width or card count requires it.
- The grid must keep visible cards readable and actionable at supported viewport sizes.

## Service Catalog State

- **Purpose**: Represents the current service set rendered on the services page.
- **Source**: The `services` collection supplied to the `service-list` page spec.

### Relationships

- One **Service Catalog State** contains many **Service Card** items.
- One **Services Grid** renders one **Service Catalog State** on the services page.

### State Transitions

1. **Initial render**: Existing service entries are rendered into the services grid.
2. **Catalog growth**: New service entries are added to the source collection and appear as additional cards after rebuild or re-render.
3. **Adaptive reflow**: The grid recalculates placement based on available width and service count while preserving card affordances.
