'''
Jesse Duncan
SDEV 220
Programming Exercise: 19.1 - addMethods
Due July 22, 2018
'''


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
        self.postOrderHelper(self.root)

    def postOrderHelper(self, root):
        if root != None:
            self.postOrderHelper(root.left)
            self.postOrderHelper(root.right)
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




    def breadthFirstTraversal(self): #Breadth-First Traversal

      self.root.level = 0
      queue = [self.root]
      out = []
      current_level = self.root.level

      while len(queue) > 0:

         current_node = queue.pop(0)

         if current_node.level > current_level:
            current_level += 1
            out.append("\n")

         out.append(str(current_node.info) + " ")

         if current_node.left:

            current_node.left.level = current_level + 1
            queue.append(current_node.left)


         if current_node.right:

            current_node.right.level = current_level + 1
            queue.append(current_node.right)


      print ("".join(out))





    def breadthFirstTraversal(self):
        return(self.breadthFirstTraversalHelper(self.root))

    def breadthFirstTraversalHelper(self, root):
        nodes = []
        stack = [root]
        if root != None:
            level = 0
            while stack:
                cur_node = stack[0]
                stack = stack[1:]
                nodes.append(cur_node.element)
                print(cur_node.element, end = " ")
                if cur_node.left != None:
                    stack.append(cur_node.left)
                if cur_node.right != None:
                    stack.append(cur_node.right)

    def height(self):
        return self.heightHelper(self.root)

    def heightHelper(self, root):
        if root is None:
            return 0
        else:
            return max(self.heightHelper(root.left), self.heightHelper(root.right)) + 1

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
tree.insert("Jones")
tree.insert("Peter")
tree.insert("Daniel")
print("Inorder (sorted): ", end = "")
tree.inorder()
print("\nPostorder: ", end = "")
tree.postorder()
print("\nPreorder: ", end = "")
tree.preorder()
print("\nThe number of nodes is " + str(tree.getSize()))
print("Breadth First Traversal:", end = " ")
tree.breadthFirstTraversal()
print("\nThe height of the tree is: " + str(tree.height()))
