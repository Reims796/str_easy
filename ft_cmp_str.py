def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_cmp_str(str1, str2, num):
    x = ""
    num = num - 1
    for i in range(num):
        x = x + str1[i]
    x = x + str2

    for i in range(num, ft_len(str1)):
        x = x + str1[i]
    return x
