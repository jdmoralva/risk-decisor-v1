(function () {
  function initTreeToggleController(root) {
    var scope = root || document;
    var treeToggles = scope.querySelectorAll('[data-tree-toggle]');

    treeToggles.forEach(function (toggle) {
      toggle.addEventListener('click', function () {
        var isExpanded = toggle.getAttribute('aria-expanded') === 'true';
        var controlsId = toggle.getAttribute('aria-controls');
        var controlledElement = controlsId ? document.getElementById(controlsId) : null;
        var nextExpanded = !isExpanded;

        toggle.setAttribute('aria-expanded', String(nextExpanded));

        if (controlledElement) {
          controlledElement.hidden = !nextExpanded;
        }
      });
    });
  }

  window.initTreeToggleController = initTreeToggleController;
})();
