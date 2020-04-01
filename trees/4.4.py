# Check Balanced: Implement a function to check if a binary 
# tree is balanced. For the purposes of this question, a 
# balanced tree is defined to be a tree such that the heights
# of the two subtrees of any node never differ by more than one.

from tree import BSTNode, build_default_tree


def check_balance(t):
    _, balanced = _height(t)
    return balanced

def _height(root):
    if not root:
        return 0, True
    l, ok = _height(root.left)
    if not ok:
        return None, False
    r, ok = _height(root.right)
    if not ok:
        return None, False

    return max([l, r]) + 1, abs(l - r) <= 1


if __name__ == "__main__":
    t = build_default_tree()
    print(check_balance(t))

    t = BSTNode(4)
    t.insert(2)
    t.insert(1)
    t.insert(3)
    print(check_balance(t))

