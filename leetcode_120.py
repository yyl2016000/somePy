class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return 0
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]

def main():
    in_list = list(input())
    print(Solution().minimumTotal(in_list))

if __name__ == '__main__':
    main()