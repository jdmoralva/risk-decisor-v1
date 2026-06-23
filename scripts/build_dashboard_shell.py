import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "src" / "dashboard_shell"
TEMPLATE = (SOURCE / "template.html").read_text(encoding="utf-8")
ICON_SPRITE = (SOURCE / "icon-sprite.html").read_text(encoding="utf-8")
PAGES = json.loads((SOURCE / "pages.json").read_text(encoding="utf-8"))
ENTITY_CARDS = json.loads((SOURCE / "entity-cards.json").read_text(encoding="utf-8"))
TREE_MENUS = json.loads((SOURCE / "tree-menus.json").read_text(encoding="utf-8"))
HEADER_ADDONS = json.loads((SOURCE / "header-addons.json").read_text(encoding="utf-8"))

SIDEBAR_ITEMS = [
    {"key": "applications", "label": "Applications", "href": "applications.html", "icon": "icon-grid"},
    {"key": "integrations", "label": "Integrations", "href": "integrations.html", "icon": "icon-branch"},
    {"key": "alerts", "label": "Alerts", "href": "alerts.html", "icon": "icon-alert"},
    {"key": "workspaces", "label": "Workspaces", "href": "workspaces.html", "icon": "icon-briefcase"},
]


def read_partial(name: str) -> str:
    if not name:
        return ""
    return (SOURCE / "partials" / name).read_text(encoding="utf-8")


def render_header_addon(name: str | None, placement: str) -> str:
    if not name:
        return ""

    addon = HEADER_ADDONS[name]
    if addon["placement"] != placement:
        return ""

    if addon["variant"] == "stagebar":
        items = "\n".join(
            f'          <span class="service-stagebar__item{" service-stagebar__item--active" if item.get("active") else ""}">{item["label"]}</span>'
            for item in addon["items"]
        )
        return (
            f'        <div class="service-stagebar" aria-label="{addon["ariaLabel"]}">\n'
            f'{items}\n'
            f'        </div>'
        )

    if addon["variant"] == "services-toolbar":
        tools = "\n".join(
            f'          <button class="services-tool" type="button" aria-label="{tool["label"]}"><svg><use href="#{tool["icon"]}"></use></svg></button>'
            for tool in addon["tools"]
        )
        action_dot = '<span class="services-add-dot" aria-hidden="true"></span>' if addon["action"].get("dot") else ""
        return (
            f'      <section class="services-toolbar" aria-label="{addon["ariaLabel"]}">\n'
            f'        <div class="services-tools">\n{tools}\n        </div>\n'
            f'        <div class="hero-ribbon"><span class="hero-ribbon__edge"></span><h1>{addon["title"]}</h1><span class="hero-ribbon__edge"></span></div>\n'
            f'        <button class="services-add-button" type="button">{action_dot}<span>{addon["action"]["label"]}</span></button>\n'
            f'      </section>'
        )

    raise ValueError(f'Unknown HeaderAddon variant: {addon["variant"]}')


def render_environment_entity_card(item: dict) -> str:
    classes = ["environment-card"]
    if item.get("selected"):
        classes.append("environment-card--selected")
    if item.get("href"):
        classes.append("environment-card--navigable")

    stretched_link = ""
    if item.get("href"):
        stretched_link = (
            f'          <a class="environment-card__stretched-link" href="{item["href"]}" aria-label="{item["linkLabel"]}"></a>\n'
        )

    meta_buttons = "\n".join(
        f'            <button class="meta-icon" type="button" aria-label="{meta["label"]}"><svg><use href="#{meta["icon"]}"></use></svg></button>'
        for meta in item["meta"]
    )

    return (
        f'        <article class="{" ".join(classes)}" tabindex="0" data-card>\n'
        f'{stretched_link}'
        f'          <button class="environment-card__menu" type="button" aria-label="{item["menuLabel"]}"><svg><use href="#icon-ellipsis"></use></svg></button>\n'
        f'          <div class="environment-card__badge" aria-hidden="true"><svg><use href="#{item["badgeIcon"]}"></use></svg></div>\n'
        f'          <h2>{item["title"]}</h2>\n'
        f'          <div class="environment-card__rule"></div>\n'
        f'          <div class="environment-card__meta" aria-label="{item["metaAria"]}">\n'
        f'{meta_buttons}\n'
        f'          </div>\n'
        f'        </article>'
    )


def render_service_entity_card(item: dict) -> str:
    classes = ["service-card"]
    if item.get("href"):
        classes.append("service-card--navigable")

    stretched_link = ""
    if item.get("href"):
        stretched_link = (
            f'          <a class="service-card__stretched-link" href="{item["href"]}" aria-label="{item["linkLabel"]}"></a>\n'
        )

    return (
        f'        <article class="{" ".join(classes)}">\n'
        f'{stretched_link}'
        f'          <span class="service-card__pin" aria-hidden="true"></span>\n'
        f'          <div class="service-card__actions"><button class="service-card__action" type="button" aria-label="{item["deleteLabel"]}"><svg><use href="#icon-trash"></use></svg></button><button class="service-card__action" type="button" aria-label="{item["moreLabel"]}"><svg><use href="#icon-ellipsis"></use></svg></button></div>\n'
        f'          <div class="service-card__icon"><svg><use href="#icon-cube"></use></svg></div><h2>{item["title"]}</h2>\n'
        f'        </article>'
    )


