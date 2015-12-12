import collections

with open("input") as file:
    instructions = file.readline()
    
    santa = collections.defaultdict(int)
    robo = collections.defaultdict(int)

    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0

    santa[(santa_x, santa_y)] += 1
    robo[(robo_x, robo_y)] += 1
    
    who = True
    for c in instructions:
        
        if(who):
            if c == '^':
                santa_y += 1
                santa[(santa_x, santa_y)] += 1
            elif c == 'v':
                santa_y -= 1
                santa[(santa_x, santa_y)] += 1
            elif c == '<':
                santa_x -= 1
                santa[(santa_x, santa_y)] += 1
            elif c == '>':
                santa_x += 1
                santa[(santa_x, santa_y)] += 1
            else:
                continue
            who = False
        else:
            if c == '^':
                robo_y += 1
                robo[(robo_x, robo_y)] += 1
            elif c == 'v':
                robo_y -= 1
                robo[(robo_x, robo_y)] += 1
            elif c == '<':
                robo_x -= 1
                robo[(robo_x, robo_y)] += 1
            elif c == '>':
                robo_x += 1
                robo[(robo_x, robo_y)] += 1
            else:
                continue
            who = True

    sumHouse = santa.copy()
    sumHouse.update(robo)

    print(len(sumHouse.keys()))
