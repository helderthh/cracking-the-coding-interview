
# One Away: There are three types of edits that 
# can be performed on strings: insert 
# a character, remove a character, or 
# replace a character. Given two strings,
# write a function to check if they are
# one edit (or zero edits) away.
# 
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false


def is_one_away(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    if abs(len_s1 - len_s2) > 1:
        return False

    # find differences
    i = 0  # iterate s1
    j = 0  # iterate s2
    diff = 0
    max_idx = min(len_s1, len_s2)

    while i < max_idx and j < max_idx:
        if s1[i] != s2[j]:
            diff += 1
            if len_s1 < len_s2:
                j += 1
                continue
            elif len_s1 > len_s2:
                i += 1
                continue

        i += 1
        j += 1

    return diff <= 1


if __name__ == "__main__":
    print(is_one_away("pale", "ple"))
    print(is_one_away("pales", "pale"))
    print(is_one_away("pale", "bale"))
    print(is_one_away("pale", "bake"))
    print(is_one_away("pale", "bakess"))