# Context

## Terms

### DashboardShell
Shared module that renders the dashboard chrome for every generated page: topbar, breadcrumb trail, sidebar navigation, optional header extras, and the page content slot.

### EntityCard
Shared module that renders repeated catalog cards for environment-style grids and service-style grids from data, instead of copying card markup per page.

### CardSelectionController
Page-owned module that activates one selected environment-style card at a time for card-grid screens.

### TreeToggleController
Page-owned module that owns expand and collapse behavior for the CreditCard object tree.

### TreeMenu
Generated module that renders nested object-tree options and submenus for workbench pages from tree data instead of inline tree markup.

### HeaderAddon
Generated module that renders header variations such as stage bars and services action toolbars from data instead of bespoke partial markup.

### CardGridPage
Page-type module for screens composed of a hero section and an EntityCard grid.

### ServiceListPage
Page-type module for screens composed of a HeaderAddon toolbar and a service EntityCard grid.

### WorkbenchPage
Page-type module for screens composed of a workbench layout, such as the CreditCard object tree and design canvas.

### PageSpec
Structured module interface that selects one page-type module and provides only the data needed by that page type, with a small escape hatch for a custom section when required.

### PageBootstrap
Runtime module that initializes the generated screen through a small bootstrap key interface instead of page-local global wiring.

### PageBootstrapRegistry
Runtime module that maps generated page bootstrap keys to page-owned adapters and initializes them through one ES module seam.
