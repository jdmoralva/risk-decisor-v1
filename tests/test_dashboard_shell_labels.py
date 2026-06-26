import unittest

from scripts.build_dashboard_shell import render_page


class DashboardShellLabelTests(unittest.TestCase):
    def test_render_page_uses_configured_sidebar_labels(self):
        page = {
            "title": "Test Page",
            "bodyClass": "",
            "styles": ["style.css"],
            "bootstrapKey": None,
            "activeNav": "integrations",
            "breadcrumbs": [{"type": "current", "label": "Current"}],
            "pageSpec": {
                "type": "card-grid",
                "hero": {
                    "ariaLabel": "Page title and actions",
                    "title": "TITLE",
                    "actionLabel": "Action",
                },
                "cards": {
                    "ariaLabel": "Cards",
                    "entityCards": {"variant": "environment", "collection": "environments"},
                },
            },
        }
        build_context = {
            "template": "{{STYLE_LINKS}}{{BREADCRUMBS}}{{SIDEBAR_ITEMS}}{{HEADER_ROW_ADDON}}{{MAIN_CONTENT}}{{RUNTIME_SCRIPT}}",
            "icon_sprite": "",
            "entity_cards": {"environments": []},
            "tree_menus": {},
            "header_addons": {},
            "shell_config": {
                "sidebarItems": [
                    {"key": "applications", "label": "Apps", "href": "applications.html", "icon": "icon-grid"},
                    {"key": "integrations", "label": "Imported", "href": "integrations.html", "icon": "icon-branch"},
                ]
            },
        }

        html = render_page(page, build_context)

        self.assertIn('aria-label="Imported"', html)

    def test_render_page_uses_workbench_labels_from_page_spec(self):
        page = {
            "title": "Workbench",
            "bodyClass": "creditcard-page",
            "styles": ["style.css"],
            "bootstrapKey": None,
            "activeNav": "integrations",
            "breadcrumbs": [{"type": "current", "label": "Current"}],
            "pageSpec": {
                "type": "workbench",
                "workbench": {
                    "ariaLabel": "Workbench",
                    "treePanelAriaLabel": "Tree panel",
                    "canvasAriaLabel": "Canvas",
                    "treeMenu": "creditcardObjects",
                    "canvasHint": "Hint",
                    "searchRegionAriaLabel": "Find objects",
                    "searchInputAriaLabel": "Find",
                    "addObjectAriaLabel": "Create object",
                    "gridViewAriaLabel": "Tile view",
                    "branchViewAriaLabel": "Flow view",
                },
            },
        }
        build_context = {
            "template": "{{STYLE_LINKS}}{{BREADCRUMBS}}{{SIDEBAR_ITEMS}}{{HEADER_ROW_ADDON}}{{MAIN_CONTENT}}{{RUNTIME_SCRIPT}}",
            "icon_sprite": "",
            "entity_cards": {},
            "tree_menus": {"creditcardObjects": {"ariaLabel": "Objects", "items": []}},
            "header_addons": {},
            "shell_config": {"sidebarItems": []},
        }

        html = render_page(page, build_context)

        self.assertIn('aria-label="Find objects"', html)
        self.assertIn('aria-label="Find"', html)
        self.assertIn('aria-label="Create object"', html)
        self.assertIn('aria-label="Tile view"', html)
        self.assertIn('aria-label="Flow view"', html)


if __name__ == "__main__":
    unittest.main()
