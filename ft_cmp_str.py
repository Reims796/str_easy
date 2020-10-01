def ft_cmp_str(str1, str2, num):
    result = ""
    for i in range(num):
        result = result + str1[i]
    result = result + str2

    for i in range(num, len(str1)):
        result = result + str1[i]
    return result
