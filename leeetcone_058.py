class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a_list = s.split()
        if not a_list:
            return 0
        for i in a_list[-1]:
            if i <= '9' and i >= '0':
                break
        else:
            return len(a_list[-1])
        return 0

def main():
    s = input()
    print(Solution().lengthOfLastWord(s))

if __name__ == '__main__':
    main()