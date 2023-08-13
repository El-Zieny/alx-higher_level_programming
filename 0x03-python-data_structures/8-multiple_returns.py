#!/usr/bin/python3
def multiple_returns(s):
    if s:
        return len(s), s[0]
    else:
        return 0, None
