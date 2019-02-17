def on_rahulik(arvamus1, arvamus2, lubatud_erinevus):
    if arvamus1 * arvamus2 >= 0 or (abs(arvamus1 - arvamus2) <= lubatud_erinevus):
        # if (arvamus1 > 0 and arvamus2 > 0) or (arvamus1 < 0 and arvamus2 < 0) or (arvamus1 == 0) or (arvamus2 == 0) or (abs(arvamus1 - arvamus2) <= lubatud_erinevus):
        return True
    return False


def dissonantside_arv(arvamused, lubatud_erinevus):
    dissonantsid = 0

    for i in range(len(arvamused) - 1):
        if not on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus):
            dissonantsid += 1

    return dissonantsid


print(dissonantside_arv([1, 4], 2))
# 0

print(dissonantside_arv([-1, 3], 4))
# 0

print(dissonantside_arv([-1, 3], 3))
# 1

print(dissonantside_arv([0, 3], 1))
# 0

print(dissonantside_arv([1, 4, 0, -10, -1, 3, 42], 2))
# 1

print(dissonantside_arv([1, -3, 1, 0, 0, -2, -3, 3, -3, 12], 3))
# 5
