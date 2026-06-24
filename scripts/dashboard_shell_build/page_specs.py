from scripts.dashboard_shell_build.context import read_partial
from scripts.dashboard_shell_build.entity_cards import build_entity_cards
from scripts.dashboard_shell_build.header_addons import render_header_addon
from scripts.dashboard_shell_build.tree_menus import build_tree_menu


def render_hero_section(hero: dict) -> str:
    return (
        f'      <section class="content__hero" aria-label="{hero["ariaLabel"]}">\n'
        f'        <div class="hero-ribbon">\n'
        f'          <span class="hero-ribbon__edge"></span>\n'
        f'          <h1>{hero["title"]}</h1>\n'
        f'          <span class="hero-ribbon__edge"></span>\n'
        f'        </div>\n\n'
        f'        <button class="import-button" type="button">\n'
        f'          <svg><use href="#icon-plus"></use></svg>\n'
        f'          <span>{hero["actionLabel"]}</span>\n'
        f'        </button>\n'
        f'      </section>'
    )


def render_card_grid_page(spec: dict, entity_cards: dict) -> str:
    sections = [
        render_hero_section(spec["hero"]),
        (
            f'      <section class="cards-grid" aria-label="{spec["cards"]["ariaLabel"]}">\n'
            f'{build_entity_cards(spec["cards"]["entityCards"], entity_cards)}\n'
            f'      </section>'
        ),
    ]
    custom_section = read_partial(spec.get("customSectionPartial"))
    if custom_section:
        sections.append(custom_section)
    return "\n\n".join(sections)


def render_service_list_page(spec: dict, entity_cards: dict, header_addons: dict) -> str:
    sections = [
        render_header_addon(spec.get("headerAddon"), "content", header_addons),
        (
            f'      <section class="services-grid" aria-label="{spec["cards"]["ariaLabel"]}">\n'
            f'{build_entity_cards(spec["cards"]["entityCards"], entity_cards)}\n'
            f'      </section>'
        ),
    ]
    custom_section = read_partial(spec.get("customSectionPartial"))
    if custom_section:
        sections.append(custom_section)
    return "\n\n".join(sections)


def render_workbench_page(spec: dict, tree_menus: dict) -> str:
    workbench = spec["workbench"]
    sections = [
        (
            f'      <section class="service-workbench" aria-label="{workbench["ariaLabel"]}">\n'
            f'        <div class="service-canvas">\n'
            f'          <section class="service-sidebar-panel" aria-label="{workbench["treePanelAriaLabel"]}">\n'
            f'            <div class="service-sidebar-panel__header">\n'
            f'              <label class="service-search" aria-label="Search objects">\n'
            f'                <input type="text" value="" aria-label="Search">\n'
            f'                <svg><use href="#icon-search"></use></svg>\n'
            f'              </label>\n'
            f'            </div>\n\n'
            f'            <div class="service-sidebar-panel__header">\n'
            f'              <div class="service-sidebar-icons">\n'
            f'                <button class="service-sidebar-icon" type="button" aria-label="Add object"><svg><use href="#icon-plus"></use></svg></button>\n'
            f'                <button class="service-sidebar-icon" type="button" aria-label="Grid view"><svg><use href="#icon-grid"></use></svg></button>\n'
            f'                <button class="service-sidebar-icon" type="button" aria-label="Branch view"><svg><use href="#icon-branch"></use></svg></button>\n'
            f'              </div>\n'
            f'            </div>\n\n'
            f'            <div class="service-tree">\n'
            f'{build_tree_menu(workbench["treeMenu"], tree_menus)}\n'
            f'            </div>\n'
            f'          </section>\n\n'
            f'          <section class="service-main-panel" aria-label="{workbench["canvasAriaLabel"]}">\n'
            f'            <div class="service-main-panel__hint">\n'
            f'              <p>{workbench["canvasHint"]}</p>\n'
            f'            </div>\n'
            f'          </section>\n'
            f'        </div>\n'
            f'      </section>'
        )
    ]
    custom_section = read_partial(spec.get("customSectionPartial"))
    if custom_section:
        sections.append(custom_section)
    return "\n\n".join(sections)


def build_page_spec(page_spec: dict, entity_cards: dict, tree_menus: dict, header_addons: dict) -> str:
    page_type = page_spec["type"]
    if page_type == "card-grid":
        return render_card_grid_page(page_spec, entity_cards)
    if page_type == "service-list":
        return render_service_list_page(page_spec, entity_cards, header_addons)
    if page_type == "workbench":
        return render_workbench_page(page_spec, tree_menus)
    raise ValueError(f"Unknown PageSpec type: {page_type}")
