from os import path
from notebook.nbextensions import check_nbextension, enable_nbextension, install_nbextension
from .yamlmanager import YamlFileContentsManager

def activate(config, user=True):
    config.NotebookApp.contents_manager_class = YamlFileContentsManager
    if not check_nbextension('ipyaml', user):
        install_nbextension(path.join(path.dirname(__file__), 'nbext'), destination='ipyaml', 
                            user=user)
    enable_nbextension('notebook', 'ipyaml/main')
