class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # finalnum
        mult1 = 1
        ans = 0
        for i in reversed(range(len(num1))):
            mult2 = 1
            for j in reversed(range(len(num2))):
                # take num1 down and multiply by every number in the num2
                ans += int(num2[j])*mult1 * int(num1[i])*mult2
                mult2 *= 10
            mult1 *= 10
        return str(ans)