class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        g=[]
        g.append("."*n)
        for i in range(m-1):
            g.append("#"*(n-1)+".")
        return g