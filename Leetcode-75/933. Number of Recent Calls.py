class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        count = 0
        for i in range(0, len(self.counter)):
            # everything after current time - 3000 is valid
            if(self.counter[i] >= t-3000):
                count = len(self.counter) - i
                # remove everything before current time - 3000 because ping is always in increasing order
                self.counter = self.counter[i:len(self.counter)]
                break
        return count

