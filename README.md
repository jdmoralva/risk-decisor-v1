# Provenir Dashboard Mockup

Static HTML/CSS/JS prototype that recreates the provided dashboard style and packages it as a small multi-page sidebar navigation demo.

## Files

```text
.
├─ applications.html
├─ integrations.html
├─ alerts.html
├─ workspaces.html
├─ index.html
├─ style.css
└─ assets/
   ├─ fonts/
   ├─ icons/
   ├─ images/
   └─ js/
```

## Run

Open `index.html` directly in a browser. The sidebar links navigate to the other static HTML pages.

## Notes

- Fonts are local under `assets/fonts/`.
- The reusable icon source sprite lives in `assets/icons/sprite.svg`.
- Each page keeps an inline runtime sprite so icons work correctly when opened via `file://`.
- Card selection behavior is in `assets/js/main.js`.

## Extend

- Add future screenshots or exported UI assets to `assets/images/`.
- Move repeated page sections into components if you later migrate this mockup into a framework.
