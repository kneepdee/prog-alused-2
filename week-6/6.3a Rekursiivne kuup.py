# def kuup(jarj):
#     kuup_jarj = []
#     for el in jarj:
#         kuup_jarj.append(el ** 3)
#     return kuup_jarj


# def summa_sabarekursioon_lõige(järjend, tulemus=0):
#     if len(järjend) > 0:
#         return summa_sabarekursioon_lõige(järjend[1:], järjend[0] + tulemus)
#     return tulemus

def kuup(jarj):
    if len(jarj) == 0:
        return jarj
    return [jarj[0] ** 3] + kuup(jarj[1:])


print(kuup([1, 2, 3]))
# print(summa_sabarekursioon_lõige([1, 2, 3]))
