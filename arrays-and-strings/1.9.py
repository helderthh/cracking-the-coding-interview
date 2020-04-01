# String Rotation: Assumeyou have a 
# method isSubstring which checks if 
# one word is a substring of another.
# Given two strings, s1 and s2, write 
# code to check if s2 is a rotation of
# s1 using only one call to isSubstring
#  (e.g.,"waterbottle" is a rotation of"erbottlewat").


def is_rotation(s1, s2):
    is_start = False
    for i, c1 in enumerate(s1):
        is_start = True
        aux_index = i

        for c2 in s2:
            if s1[aux_index] != c2:
                is_start = False
                break
            
            aux_index = (aux_index + 1) % len(s1)

        if is_start:
            break
    
    if not is_start:
        return False

    return s1[i:] + s1[:i] == s2

if __name__ == "__main__":
    print(is_rotation("house", "house"))
    print(is_rotation("house", "sehou"))
    print(is_rotation("house", "ehous"))
    print(is_rotation("house", "useho"))
    print(is_rotation("house", "ouseh"))
    print(is_rotation("house", "ousea"))


