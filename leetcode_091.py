class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = {-1:1,0:1}
        for i in range(1,len(s)):
            if s[i] == '0':
                if (s[i-1] == '1' or s[i-1] == '2'):
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[len(s)-1]

def main():
    in_str = input()
    print(Solution().numDecodings(in_str))

if __name__ == '__main__':
    main()