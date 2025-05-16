from collections import deque, defaultdict

def get_alien_order(word_count):
    words = [input().strip() for _ in range(word_count)]

    graph = defaultdict(list)
    indegree = defaultdict(int)
    seen_letters = set()


    for i in range(word_count - 1):
        first, second = words[i], words[i + 1]
        if len(first) > len(second) and first.startswith(second):
            print(-1)
            return
        for a, b in zip(first, second):
            if a != b:
                graph[a].append(b)
                indegree[b] += 1
                break


    for word in words:
        for ch in word:
            seen_letters.add(ch)
            if ch not in indegree:
                indegree[ch] = 0


    zero_in = deque([ch for ch in seen_letters if indegree[ch] == 0])
    result = []

    while zero_in:
        zero_in = deque(sorted(zero_in))
        current = zero_in.popleft()
        result.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_in.append(neighbor)

    if len(result) == len(seen_letters):
        print("".join(result))
    else:
        print(-1)

n = int(input())
get_alien_order(n)