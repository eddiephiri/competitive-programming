class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player_stats = {}
        winners = []
        losers = []

        for winner, loser in matches:
            if winner not in player_stats:
                player_stats[winner] = 0
            if loser not in player_stats:
                player_stats[loser] = 1
            elif loser in player_stats:
                player_stats[loser] += 1
        
        for item in player_stats.items():
            if item[1] == 0:
                winners.append(item[0])
            elif item[1] == 1:
                losers.append(item[0])

        return [sorted(winners), sorted(losers)]
        