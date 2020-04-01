

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


def print_path(path):
    s = ""
    for p in path:
        s += str(p) + " "

    print(f"{s}\n---")

def paths_with_sum(root, total):
    return _paths_with_sum(root, total)

def _paths_with_sum(root, total, curr_total=0, curr_path=[]):
    if not root:
        return []

    paths = []
    curr_path.append(root)
    curr_total += root.key
    if curr_total == total:
        paths.append(curr_path)
    
    # look for paths continuing with the curr_path
    l_paths = _paths_with_sum(root.left, total, curr_total, curr_path.copy())
    r_paths = _paths_with_sum(root.right, total, curr_total, curr_path.copy())

    paths += l_paths + r_paths

    # look for paths using children as root
    l_paths = _paths_with_sum(root.left, total, 0, [])
    r_paths = _paths_with_sum(root.right, total, 0, [])
    paths += l_paths + r_paths
    
    return paths
    

if __name__ == '__main__':
    root = Node(2)

    x0 = Node(0)
    x0.left = Node(1)
    
    x3 = Node(3)
    x3.right = x0

    x1 = Node(1)
    x1.right = Node(4, None, Node(1))
    x1.left = x3
    root.left = x1

    x5 = Node(5)
    x5.right = Node(0, Node(-1), None)
    root.right = x5

    paths = paths_with_sum(root, 6)
    for path in paths:
        print_path(path)

