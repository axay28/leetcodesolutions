class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set()
        losses=collections.Counter()
        for winner,loser in matches:
            losses[loser]+=1
            players.add(winner)
            players.add(loser)
        no_losses,one_loss=[],[]
        for player in players:
            if losses[player]==1:
                one_loss.append(player)
            elif losses[player]==0:
                no_losses.append(player)
        return [sorted(no_losses),sorted(one_loss)]