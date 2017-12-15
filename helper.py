def swap(l, i, j):
    """
    Swap element l[i] and l[j].
    To avoid unexpected errors, use the traditional method.
    """
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp
