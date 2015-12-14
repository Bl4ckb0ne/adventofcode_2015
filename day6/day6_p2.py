with open('input') as file:
    instructions = file.readlines()
    lights = [[0 for x in range(1000)] for x in range(1000)] 
    for line in instructions:
        line = line[:-1]
        print(line)
        line = line.split(' ')
        if len(line) == 1:
            break
        do = line[0]
        if do != 'toggle':
            do = line[1]
            start = [int(x) for x in list(line[2].split(','))]
            finish = [int(x) for x in list(line[4].split(','))]
        else:
            start = [int(x) for x in list(line[1].split(','))]
            finish = [int(x) for x in list(line[3].split(','))]

        if do == 'on':
            for i in range(start[0], finish[0] + 1):
                for j in range(start[1], finish[1] + 1):
                    lights[i][j] += 1
        elif do == 'off':
            for i in range(start[0], finish[0] + 1):
                for j in range(start[1], finish[1] + 1):
                    lights[i][j] -= 1 if lights[i][j] - 1 >= 0 else 0 
        elif do == 'toggle':
            for i in range(start[0], finish[0] + 1):
                for j in range(start[1], finish[1] + 1):
                    lights[i][j] += 2

    print(sum ( [ sum(x) for x in lights ] ))
