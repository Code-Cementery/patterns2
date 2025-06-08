import codecs
import json
import string
from collections import Counter



special = {
    'ʒ': 'z',
    'ý': 'y',
    'ẏ': 'y',
    'ſ': 's',
    'í': 'ii',
    'ó': 'oo',
    'á': 'aa',
    'ū': 'uu',
    'ł': 'l',
    '́': "'",
    '̄': '-'
}

def convert_special(data):
    for f,t in special.items():
        data = data.replace(f, t)

    return data

def convert_back(data):
    for f,t in special.items():
        data = data.replace(t, f)

    return data
