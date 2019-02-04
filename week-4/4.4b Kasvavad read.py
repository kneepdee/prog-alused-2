# jarjend_ruudus = [[4, 3, 2], [-1, 0]]

# kasvavaid = 0
# for rida in jarjend_ruudus:
#     if len(rida) > 0:
#         kasvav = True
#         eelmine = rida[0]
#         for el in rida[1:]:
#             if el <= eelmine:
#                 kasvav = False
#                 break
#             eelmine = el
#         if kasvav:
#             kasvavaid += 1

# print("Kasvavaid ridu on " + str(kasvavaid))


#


jarjend_ruudus = [[4, 3, 2], [-1, 0], [1, 2, 3]]

def on_kasvav(rida):
    if len(rida) > 0:
        kasvav = 1
        eelmine = rida[0]
        for el in rida[1:]:
            if el <= eelmine:
                kasvav = 0
                break
            eelmine = el
    return kasvav


kasvavaid = 0
for rida in jarjend_ruudus:
    kasvavaid += on_kasvav(rida)

print("Kasvavaid ridu on " + str(kasvavaid))
