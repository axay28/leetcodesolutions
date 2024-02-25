class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            pre[c].append(p)
        visited=set()
        def dfs(c):
            if c in visited:
                return False
            if pre[c]==[]:
                return True
            visited.add(c)
            for p in pre[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            pre[c]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True