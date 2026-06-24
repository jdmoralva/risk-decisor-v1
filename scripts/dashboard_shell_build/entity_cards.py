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


def build_entity_cards(spec: dict | None, entity_cards: dict) -> str:
    if not spec:
        return ""

    items = entity_cards[spec["collection"]]
    if spec["variant"] == "environment":
        return "\n".join(render_environment_entity_card(item) for item in items)
    if spec["variant"] == "service":
        return "\n".join(render_service_entity_card(item) for item in items)
    raise ValueError(f'Unknown EntityCard variant: {spec["variant"]}')
