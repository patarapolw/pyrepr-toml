import json

from pyrepr import Repr

if __name__ == '__main__':
    with open('input/input.json') as f_in, open('output/output.toml.repr', 'w') as f_out:
        f_out.write(str(Repr(json.load(f_in))))  # default str representation is TOML-like
