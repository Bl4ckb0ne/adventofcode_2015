with open("input") as file:
    floor = 0
    count = 1
    while True:
        char = file.read(1)
        if not char:
            break
        elif char == "(":
            floor = floor + 1
        elif char == ")":
            floor = floor - 1

        if floor == -1:
            print(count)

        count += 1

    print(floor) 
