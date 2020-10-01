def ft_max_char_on_end(str):
    a = "0123456789"

    b = ""
    x = ""
    for i in str:
        if i in a:
            b = b + i
        else:
            if len(b) > len(x):
                x = b
                b = ""
    if len(b) > len(x):
        x = b
    return x