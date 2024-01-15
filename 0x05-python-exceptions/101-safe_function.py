#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
    else:
        return (res)
