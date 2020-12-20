#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        p = [x for x in sorted(a_dictionary.keys())]
        return (p[len(p) - 1])
    return None
