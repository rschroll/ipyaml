define([
  'base/js/namespace',
  'notebook/js/notebook'
], function(
  Jupyter,
  Notebook
) {
  var self = this;

  function toggle_yaml(env) {
    var metadata = env.notebook.metadata;
    metadata.ipyaml = !metadata.ipyaml;
    set_yaml(metadata.ipyaml);
    rename_notebook(env.notebook);
  }

  function set_yaml(yaml_on) {
    yaml_on = yaml_on ? true : false;  // undefined acts as true in toggleClass
    $(self.button).toggleClass('active', yaml_on);
  }

  function rename_notebook(notebook) {
    var ext = notebook.metadata.ipyaml ? ".ipyaml" : ".ipynb";
    var new_name = notebook.get_notebook_name() + ext;
    // ensure_extension will keep the file extension from changing, but we
    // want it to change.  So neuter it during the call to rename.
    var old_ensure_extension = Notebook.Notebook.prototype.ensure_extension;
    Notebook.Notebook.prototype.ensure_extension = function (name) { return name; };
    notebook.rename(new_name).then(function () {
      notebook.save_checkpoint();
    });
    Notebook.Notebook.prototype.ensure_extension = old_ensure_extension;
  }

  function load_ipython_extension() {
    var action = {
      help: 'Toggle YAML Output',
      help_index: 'zz',
      handler: toggle_yaml
    };
    var full_action_name = Jupyter.actions.register(action, 'toggle-yaml', 'ipyaml');
    var bg = Jupyter.toolbar.add_buttons_group([full_action_name])[0];
    self.button = bg.children[0];
    self.button.innerHTML = "IPYAML";

    set_yaml(Jupyter.notebook.metadata.ipyaml);
  }

  return {
    load_ipython_extension: load_ipython_extension
  };
});
