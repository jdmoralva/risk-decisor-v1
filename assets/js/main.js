const cards = document.querySelectorAll('[data-card]');
const sidebarActions = document.querySelectorAll('[data-sidebar-action]');

const setActiveCard = (card) => {
  cards.forEach((item) => item.classList.toggle('environment-card--selected', item === card));
};

cards.forEach((card) => {
  card.addEventListener('click', (event) => {
    if (event.target.closest('button')) {
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

const setActiveSidebarAction = (activeAction) => {
  sidebarActions.forEach((action) => {
    const isActive = action === activeAction;

    action.classList.toggle('sidebar__action--active', isActive);
    action.setAttribute('aria-pressed', String(isActive));

    if (isActive) {
      action.setAttribute('aria-current', 'page');
      return;
    }

    action.removeAttribute('aria-current');
  });
};

sidebarActions.forEach((action) => {
  action.addEventListener('click', () => {
    setActiveSidebarAction(action);
  });
});
