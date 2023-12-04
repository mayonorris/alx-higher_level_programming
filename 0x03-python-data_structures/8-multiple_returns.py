#!/usr/bin/python3
def multiple_returns(sentence):
     l = len(sentence)
    if sentence == '':
        return(l, None)
    first_char = sentence[0]
    return (l, first_char)
