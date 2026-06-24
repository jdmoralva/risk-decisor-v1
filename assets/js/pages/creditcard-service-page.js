import { initTreeToggleController } from '../controllers/tree-toggle-controller.js';

export function bootstrapCreditcardServicePage(options = {}) {
  return {
    treeToggleController: initTreeToggleController({
      root: options.root || document,
    }),
  };
}
