# def kuup(jarj):
#     kuup_jarj = []
#     for el in jarj:
#         kuup_jarj.append(el ** 3)
#     return kuup_jarj


def kuup(järjend, tulemus=[]):
    if len(järjend) > 0:
        return kuup(järjend[1:], [järjend[0] ** 3] + tulemus)[::-1]
    return tulemus


print(kuup([1, 2, 3, 4, 5]))
