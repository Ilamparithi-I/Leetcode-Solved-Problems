class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for i in asteroids:
            if (i < 0):
                flag = True
                while(len(result) != 0):
                    val = result.pop()
                    if val > 0:
                        if abs(val) > abs(i):
                            result.append(val)
                            break
                        elif abs(val) == abs(i):
                            flag = False
                            break
                        else:
                            continue
                    else:
                        result.append(val)
                        result.append(i)
                        break
                if (flag and len(result) == 0):
                    result.append(i)
            else:
                result.append(i)
        return result
