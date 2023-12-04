#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return (None)
    l = len(sentence)
    first_char = sentence[0]
    return (l, first_char)
