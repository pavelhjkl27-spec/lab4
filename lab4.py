

def box(objects):
    size = [objects[index][0] for index in objects]
    value = [objects[index][1] for index in objects]
    sm = -205

    n = len(objects)
    A = 9

    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif size[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - size[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]

    res = V[n][A]
    a = A
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append((size[i - 1], value[i - 1]))
            res -= value[i - 1]
            a -= size[i - 1]

    sm_items = sum([i[1] for i in items_list])
    selected_stuff = set()

    for search in items_list:
        for key, value in objects.items():
            if value == search:
                selected_stuff.add(key)
    selected_stuff = sorted(selected_stuff, key=lambda x: objects[x][0], reverse=True)
    sm += sm_items * 2 + 10
    if sm > 0:
        return selected_stuff, sm
    return None


objects = {'rifle': (3, 25), 'pistol': (2, 15), 'ammo': (2, 15), 'medkit': (2, 20),
           'inhaler': (1, 5), 'knife': (1, 15), 'axe': (3, 20), 'talisman': (1, 25),
           'flask': (1, 15), 'antidot': (1, 10), 'supplies': (2, 20), 'crossbow': (2, 20)}

items = list(objects.keys())
all_combinations = []

for size in range(1, len(items) + 1):
    indices = list(range(size))

    while True:
        combo = {}
        for idx in indices:
            item = items[idx]
            combo[item] = objects[item]
        all_combinations.append(combo)

        i = size - 1
        while i >= 0 and indices[i] == len(items) - size + i:
            i -= 1

        if i < 0:
            break

        indices[i] += 1
        for j in range(i + 1, size):
            indices[j] = indices[j - 1] + 1

count = 0

for combo in all_combinations:
    result = box(combo)
    if result:
        count += 1
        print(f'Комбинация №{count}')
        matrix = [[0 for i in range(3)] for j in range(3)]

        for i in result[0][:]:
            ln = objects[i][0]
            for j, val in enumerate(matrix):
                if ln <= val.count(0):
                    for k in range(val.index(0), val.index(0) + ln):
                        matrix[j][k] = i[0]
                    result[0].remove(i)
                    break
                else:
                    continue

        matrix = [[i[j] for i in matrix] for j in range(3)]

        for i in result[0][:]:
            ln = objects[i][0]
            for j, val in enumerate(matrix):
                if ln <= val.count(0):
                    for k in range(val.index(0), val.index(0) + ln):
                        matrix[j][k] = i[0]
                    result[0].remove(i)
                    break
                else:
                    continue

        for i in matrix:
            print(i)

        print(f'Итоговое число очков выживания: {result[1]}')
        print()