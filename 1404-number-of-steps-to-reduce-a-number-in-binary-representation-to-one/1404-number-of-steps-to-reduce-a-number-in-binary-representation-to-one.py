class Solution:
    def numSteps(self, s: str) -> int:
        deci = int(s, 2)
        count = 0

        while deci > 1:
            if deci % 2 == 0:
                deci //= 2
            else:
                deci += 1

            count += 1

        return count