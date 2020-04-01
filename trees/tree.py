# Binary Searh Tree node

class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def min(self):
        root = self
        while root and root.left:
            root = root.left
        return root

    def insert(self, key):
        if key < self.key:
            if not self.left:
                self.left = BSTNode(key)
                return self.left
            return self.left.insert(key)

        if key > self.key:
            if not self.right:
                self.right = BSTNode(key)
                return self.right
            return self.right.insert(key)

        return self
    
    def delete(self, key):
        return BSTNode._delete(self, key)
    
    @staticmethod
    def _delete(root, key, parent=None):
        if not root:
            return None
        
        if key < root.key:
            return BSTNode._delete(root.left, key, root)
        if key > root.key:
            return BSTNode._delete(root.right, key, root)
        
        # root has the key
        # if no children, delete root making parent stop pointing to it
        if not root.left and not root.right:
            if parent:
                if parent.left == root:
                    parent.left = None
                elif parent.right == root:
                    parent.right = None
            return root

        # if root has only one child, make parent point to it and not to root
        if root.left and not root.right:
            if parent:
                if parent.left == root:
                    parent.left = root.left
                else:  # parent.right == root
                    parent.right = root.left
            root.left = None  # clear the node
            return root
        
        elif root.right and not root.left:
            if parent:
                if parent.left == root:
                    parent.left = root.right
                else:  # parent.right == root
                    parent.right = root.right
            return root

        else:  # 2 children
            # swap successor key
            m = root.right.min()
            temp = m.key
            m.key = root.key
            root.key = temp
            # and delete it (it won't have 2 children now)
            return BSTNode._delete(root.right, key, parent=root)
        
    def height(self):
        left, right = 0, 0
        if self.left:
            left = self.left.height()
        if self.right:
            right = self.right.height()
        return max([left, right]) + 1

    def __str__(self):
        return str(self.key)


class BSTLinkedNode(BSTNode):
    """Node with link to its parent node"""
    def __init__(self, key, parent=None):
        super().__init__(key)
        self.parent = parent

    def insert(self, node):
        if node.key < self.key:
            if not self.left:
                node.parent = self
                self.left = node
                return self.left
            return self.left.insert(node)

        if node.key > self.key:
            if not self.right:
                node.parent = self
                self.right = node
                return self.right
            return self.right.insert(node)

        return self

    def __str__(self):
        return str(self.key)


def inorder_traversal(root, fn):
    if not root:
        return

    inorder_traversal(root.left, fn)
    fn(root.key)
    inorder_traversal(root.right, fn)


def build_default_tree():
    t = BSTNode(4)
    t.insert(2)
    t.insert(1)
    t.insert(3)
    t.insert(6)
    t.insert(5)
    t.insert(7)
    return t


if __name__ == "__main__":
    t = BSTNode(5)
    t.insert(3)
    t.insert(1)
    t.insert(6)
    t.insert(4)
    
    print("inorder_traversal")
    inorder_traversal(t, print)

    print(f"height: {t.height()}")

    print(f"delete {t.delete(1)}")
    print(f"delete {t.delete(4)}")

    print(f"height: {t.height()}")
    
    print(f"min: {t.min().key}")
