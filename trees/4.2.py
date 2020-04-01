# Given a sorted (increasing order) array with unique integer
# elements, write an algo­rithm to create a binary search tree
# with minimal height.

from tree import BSTNode, inorder_traversal


def _build_tree(array, l, r):
    if not array or l > r:
        return None

    mid = (l + r) // 2

    root = BSTNode(array[mid])
    root.left = _build_tree(array, l, mid - 1)
    root.right = _build_tree(array, mid + 1, r)
    return root


def build_tree_from_sorted_array(l):
    return _build_tree(l, 0, len(l) - 1)


if __name__ == "__main__":
    l = [1,2,3,4,5,6,7]
    t = build_tree_from_sorted_array(l)
    inorder_traversal(t, print)

    print(f"height: {t.height()}")
    print(f"min: {t.min()}")


