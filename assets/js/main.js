const cards = document.querySelectorAll('[data-card]');
const treeToggles = document.querySelectorAll('[data-tree-toggle]');

const setActiveCard = (card) => {
  cards.forEach((item) => item.classList.toggle('environment-card--selected', item === card));
};

cards.forEach((card) => {
  card.addEventListener('click', (event) => {
    if (event.target.closest('button, a')) {
      return;
    }

    setActiveCard(card);
  });

  card.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      setActiveCard(card);
    }
  });
});

treeToggles.forEach((toggle) => {
  toggle.addEventListener('click', () => {
    const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
    const controlsId = toggle.getAttribute('aria-controls');
    const controlledElement = controlsId ? document.getElementById(controlsId) : null;
    const nextExpanded = !isExpanded;

    toggle.setAttribute('aria-expanded', String(nextExpanded));

    if (controlledElement) {
      controlledElement.hidden = !nextExpanded;
    }
  });
});
