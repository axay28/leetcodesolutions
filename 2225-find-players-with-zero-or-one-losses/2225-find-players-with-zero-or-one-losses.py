class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set()
        losses=collections.Counter()
        for winner,loser in matches:
            losses[loser]+=1
            players.add(winner)
            players.add(loser)
        # print(losses)
        # print(players)
        no_losses,one_loss=[],[]
        for player in players:
            if losses[player]==1:
                one_loss.append(player)
                # print(one_loss)
            elif losses[player]==0:
                no_losses.append(player)
                # print(no_losses)
        return [sorted(no_losses),sorted(one_loss)]