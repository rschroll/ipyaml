# IPYaml

IPYaml provides an alternate file format to the standard JSON format for storing Jupyter notebook files.  By taking advantage of YAML's block strings, it provides an easier-to-read representation of the notebook.  It also drops all output and much of the metadata from the notebook.  This makes it a better fit for version control systems, as long as you don't care about storing the output.

As an example, here's a simple cell stored in the *ipynb* format:
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
     "'ipyaml'"
    ]
   },
   "execution_count": 1,
   "metadata": {},
   "output_type": "execute_result"
  }
 ],
 "source": [
  "\"ipynb\".replace(\"nb\", \"aml\")"
 ]
}
```
And here's that same cell in the *ipyaml* format:
```
- cell_type: code
  source: |-
    "ipynb".replace("nb", "aml")
```

## Installation

Copy the `ipyaml` notebook somewhere on you Python path.

## Usage

This package acts as an extension for Jupyter.  It ties in at too low a level to use the server extension mechanism, so you need to load it in your config file.  Add to `~/.jupyter/jupyter_notebook_config.py` the lines
```python
c = get_config()  # This line may already be here.
from ipyaml import activate
activate(c)
```
This will modify the notebook server to recognize the *ipyaml* file format.  It will also install and load a notebook extension that adds a button to the notebook toolbar, which lets you switch between the *ipynb* and *ipyaml* formats.

Unfortunately, the notebook extension will not be deactivated simply by removing those lines from the config file.  Instead, you will need to run
```bash
jupyter nbextension disable ipyaml/main
```

### Command line tool

The `ipyamlconvert` script allows you to batch convert notebooks between the *ipynb* and *ipyaml* formats.  It determines type from file extension and will convert each notebook passed to it to the other format, writing it to the same directory with the appropriate extension.  It does not check for existing files; they may be overwritten.

## License

IPYaml is copyright 2017 Robert Schroll, released under the BSD 3-Clause license.  See the LICENSE file for details.  The source is available at https://github.com/rschroll/ipyaml.
