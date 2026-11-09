def base_command(point: list):
    x, y, direction, command = point
    #
    directions = ['N', 'E', 'S', 'W']
    ind = directions.index(direction)

    # коэфицент и координаты относительно направления
    if direction == 'N':
        coordinats = [x, y]
        k = [1, 1]
    elif direction == 'S':
        coordinats = [x, y]
        k = [-1, -1]
    elif direction == 'E':
        coordinats = [y, x]
        k = [-1, 1]
    elif direction == 'W':
        coordinats = [y, x]
        k = [1, -1]

    # команды
    if command == 'F':
        coordinats[1] += k[1]
    elif command == 'B':
        coordinats[1] -= k[1]
    elif command == 'R':
        coordinats[0] += k[0]
    elif command == 'L':
        coordinats[0] -= k[0]
    elif command == ')':
        if ind == 3:
            direction = 'N'
        else:
            direction = directions[ind + 1]
    elif command == '(':
        if ind == 0:
            direction = 'W'
        else:
            direction = directions[ind - 1]

    x, y = coordinats

    return [x, y, direction, command]


commands = input()

point = [0, 0, 'N', '']
for c in commands:
    point[3] = c
    point = base_command(point)

print(point[0], point[1])
