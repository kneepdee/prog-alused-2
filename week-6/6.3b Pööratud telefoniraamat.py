def kes_on(telefoninumber, pööratud_telefoniraamat):
    if len(pööratud_telefoniraamat) == 0:
        return None
    if pööratud_telefoniraamat[0][0] == telefoninumber:
        return pööratud_telefoniraamat[0][1]
    return kes_on(telefoninumber, pööratud_telefoniraamat[1:])


print(kes_on(54125632, [(4710209, 'Ernst'),
                        (54125632, 'Uno'), (65242506, 'Arvo')]))
print(kes_on(5412, [(4710209, 'Ernst'),
                    (54125632, 'Uno'), (65242506, 'Arvo')]))
