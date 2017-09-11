# NbClean

NbClean cleans all of the output cruft from your Jupyter notebooks, leaving you with the bare minimum needed to run the notebook code again.  This will reduce the noise in your version control system from diffs that don't reflect changes that you made.

As an example, here's a simple cell stored in the v4 format:
```
{
 "cell_type": "code",
 "execution_count": 1,
 "metadata": {
  "collapsed": false
 },
 "outputs": [
  {
   "data": {
    "text/plain": [
     "3"
    ]
   },
   "execution_count": 1,
   "metadata": {},
   "output_type": "execute_result"
  }
  "1 + 2"
 ]
}
```
And here's that same cell after we've cleaned it:
```
{
 "cell_type": "code",
 "execution_count": null,
 "metadata": {},
 "outputs": [],
 "source": [
  "1 + 2"
 ]
}
```

## Installation

IPYaml can be installed with pip:
```
pip install git+https://github.com/rschroll/ipyaml.git@nbclean
```

## Usage

This package acts as an extension for Jupyter.  It ties in at too low a level to use the server extension mechanism, so you need to load it in your config file.  Add to `~/.jupyter/jupyter_notebook_config.py` the lines
```python
c = get_config()  # This line may already be here.
from nbclean import activate
activate(c)
```
This will modify the notebook server to be able to clean notebooks when they are saved.  It will also install and load a notebook extension that adds a button to the notebook toolbar, which lets indicate whether this cleaning should take place.  By default, it is off, so you'll have to enable it for each notebook you wish to be automatically cleaned.

Unfortunately, the notebook extension will not be deactivated simply by removing those lines from the config file.  Instead, you will need to run
```bash
jupyter nbextension disable nbconvert/main
```

### Command line tool

The `cleanipynb` script allows you to batch clean notebooks.  It will overwrite all files with cleaned version.

### Metadata

NbClean adds notebook metadata key, `nbclean`, as a flag to indicate whether cleaning should happen on save.  This is turned on by the `cleanipynb` script.  This should be preserved by other Jupyter instances without NbClean.  It will not make them do the cleaning for you, unfortunately.

## License

NbClean is copyright 2017 Robert Schroll, released under the BSD 3-Clause license.  See the LICENSE file for details.  The source is available at https://github.com/rschroll/ipyaml/tree/nbclean.
