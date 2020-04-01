# List of Depths: Given a binary tree, design an algorithm
# which creates a linked list of all the nodes at each depth
# (e.g., if you have a tree with depth D, you'll have D linked lists).

from tree import BSTNode, build_default_tree


def list_of_depths(root, path=[], paths=[]):
    if not root:
        return paths

    path.append(root)
    
    if not root.left and not root.right:
        # end of path
        paths.append(path)
        return paths

    # add current node to the path
    list_of_depths(root.left, path.copy(), paths)
    list_of_depths(root.right, path.copy(), paths)
    return paths


if __name__ == "__main__":
    t = build_default_tree()
    paths = list_of_depths(t)
    
    print(f"total paths: {len(paths)}")
    for p in paths:
        print("---")
        s = ""
        for n in p:
            s += f"{n} "
        print(s)



