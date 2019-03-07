class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[(i,j)] = 1
                else:
                    dp[(i,j)] = dp[(i-1,j)]+dp[(i,j-1)]
        return dp[(m-1,n-1)]

def main():
    in_str1 = int(input())
    in_str2 = int(input())
    ret = Solution().uniquePaths(in_str1,in_str2)
    print(ret)

if __name__ == '__main__':
    main()

'''
采用dp的方法来求解，进行遍历，每一个元素的值为到达该元素所在格的路径条数
每个元素的值为左边元素加上方的元素的值

'''