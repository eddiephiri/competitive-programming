class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [x for x in range(1, n + 1)]
        N = len(friends)
        running_i = 0

        while N > 1:
            elim = (running_i + k - 1) % N
            friends.pop(elim)
            N = len(friends)
            running_i = elim

        return friends[0]