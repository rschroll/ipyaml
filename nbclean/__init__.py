from os import path
from notebook.nbextensions import check_nbextension, enable_nbextension, install_nbextension
from .nbcleanmanager import NbCleanFileContentsManager, clean_v4_nb

def activate(config, user=True):
    config.NotebookApp.contents_manager_class = NbCleanFileContentsManager
    if not check_nbextension('nbclean', user):
        install_nbextension(path.join(path.dirname(__file__), 'nbext'), destination='nbclean',
                            user=user)
    enable_nbextension('notebook', 'nbclean/main')
