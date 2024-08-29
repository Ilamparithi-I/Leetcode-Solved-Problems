class Solution:
    def removeStars(self, s: str) -> str:
        current = 0
        st = []
        for i in s:
            if i == '*':
                st.pop()
            else:
                st.append(i)
        return ''.join(st)