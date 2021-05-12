from typing import List
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # step1: 그래프 초기화
        graph = collections.defaultdict(list)
        for u, v, w in times: graph[u].append((v, w))

        # step2: bfs
        visited = set()
        # 시작 노드를 제외한 모든 노드로의 거리를 무한대로 초기화
        distance = {i: float('inf') for i in range(1, n+1)}
        distance[k] = 0

        # 첫 노드로 시작할 것
        min_heap = [(0, k)]

        while min_heap:
            # step3: 가작 작은 거리의 노드 찾기
            cost, node = heapq.heappop(min_heap)
            visited.add(node)
            if len(visited) == n: return cost
            for node2, cost2 in graph[node]:
                if node2 in visited: continue
                # step4: 새로운 cost(거리)가 기존의 거리보다 더 짧으면 갱신
                if distance[node2] > cost + cost2: distance[node2] = cost + cost2
                heapq.heappush(min_heap, (cost + cost2, node2))
        return -1