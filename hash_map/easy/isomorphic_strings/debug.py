class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        isoDictS = {}
        isoDictT = {}
        for i in range(len(s)):

            print(f'isoDictS at {i}: {isoDictS}')
            print(f'isoDictT at {i}: {isoDictT}')
            print(f'isoDictS.keys() at {i}: {isoDictS.keys()}')
            print(f't[i] at {i}: {t[i]}\n')

            if t[i] in isoDictT.keys() and isoDictT[t[i]] != s[i]:
                print('here')
                return False
            else:
                isoDictT[t[i]] = s[i]
            if s[i] in isoDictS.keys() and isoDictS[s[i]] != t[i]:
                print('there')
                return False
            else:
                isoDictS[s[i]] = t[i]
        
        print(f'isoDictS at {i}: {isoDictS}')
        print(f'isoDictT at {i}: {isoDictT}')
        print(f'isoDictS.keys() at {i}: {isoDictS.keys()}')
        print(f't[i] at {i}: {t[i]}\n')

        return True

s = "egg"
t = "add"    
print(Solution().isIsomorphic(s=s, t=t))