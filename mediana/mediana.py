def mediana(a, b):
    i_a, f_a = 0, len(a)-1
    i_b, f_b = 0, len(b)-1
    return mediana_rec(a, b, i_a, f_a, i_b, f_b)

def mediana_rec(a, b, i_a, f_a, i_b, f_b):
    meio_a = (i_a + f_a) // 2
    meio_b = (i_b + f_b) // 2

    if a[meio_a] == b[meio_b]:
        return a[meio_a]

    if f_b - i_b == 0 and f_a - i_a == 0:
        return (a[meio_a] + b[meio_b])/2

    if f_b - i_b == 1 and f_a - i_a == 1:
        return (max(a[i_a], b[i_b]) + min(a[f_a], b[f_b]))/2

    if a[meio_a] > b[meio_b]:
        return mediana_rec(a, b, i_a, meio_a, meio_b, f_b)
    elif a[meio_a] < b[meio_b]:
        return mediana_rec(a, b, meio_a, f_a, i_b, meio_b)

# a = [9]
# b = [14]
# juntos = [9, 14]

# a = [1, 4, 7, 8, 9]
# b = [10, 11, 12, 13, 14]
# juntos = [1, 4, 7, 8, 9, 10, 11, 12, 13, 14]

#a = [1, 4, 7, 12, 15]
#b = [10, 11, 12, 13, 14]
# juntos = [1, 4, 7, 10, 11, 12, 12, 13, 14, 15]
print(mediana(a, b))

