def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_first_end_three(str):
    if ft_len(str) > 5:
        return str[:3] + str[-3:]
    else:
        return str[0] * ft_len(str)
