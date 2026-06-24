SIDEBAR_ITEMS = [
    {"key": "applications", "label": "Applications", "href": "applications.html", "icon": "icon-grid"},
    {"key": "integrations", "label": "Integrations", "href": "integrations.html", "icon": "icon-branch"},
    {"key": "alerts", "label": "Alerts", "href": "alerts.html", "icon": "icon-alert"},
    {"key": "workspaces", "label": "Workspaces", "href": "workspaces.html", "icon": "icon-briefcase"},
]


def build_styles(styles: list[str]) -> str:
    return "\n".join(f'  <link rel="stylesheet" href="{href}">' for href in styles)


def build_scripts(scripts: list[str]) -> str:
    return "\n".join(f'  <script src="{src}"></script>' for src in scripts)


def build_breadcrumbs(items: list[dict]) -> str:
    parts: list[str] = []
    for index, item in enumerate(items):
        if item["type"] == "home":
            parts.append(
                f'          <a href="{item["href"]}" class="breadcrumbs__link" aria-label="Home"><svg><use href="#icon-home"></use></svg></a>'
            )
        elif item["type"] == "link":
            parts.append(f'          <a href="{item["href"]}" class="breadcrumbs__link">{item["label"]}</a>')
        else:
            parts.append(f'          <span class="breadcrumbs__current">{item["label"]}</span>')

        if index < len(items) - 1:
            parts.append('          <svg class="breadcrumbs__divider"><use href="#icon-arrow-right"></use></svg>')

    return "\n".join(parts)


def build_sidebar(active_key: str) -> str:
    rendered: list[str] = []
    for index, item in enumerate(SIDEBAR_ITEMS):
        active_class = " sidebar__action--active" if item["key"] == active_key else ""
        aria_current = ' aria-current="page"' if item["key"] == active_key else ""
        rendered.append(
            f'        <a class="sidebar__action{active_class}" href="{item["href"]}" aria-label="{item["label"]}"{aria_current}><svg><use href="#{item["icon"]}"></use></svg></a>'
        )
        if index == 1:
            rendered.append('        <span class="sidebar__divider" aria-hidden="true"></span>')
    return "\n".join(rendered)
