from notebook.services.contents.filemanager import FileContentsManager
import nbformat

def clean_v4_nb(old_nb):
    new_nb = nbformat.v4.new_notebook(nbformat_minor=0)

    new_nb.metadata.kernelspec = old_nb.metadata.kernelspec
    new_nb.metadata.nbclean = True

    for cell in old_nb.cells:
        cell_factory = getattr(nbformat.v4, 'new_%s_cell' % cell.cell_type)
        new_nb.cells.append(cell_factory(cell.source))

    return new_nb


class NbCleanFileContentsManager(FileContentsManager):

    def _save_notebook(self, os_path, nb):
        if nb.metadata.get('nbclean'):
            nb_v4 = nbformat.convert(nb, 4)
            nb_clean = clean_v4_nb(nb_v4)
            with self.atomic_writing(os_path, encoding='utf-8') as f:
                nbformat.write(nb_clean, f)
        else:
            return super(NbCleanFileContentsManager, self)._save_notebook(os_path, nb)
