class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        RVotes = 0
        DVotes = 0
        
        while (True):
            queue = []
            flagR = False
            flagD = False
            for i in senate:
                if i == 'D':
                    flagD = True
                    if RVotes > 0:
                        RVotes -= 1
                        continue
                    else:
                        DVotes += 1
                        queue.append('D')
                if i == 'R':
                    flagR = True
                    if DVotes > 0:
                        DVotes -= 1
                        continue
                    else:
                        RVotes += 1
                        queue.append('R')
            if flagR and flagD:
                senate = queue
            else:
                if flagR:
                    return 'Radiant'
                else:
                    return 'Dire'
