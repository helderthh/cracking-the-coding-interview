# Given a string, write a function to 
# check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the 
# same forwards and backwards. A permutation 
# is a rearrangement of letters. The palindrome 
# does not need to be limited to just dictionary words.


def is_permutation_of_palindrome(s):
    freq = {}
    for c in s:
        if c == ' ':
            continue
        c = c.lower()
        freq[c] = freq.get(c, 0) + 1

    odd_count = 0
    for k, v in freq.items():
        if v % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False
    
    return True
    

if __name__ == "__main__":
    print(is_permutation_of_palindrome("Tact Coa"))
    print(is_permutation_of_palindrome("abbac"))
    print(is_permutation_of_palindrome("abba"))
    print(is_permutation_of_palindrome("aaabbc"))


