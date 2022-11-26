import math
import itertools

def check_palindrome(str):
    return str == str[::-1]

def get_anagrams(str):
    return ["".join(perm) for perm in itertools.permutations(str)]

class PalindromeMaker:
    palindrome = ''

    def insert_palindrome(self, str):
        if check_palindrome(str):
            half = str[:math.ceil(len(str) / 2)]
            self.palindrome = half + self.palindrome + half[::-1]
            return str + " is palindrome"
        else:
            return str + " is not palindrome"