import yaml
import nbformat


WHITELIST = ['nbformat', 'nbformat_minor', 'metadata', 'kernelspec', 'display_name',
             'language', 'name', 'cells']

class SourceCode(unicode):
    pass

class SourceDumper(yaml.SafeDumper):

    def analyze_scalar(self, scalar):
        # The default analysis doesn't allow blocks if `trailing_space`, `space_break`,
        # or `special_characters`.  The first two are common and don't actually cause
        # any problems.  We'll test for special characters ourselves and set `allow_blocks`
        # based on that.
        analysis = super(SourceDumper, self).analyze_scalar(scalar)
        special_characters = False
        for ch in scalar:
            if not (ch == u'\n' or u'\x20' <= ch <= u'\x7E'):
                if not self.allow_unicode or not (ch == u'\x85' or u'\xA0' <= ch <= u'\uD7FF'
                          or u'\uE000' <= ch <= u'\uFFFD') or ch == u'\uFEFF':
                    special_characters = True
                    break
        analysis.allow_block = not special_characters
        return analysis

def sourcecode_representer(dumper, data):
    return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')

def notebooknode_representer(dumper, data):
    if 'cell_type' in data:
        return dumper.represent_dict({
            'cell_type': data.cell_type,
            'source': SourceCode(data.source)
        })
    return dumper.represent_dict({k: v for k, v in data.iteritems() if k in WHITELIST})

SourceDumper.add_representer(nbformat.NotebookNode, notebooknode_representer)
SourceDumper.add_representer(SourceCode, sourcecode_representer)

def read(f, version=4):
    nb_struct = yaml.load(f, Loader=yaml.SafeLoader)
    nb_struct['metadata']['ipyaml'] = True
    for cell in nb_struct['cells']:
        cell['metadata'] = {}
        if cell['cell_type'] == 'code':
            cell['outputs'] = []
            cell['execution_count'] = None
    nb = nbformat.from_dict(nb_struct)
    if version is not nbformat.NO_CONVERT:
        nb = nbformat.convert(nb, version)
    nbformat.validate(nb)
    return nb

def write(nb, f=None, version=nbformat.NO_CONVERT):
    return yaml.dump(nb, f, default_flow_style=False, Dumper=SourceDumper, allow_unicode=True)


if __name__ == '__main__':

    def test_roundtrip_yaml(s, as_block=True):
        y = yaml.dump(SourceCode(s), default_flow_style=False, Dumper=SourceDumper,
                      allow_unicode=True)
        if as_block:
            assert y[0] == '|', "Not encoded as block: %r" % s
        assert s == yaml.load(y), "Did not round-trip: %r" % s

    test_roundtrip_yaml('simple string')
    test_roundtrip_yaml('string with\nnew lines')
    test_roundtrip_yaml('  leading spaces')
    test_roundtrip_yaml('  leading spaces\nand new lines')
    test_roundtrip_yaml('trailing spacings    ')
    test_roundtrip_yaml('trailing spaces   \nin multiline')
    test_roundtrip_yaml('line with only spaces\n     ')
    test_roundtrip_yaml('many trailing new lines\n\n\n')

    test_roundtrip_yaml(u'unicode \uABCD')
    test_roundtrip_yaml(u'unicode control \x80', False)
    test_roundtrip_yaml(u'unicode private \uD800', False)

    yaml_nb = """cells:
- cell_type: code
  source: |-
    1+2-3+4
- cell_type: markdown
  source: |-
    Text
- cell_type: raw
  source: |-
    Raw cell!
metadata:
  kernelspec:
    display_name: Python 2
    language: python
    name: python2
nbformat: 4
nbformat_minor: 0
"""
    assert yaml_nb == write(read(yaml_nb)), "Notebook did not round-trip"
