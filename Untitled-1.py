
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    sorted(d[key])
    return d

print(most_frequent('Jaassson'))