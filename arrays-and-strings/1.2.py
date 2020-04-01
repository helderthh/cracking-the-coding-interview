# Check Permutation: Given two strings, write a 
# method to decide if one is a permutation of the
# other.

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True



if __name__ == "__main__":
    print(check_permutation("zabv", "bzva"))
    print(check_permutation("horse", "house"))
    print(check_permutation("keep", "peek"))

