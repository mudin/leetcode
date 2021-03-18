# 478. Generate Random Point in a Circle

from random import seed
from random import random
import math


class Solution:
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x0 = x_center
        self.y0 = y_center
        seed(2)

    def randPoint(self):
        r, x0, y0 = self.radius, self.x0, self.y0
        t = random() * 2 * math.pi
        r = r * math.sqrt(random())
        x = r * math.cos(t) + x0
        y = r * math.sin(t) + y0
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
