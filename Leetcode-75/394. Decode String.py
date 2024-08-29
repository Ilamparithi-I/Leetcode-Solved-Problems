class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        for i in s:
            if i != ']':
                result.append(i)
            else:
                string = []
                sect = []
                number = []
                numberc = []
                while(True):
                    val = result.pop()
                    if val == '[':
                        while (len(result)!=0):
                            num = result.pop()
                            if num.isdigit():
                                number.append(num)
                            else:
                                result.append(num)
                                break
                        break
                    else:
                        string.append(val)
                for i in range(len(string)):
                    val = string.pop()
                    sect.append(val)
                for i in range(len(number)):
                    val = number.pop()
                    numberc.append(val)
                sect = ''.join(sect)
                sect = sect * int(''.join(numberc))
                result = result + list(sect) 
        return ''.join(result)