class Solution(object):
    def triangleType(self, nums):
        
        a, b, c = nums
        
        # Check for triangle inequality
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        
        # Determine the type of triangle
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
