def return_names(names: list, number: int):
    for i in range(0, len(names)):
        for j in range(0, len(names) - i - 1):
            if (names[j][1] > names[j + 1][1]):
                temporary = names[j]
                names[j] = names[j + 1]
                names[j + 1] = temporary
    return names[:number]

listas = [
    ['Jonas', 178],
    ['Petras', 201],
    ['Maryte', 168],
    ['Gediminas', 178],
    ['Vytautas', 183],
]


print(return_names(listas, 3))
# listas.sort()
# print(listas)
# a = sorted(listas)
# print(a)

#labas
lalala

# ED
# 12