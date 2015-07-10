from collections import namedtuple
import re

Key = namedtuple('Key', 'N exp')


def InputParser(input):
    if re.match("N=[0-9].*,(e|d)=[0-9].*", input) is not None:
        key_pairs = input.split(",")
        value_pairs = []
        for key_pair in key_pairs:
            value_pair = key_pair.split("=")
            value_pairs.append(value_pair[1])

        return Key(N=int(value_pairs[0]), exp=int(value_pairs[1]))

    elif re.match("[0-9].*,[0-9].*", input) is not None:
        key_pairs = input.split(",")
        return Key(N=int(key_pairs[0]), exp=int(key_pairs[1]))
    else:
        raise IOError
