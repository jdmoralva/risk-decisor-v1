def render_header_addon(name: str | None, placement: str, header_addons: dict) -> str:
    if not name:
        return ""

    addon = header_addons[name]
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
