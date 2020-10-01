def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_slice_str(str, start, end):
    x = ""
    for i in range(start, end+1):
        if i >= ft_len(str):
            break
        x = x + str[i]
    return x
