def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_three_str(str1, str2, str3):
    x = ""
    for i in range(ft_len(str1)):
        b = 0
        for d in range(ft_len(str2)):
            if str1[i+d] != str2[d]:
                b = 1
        if b == 0:
            for c in range(i):
                x = x + str1[c]

            x = x + str3

            for c in range(i+ft_len(str2), ft_len(str1)):
                x = x + str1[c]
            return x
    return -1
