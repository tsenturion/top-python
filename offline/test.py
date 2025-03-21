N = int(input())
keys = [int(input()) for _ in range(N)]
visited = [False] * (N + 1)
count = 0

for i in range(1, N + 1):
    if not visited[i]:
        cycle = []
        current = i
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            current = keys[current - 1]
        if current in cycle:
            count += 1

print(count)