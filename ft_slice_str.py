def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_slice_str(str, start, end):
    b = ft_len(str)
    c = ""
    if end > b:
        for i in range(1, b):
            c += str[i]
    else:
        for i in range(start - 1, end):
            c += str[i]
    return c
