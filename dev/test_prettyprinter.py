from prettyprinter import pprint
import json


if __name__ == '__main__':
    with open('../tests/input/input.json') as f:
        print(pprint(json.load(f)))
