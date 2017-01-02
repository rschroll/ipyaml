import os
from tornado.web import HTTPError
from notebook.services.contents.filemanager import FileContentsManager

from .yamlnbformat import read, write


class YamlFileContentsManager(FileContentsManager):

    def get(self, path, content=True, type=None, format=None):
        if type is None and path.endswith('.ipyaml'):
            path = path.strip('/')
            if self.exists(path):
                os_path = self._get_os_path(path)
                if not os.path.isdir(os_path):
                    return self._notebook_model(path, content=content)

        return super(YamlFileContentsManager, self).get(path, content, type, format)

    def _read_notebook(self, os_path, as_version=4):
        with self.open(os_path, 'r', encoding='utf-8') as f:
            c = f.read(1)
            if c != '{':
                f.seek(0)
                try:
                    return read(f, as_version)
                except Exception as e:  # All sorts of things could go wrong!
                    raise HTTPError(400, u"Unreadable YAML Notebook: %s %r" % (os_path, e))

        return super(YamlFileContentsManager, self)._read_notebook(os_path, as_version)

    def _save_notebook(self, os_path, nb):
        if nb.metadata.get('ipyaml'):
            with self.atomic_writing(os_path, encoding='utf-8') as f:
                write(nb, f)
        else:
            return super(YamlFileContentsManager, self)._save_notebook(os_path, nb)
