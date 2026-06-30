def list_to_word(towers, word):
    for i in towers:
       word += f'{i} '
    
    word = word.strip()
    word += '\n'
    return word

def hanoi_tower(disks, source, destination, auxiliary, towers, word):
    if disks == 1:
        word = list_to_word(towers, word)
        towers[destination].append(towers[source].pop())
        word = list_to_word(towers, word)
        return word
        

    word = hanoi_tower(disks - 1, source, auxiliary, destination, towers, word)
    
    
    towers[destination].append(towers[source].pop())
    
    
    word = hanoi_tower(disks - 1, auxiliary, destination, source, towers, word)
    
    
    return word

def hanoi_solver(disks: int):
    towers = [[], [], []]
    for i in range(disks, 0, -1):
        towers[0].append(i)
    
    word = ''
    word = hanoi_tower(disks, 0, 2, 1, towers, word)
    word = word.strip('\n')
    return word




