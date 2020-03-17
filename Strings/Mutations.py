def mutate_string(string, position, character):
    l = list(string)
    l[position]=character
    res = ''.join(l)
    return res

