tri = [ 
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]
lst = []
for a in range(len(tri[0])):
    for b in range(a, a + 2):
        for c in range(b, b + 2):
            for d in range(c, c + 2):
                for e in range(d, d + 2):
                    for f in range(e, e + 2):
                        for g in range(f, f + 2):
                            for h in range(g, g + 2):
                                for k in range(h, h + 2):
                                    for aa in range(k, k + 2):
                                        for bb in range(aa, aa + 2):
                                            for cc in range(bb, bb + 2):
                                                for dd in range(cc, cc + 2):
                                                    for ee in range(dd, dd + 2):
                                                        for ff in range(ee, ee + 2):
                                                            summa = tri[0][a] + tri[1][b] + tri[2][c] + tri[3][d] + \
                                                                    tri[4][e] + tri[5][f] + tri[6][g] + tri[7][h] + \
                                                                    tri[8][k] + tri[9][aa] + tri[10][bb] + tri[11][cc] + \
                                                                    tri[12][dd] + tri[13][ee] + tri[14][ff]
                                                            lst.append(summa)
print(max(lst))
