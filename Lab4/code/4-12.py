import random

class HDPoints:
    def __init__(self, points):
        self.points = points

    def centerpoint(self):
        n = len(self.points)
        dim = len(self.points[0])
        center = [0]*dim
        for p in self.points:
            for i in range(dim):
                center[i] += p[i]
        return [c/n for c in center]

    def minkowski(self, x, y, p):
        if p == 0:
            return max(abs(a-b) for a,b in zip(x,y))
        s = sum(abs(a-b)**p for a,b in zip(x,y))
        return s ** (1/p)

    def farthestpoint(self, p):
        c = self.centerpoint()
        max_dist = -1
        idx = -1
        for i, pt in enumerate(self.points):
            d = self.minkowski(pt, c, p)
            if d > max_dist:
                max_dist = d
                idx = i
        return idx, max_dist

    def farthest2points(self, p):
        max_d = -1
        a = b = -1
        n = len(self.points)
        for i in range(n):
            for j in range(i+1, n):
                d = self.minkowski(self.points[i], self.points[j], p)
                if d > max_d:
                    max_d = d
                    a,b = i,j
        return a,b,max_d

# 随机生成50个5维点
points = [[random.random() for _ in range(5)] for _ in range(50)]
hd = HDPoints(points)
p = random.randint(0,5)
print("中心点:", hd.centerpoint())
print("最远点:", hd.farthestpoint(p))
print("最远两点:", hd.farthest2points(p))