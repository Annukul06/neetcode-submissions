class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = sorted(s)
        T = sorted(t)
        if T == S:
            return True

        else:
            return False 

    

        
        