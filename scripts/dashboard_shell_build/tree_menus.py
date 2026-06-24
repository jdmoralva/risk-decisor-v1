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
    second_node = icon_markup if item.get("icon") else box_markup

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


def build_tree_menu(name: str | None, tree_menus: dict) -> str:
    if not name:
        return ""
    menu = tree_menus[name]
    rendered_items = "\n".join(render_tree_option(item) for item in menu["items"])
    return (
        f'              <ul class="service-tree__group" aria-label="{menu["ariaLabel"]}">\n'
        f'{rendered_items}\n'
        f'              </ul>'
    )
