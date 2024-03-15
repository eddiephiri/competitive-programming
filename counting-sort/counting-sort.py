class Solution:
    def countingSort(self, n: int, arr: list[int])-> list[int]:
        res = [0] * 100

        for i in arr:
            res[i] += 1
        print(*res)

        return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ans = Solution().countingSort(n, arr)
    print(*ans)
