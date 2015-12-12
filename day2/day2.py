with open("input") as file: 
    sumPaper = 0
    sumRibbon = 0
    for line in file: 
        try:
            line = line[:-1]
            d = list(map(int, line.split('x')))
            sumPaper += ((2 * d[0] * d[1]) + (2 * d[1] * d[2]) + (2 * d[2] * d[1])) + min(d[0] * d[1], d[1] * d[2], d[2] * d[0])
            sumRibbon += min(d[0], d[1], d[2]) * 2 + sorted(d)[1] * 2 + (d[0] * d[1] * d[2])
        except ValueError:
            break
    print(sumPaper)
    print(sumRibbon)

