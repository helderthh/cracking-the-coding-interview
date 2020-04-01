# BST Sequences: A binary search tree was created
# by traversing through an array from left to right
# and inserting each element. Given a binary search tree
# with distinct elements, print all possible arrays that 
# could have led to this tree.

from tree import build_default_tree


def bst_sequences(t):
    if t is None:
        return []
    if not t.left and not t.right:
        return [[t]]
        
    left_sequences = bst_sequences(t.left)
    right_sequences = bst_sequences(t.right)
    sequences = []

    # build sequences starting with the left child sequences
    for ls in left_sequences:
        for rs in right_sequences:
            s = [t]  # all sequences should start with the root
            s.extend(ls)
            s.extend(rs)
            sequences.append(s)
    # build sequences starting with the right child sequences
    for rs in right_sequences:
        for ls in left_sequences:
            s = [t]  # all sequences should start with the root
            s.extend(rs)
            s.extend(ls)
            sequences.append(s)
    return sequences


if __name__ == "__main__":
    t = build_default_tree()
    sequences = bst_sequences(t)
    for s in sequences:
        out = ""
        for p in s:
           out += str(p) + " "
        print(f"{out}")
    
    print(f"total sequences: {len(sequences)}")