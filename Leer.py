def leerNum(path):
    l = []
    with open(path, 'r') as f:
        for n in f.readlines():
            l.append(float(n))
    return l