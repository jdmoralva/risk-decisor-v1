(function () {
  function initCardSelectionController(root) {
    var scope = root || document;
    var cards = scope.querySelectorAll('[data-card]');

    function setActiveCard(card) {
      cards.forEach(function (item) {
        item.classList.toggle('environment-card--selected', item === card);
      });
    }

    cards.forEach(function (card) {
      card.addEventListener('click', function (event) {
        if (event.target.closest('button, a')) {
          return;
        }

        setActiveCard(card);
      });

      card.addEventListener('keydown', function (event) {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          setActiveCard(card);
        }
      });
    });
  }

  window.initCardSelectionController = initCardSelectionController;
})();
