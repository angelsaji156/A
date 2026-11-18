
def waterjug(a, b, target, limit):
    def dls(x, y, depth, path):
        if x == target or y == target:
            return path

        if depth == limit:
            return None

        moves = [
            (a, y),       # Fill jug 1
            (x, b),       # Fill jug 2
            (0, y),       # Empty jug 1
            (x, 0),       # Empty jug 2
            (x - min(x, b-y), y + min(x, b-y)),  # Pour 1 to 2
            (x + min(y, a-x), y - min(y, a-x))   # Pour 2 to 1
        ]

        for state in moves:
            if state not in path:
                result = dls(state[0], state[1],
                             depth + 1, path + [state])
                if result:
                    return result

        return None

    return dls(0, 0, 0, [(0, 0)])


a = int(input("Enter capacity of jug 1: "))
b = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))
limit = int(input("Enter depth limit: "))

result = waterjug(a, b, target, limit)

if result:
    print("Solution path:")
    for state in result:
        print(state)
else:
    print("Solution not found within depth limit")
