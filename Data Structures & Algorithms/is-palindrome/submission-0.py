class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        x = s.lower()
        for char in x:
            if "a" <= char <= 'z' or "0" <= char <= '9':
                string  += char

        rev_string = ""
        for char in string[::-1]:
            rev_string += char

        if rev_string == string:
            return True
        else:
            return False

       