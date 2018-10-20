import json

from pyrepr import Repr

if __name__ == '__main__':
    with open('input/input.json') as f_in, open('output/output.md', 'w') as f_out:
        f_out.write(Repr(json.load(f_in)).to_str('markdown'))
