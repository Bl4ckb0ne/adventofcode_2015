with open('input2') as file:            # DAY 2
#with open('input') as file:            # DAY 1
    instructions = file.readlines()
    var = {}
    keys = []
    # Find the assignations
    for line in instructions:
        split = line[:-1].split(' ')
        if split[1] == '->':
            try: 
                var[split[2]] = int(split[0])
                instructions.remove(line)
                keys.append(split[2])
            except ValueError:
                continue
   
    while len(instructions) != 0:
        for key in keys:
            for line in instructions:
                split = line[:-1].split(' ')
                if split[1] == '->':
                    if split[0] == key:
                        keys.append(split[2])
                        var[split[2]] = var[split[0]]
                        instructions.remove(line)
                    else:
                        continue
                
                elif split[0] == 'NOT':
                    if split[1] == key:
                        keys.append(split[3])
                        var[split[3]] = ~ var[split[1]] & 0xffff
                        instructions.remove(line)
                    else:
                        continue
                            
                elif split[1] == 'AND':
                    try:
                        split[0] = int(split[0])
                    except ValueError:
                        pass

                    if isinstance(split[0], int):
                        if split[2] in keys:
                            keys.append(split[4])
                            var[split[4]] = split[0] & var[split[2]]
                            instructions.remove(line)
                        else:
                            continue

                    else:
                        if split[0] == key and split[2] in keys or split[0] in key and split[2] == key:
                            keys.append(split[4])
                            var[split[4]] = var[split[0]] & var[split[2]]
                            instructions.remove(line)
                        else:
                            continue
                
                elif split[1] == 'OR':
                    if split[0] == key and split[2] in keys or split[0] in key and split[2] == key:
                        keys.append(split[4])
                        var[split[4]] = var[split[0]] | var[split[2]]
                        instructions.remove(line)
                    else:
                        continue
                    
                elif split[1] == 'LSHIFT':
                    if split[0] == key:
                        keys.append(split[4])
                        var[split[4]] = var[split[0]] << int(split[2])
                        instructions.remove(line)
                    else:
                        continue
        
                elif split[1] == 'RSHIFT':
                    if split[0] == key:
                        keys.append(split[4])
                        var[split[4]] = var[split[0]] >> int(split[2])
                        instructions.remove(line)
                    else:
                        continue
    
    print(var['a'])
