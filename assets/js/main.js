const cards = document.querySelectorAll('[data-card]');

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