def render_tree_option(item: dict) -> str:
    classes = ["service-tree__option"]
    if item.get("kind") == "top":
        classes.append("service-tree__option--top")
    if item.get("kind") == "submenu":
        classes.append("service-tree__option--submenu")
    if item.get("selected"):
        classes.append("service-tree__option--selected")

    toggle = item.get("toggle")
    toggle_attrs = ""
    if toggle:
        toggle_attrs = (
            f' aria-expanded="{"true" if toggle["expanded"] else "false"}"'
            f' aria-controls="{toggle["controls"]}" data-tree-toggle'
        )

    caret_classes = "service-tree__caret"
    if toggle:
        caret_classes += " service-tree__caret--down"

    icon_markup = ""
    if item.get("icon"):
        icon_markup = f'<svg class="service-tree__node-icon"><use href="#{item["icon"]}"></use></svg>'

    box_classes = "service-tree__box"
    if item.get("checked"):
        box_classes += " service-tree__box--checked"
    box_markup = f'<span class="{box_classes}"></span>'

    if item.get("icon"):
        second_node = icon_markup
    else:
        second_node = box_markup

    more_markup = ""
    if item.get("more"):
        more_markup = '<span class="service-tree__more" aria-hidden="true"><svg><use href="#icon-ellipsis"></use></svg></span>'

    option_html = (
        f'                  <button class="{" ".join(classes)}" type="button"{toggle_attrs}>'
        f'<span class="{caret_classes}" aria-hidden="true"></span>'
        f'{second_node}'
        f'<span class="service-tree__label">{item["label"]}</span>'
        f'{more_markup}'
        f'</button>'
    )

    if not item.get("children"):
        return f'                <li>{option_html}</li>'

    submenu = render_tree_children(item["children"], toggle["controls"], toggle["label"], toggle["expanded"])
    return f'                <li>\n{option_html}\n{submenu}\n                </li>'


def render_tree_children(items: list[dict], submenu_id: str, submenu_label: str, expanded: bool) -> str:
    hidden_attr = "" if expanded else " hidden"
    rendered_items = "\n".join(render_tree_option(item) for item in items)
    return (
        f'                  <ul class="service-tree__children" id="{submenu_id}" aria-label="{submenu_label}"{hidden_attr}>\n'
        f'{rendered_items}\n'
        f'                  </ul>'
    )


def build_tree_menu(name: str | None) -> str:
    if not name:
        return ""
    menu = TREE_MENUS[name]
    rendered_items = "\n".join(render_tree_option(item) for item in menu["items"])
    return (
        f'              <ul class="service-tree__group" aria-label="{menu["ariaLabel"]}">\n'
        f'{rendered_items}\n'
        f'              </ul>'
    )


def build_entity_cards(spec: dict | None) -> str:
    if not spec:
        return ""

    items = ENTITY_CARDS[spec["collection"]]
    if spec["variant"] == "environment":
        return "\n".join(render_environment_entity_card(item) for item in items)
    if spec["variant"] == "service":
        return "\n".join(render_service_entity_card(item) for item in items)
    raise ValueError(f'Unknown EntityCard variant: {spec["variant"]}')


def build_main_content(page: dict) -> str:
    content = read_partial(page["mainPartial"])
    content = content.replace("{{ENTITY_CARDS}}", build_entity_cards(page.get("entityCards")))
    content = content.replace("{{TREE_MENU}}", build_tree_menu(page.get("treeMenu")))
    return content.replace("{{HEADER_ADDON}}", render_header_addon(page.get("headerAddon"), "content"))


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


for page in PAGES:
    html = TEMPLATE
    html = html.replace("{{TITLE}}", page["title"])
    html = html.replace("{{BODY_CLASS_ATTR}}", f' class="{page["bodyClass"]}"' if page["bodyClass"] else "")
    html = html.replace("{{STYLE_LINKS}}", build_styles(page["styles"]))
    html = html.replace("{{SCRIPT_TAGS}}", build_scripts(page["scripts"]))
    html = html.replace("{{ICON_SPRITE}}", ICON_SPRITE)
    html = html.replace("{{BREADCRUMBS}}", build_breadcrumbs(page["breadcrumbs"]))
    html = html.replace("{{HEADER_ROW_ADDON}}", render_header_addon(page.get("headerAddon"), "breadcrumb"))
    html = html.replace("{{SIDEBAR_ITEMS}}", build_sidebar(page["activeNav"]))
    html = html.replace("{{MAIN_CONTENT}}", build_main_content(page))
    output_path = ROOT / page["output"]
    output_path.write_text(html + "\n", encoding="utf-8")

print(f"Generated {len(PAGES)} pages to {ROOT}")
