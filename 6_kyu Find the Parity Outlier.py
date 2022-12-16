def find_outlier(integers):
    k, n = 0, 0
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            k += 1
            number_k = i
        elif integers[i] % 2 != 0:
            n += 1
            number_n = i
    if k == 1:
        return integers[number_k]
    elif n == 1:
        return integers[number_n]
