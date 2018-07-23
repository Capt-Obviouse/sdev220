class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def serach(self, e):
        current = self.root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                return True
        return False

    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e)
        else:
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False

            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1
        return True

    def createNewNode(self, e):
        return TreeNode(e)

    def getSize(self):
        return self.size

    def inorder(self):
        self.inorderHelper(self.root)

    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    def postorder(self):
        self.postorderHelper(self.root)

    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    def preorder(self):
        self.preorderHelper(self.root)

    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    def path(self, e):
        list = []
        current = self.root

        while current != None:
            list.append(current)
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break
        return list

    def delete(self, e):
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element:
                parent = current
                current = current.right
            else:
                break

        if current == None:
            return False

        if current.left == None:
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = current
                rightMost = current.left

            current.element = rightMost.element

            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                parentOfRightMost.left = rightMost.left

        self.size -= 1
        return True
    def isEmpty(self):
        return self.size == 0

    def clear(self):
        self.root = None
        self.size == 0

    def getRoot(self):
        return self.root


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None


tree = BinaryTree()
tree.insert("George")
tree.insert("Michael")
tree.insert("Tom")
tree.insert("Adam")

print("Inorder (sorted): ", end = " ")
tree.inorder()
print()
