import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "src" / "dashboard_shell"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path):
    return json.loads(read_text(path))


def load_build_context() -> dict:
    return {
        "root": ROOT,
        "template": read_text(SOURCE / "template.html"),
        "icon_sprite": read_text(SOURCE / "icon-sprite.html"),
        "pages": read_json(SOURCE / "pages.json"),
        "entity_cards": read_json(SOURCE / "entity-cards.json"),
        "tree_menus": read_json(SOURCE / "tree-menus.json"),
        "header_addons": read_json(SOURCE / "header-addons.json"),
    }


def read_partial(name: str) -> str:
    if not name:
        return ""
    return read_text(SOURCE / "partials" / name)


def render_partial(name: str, context: dict) -> str:
    partial = read_text(SOURCE / "partials" / name)
    for key, value in context.items():
        partial = partial.replace("{{" + key + "}}", value)
    return partial.rstrip("\n")
