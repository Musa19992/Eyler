lst = [1, 2, 5, 10, 20, 50, 100, 200]
lst2 = []
for a in range(0, 201):
    if (a > 198):
        t = a * lst[0]
        lst2.append(t)
    if (a < 199):
        for b in range(0, 101):
            if (a > 195 or b > 97):
                t = a * lst[0] + b * lst[1]
                lst2.append(t)
            if (a < 196 or b < 98):
                for c in range(0, 41):
                    if (a > 195 or b > 97 or c > 39):
                        t = a * lst[0] + b * lst[1] + c * lst[2]
                        lst2.append(t)
                    else:
                        for d in range(0, 21):
                            if (a > 190 or b > 95 or c > 38 or d > 19):
                                t = a * lst[0] + b * lst[1] + c * lst[2] + d * lst[3]
                                lst2.append(t)
                            else:
                                for e in range(0, 11):
                                    if (a > 180 or b > 90 or c > 36 or d > 18 or e > 9):
                                        t = a * lst[0] + b * lst[1] + c * lst[2] + d * lst[3] + e * lst[4]
                                        lst2.append(t)
                                    else:
                                        for f in range(0, 5):
                                            if (a > 150 or b > 75 or c > 30 or d > 15 or e > 7 or f > 3):
                                                t = t = a * lst[0] + b * lst[1] + c * lst[2] + d * lst[3] + e * lst[
                                                    4] + f * lst[5]
                                                lst2.append(t)
                                            else:
                                                for g in range(0, 3):
                                                    if (a > 100 or b > 50 or c > 20 or d > 10 or e > 5 or f > 2 or g > 1):
                                                        t = a * lst[0] + b * lst[1] + c * lst[2] + d * lst[3] + e * lst[
                                                            4] + f * lst[5] + g * \
                                                            lst[6]
                                                        lst2.append(t)
                                                    else:
                                                        for h in range(0, 2):
                                                            if (a > 0 or b > 0 or c > 0 or d > 0 or e > 0 or f > 0 or g > 0):
                                                                break
                                                            else:
                                                                t = h * lst[7]
                                                                lst2.append(t)
print(lst2.count(200))
