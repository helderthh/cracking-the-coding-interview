from tree import BSTLinkedNode as Node


def distance_to_root(node):
    dist = 0
    root = node
    while root.parent:
        dist += 1
        root = root.parent
    return dist


def common_ancestor(a, b):
    print(f"looking for common ancestors of {a} and {b}")
    if a and b and a.parent == b.parent:
        return a.parent

    a_distance = distance_to_root(a)
    b_distance = distance_to_root(b)
    diff = abs(a_distance - b_distance)

    # go up through node 'a' path to parent, at
    # (a_distance - diff) "step" will be the common ancestor
    ancestor = a.parent
    node = a
    for i in range(a_distance - diff):
        ancestor = node.parent
        node = node.parent
    return ancestor


if __name__ == "__main__":
    t = Node(4)
    t.insert(Node(2))
    t.insert(Node(1))
    t.insert(Node(3))
    t.insert(Node(6))
    t.insert(Node(5))
    t.insert(Node(7))
    t.insert(Node(8))
    t.insert(Node(9))
    a = t.right.left
    b = t.right.right

    ancestor = common_ancestor(a, b)
    print(f"common ancestor is {ancestor}")

