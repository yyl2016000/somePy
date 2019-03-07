class Solution:
    def longestPalindrome(self, s: str) -> str:
        str = ""
        for i in range(2*len(s)-1):
            if i%2 == 0:
                start = end = i//2
                while start>=0 and end<len(s) and s[start]==s[end]:
                    start-=1
                    end+=1
            else:
                start = (i-1) // 2
                end = (i+1) //2
                while start>=0 and end<len(s) and s[start]==s[end]:
                    start-=1
                    end+=1
            if len(str)<=(end-start-1):
                str=s[start+1:end]
        return str

def main():
    in_str = input()
    ret = Solution().longestPalindrome(in_str)
    print(ret)

if __name__ == '__main__':
    main()