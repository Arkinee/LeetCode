from collections import deque

class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        ans = 10000
        for i, j, d in roads:
            g[i].append((j, d))
            g[j].append((i, d))
        vis = set()
        dq = [1]
        while dq:
            node = dq.pop()
            vis.add(node)
            for i, d in g[node]:
                if i not in vis:
                    dq.append(i)
                ans = min(ans, d)
        return ans
        
        
        
        
            