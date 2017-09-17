define([
  'base/js/namespace',
  'notebook/js/notebook'
], function(
  Jupyter,
  Notebook
) {
  var self = this;

  function toggle_nbclean(env) {
    var metadata = env.notebook.metadata;
    metadata.nbclean = !metadata.nbclean;
    set_nbclean(metadata.nbclean);
    env.notebook.save_checkpoint();
  }

  function set_nbclean(nbclean_on) {
    nbclean_on = nbclean_on ? true : false;  // undefined acts as true in toggleClass
    $(self.button).toggleClass('active', nbclean_on);
  }

  function load_ipython_extension() {
    var action = {
      icon: 'fa-paint-brush',
      help: 'Toggle Cleaned Output',
      help_index: 'zz',
      handler: toggle_nbclean
    };
    var full_action_name = Jupyter.actions.register(action, 'toggle-nbclean', 'nbclean');
    var bg = Jupyter.toolbar.add_buttons_group([full_action_name])[0];
    self.button = bg.children[0];

    set_nbclean(Jupyter.notebook.metadata.nbclean);
  }

  return {
    load_ipython_extension: load_ipython_extension
  };
});
