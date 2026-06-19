# Provenir Environments Mockup

Static HTML/CSS/JS prototype that recreates the provided environments dashboard screenshot.

## Files

```text
.
├─ index.html
├─ style.css
└─ assets/
   ├─ fonts/
   ├─ icons/
   ├─ images/
   └─ js/
```

## Run

Open `index.html` directly in a browser.

## Notes

- Fonts are local under `assets/fonts/`.
- The reusable icon source sprite lives in `assets/icons/sprite.svg`.
- The page keeps an inline runtime sprite in `index.html` so icons work correctly when opened via `file://`.
- Card selection behavior is in `assets/js/main.js`.

## Extend

- Add future screenshots or exported UI assets to `assets/images/`.
- Move repeated page sections into components if you later migrate this mockup into a framework.
