import sys; input = sys.stdin.readline
import heapq

def dijkstra(c):
    min_heap = []
    heapq.heappush(min_heap, (0, c))
    distance[c] = 0

    while min_heap:
        sec, node = heapq.heappop(min_heap)
        if distance[node] < sec: continue

        for new_sec, new_node in graph[node]:
            cost = sec + new_sec
            if distance[new_node] > cost: 
                distance[new_node] = cost
                heapq.heappush(min_heap, (cost, new_node))

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = {i: float('inf') for i in range(n+1)} 

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a)) # 가중치(초)와 노드(컴퓨터)
    
    dijkstra(c)

    result = list(filter(lambda x: x < float('inf'), distance.values()))
    time = max(result)
    virus_count = len(result)
    print(virus_count, time)
