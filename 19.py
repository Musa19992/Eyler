DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
y = 1
count = 0
for i in range(1901, 2001):
    for g in range(1, 13):
        if (g == 2) and (i%4 == 0):
            k_dney = 29
        elif(g == 2):
            k_dney = 28
        elif (g == 8) or (g == 10) or (g == 12):
            k_dney = 31
        elif (g == 9) or (g == 11):
            k_dney = 30
        elif (g%2 != 0):
            k_dney = 31
        else:
            k_dney = 30
        for t in range(k_dney):
            if (t == 0) and DAYS[y] == "SUN":
                count += 1
            y += 1
            if y == 7:
                y = 0
print(count)

