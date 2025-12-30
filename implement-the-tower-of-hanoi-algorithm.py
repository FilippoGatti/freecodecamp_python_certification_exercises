def hanoi(n, source_key, helper_key, target_key, towers, situation):
    if n > 0:
        hanoi(n-1, source_key, target_key, helper_key, towers, situation) 
        towers[target_key].append(towers[source_key].pop())
        current_state = [list(towers['A']), list(towers['B']), list(towers['C'])]
        situation.append(current_state)
        hanoi(n-1, helper_key, source_key, target_key, towers, situation)


def hanoi_solver(n):
    towers = {
        'A': [i for i in range(n, 0, -1)],
        'B': [],
        'C': []
    }
    situation = [[list(towers['A']), list(towers['B']), list(towers['C'])]]

    hanoi(n, 'A', 'B', 'C', towers, situation)

    text = []
    for el in situation:
        text.append(f'{el[0]} {el[1]} {el[2]}')
    
    return '\n'.join(text)
