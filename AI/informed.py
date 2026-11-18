
import heapq

cap1, cap2 = 4, 3
goal = 2

def h(state):
    return 0 if state[0] == goal else 1

def astar():
    pq = [(h((0, 0)), 0, (0, 0), [(0, 0)])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state[0] == goal:
            return path

        if state in visited:
            continue

        visited.add(state)
        x, y = state

        moves = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x-min(x, cap2-y), y+min(x, cap2-y)),
            (x+min(y, cap1-x), y-min(y, cap1-x))
        ]

        for nxt in moves:
            if nxt not in visited:
                new_g = g + 1
                new_f = new_g + h(nxt)
                heapq.heappush(
                    pq, (new_f, new_g, nxt, path + [nxt])
                )

    return None

# Display solution
solution = astar()

print("Water Jug Problem using A* Search")
for i, state in enumerate(solution):
    print("Step", i, ":", state)

print("Goal Achieved!")
