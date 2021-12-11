import argparse

class Node():
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BS_tree():
    def __init__(self):
        self.root = None
    def inorder(self, output):      # print the in-order traversal of binary search tree
        # TODO
        def inorder_inner(node):
            if node.left_child != None:
                inorder_inner(node.left_child)
            output.write(repr(node))
            output.write(' ')
            if node.right_child != None:
                inorder_inner(node.right_child)
        if self.root == None:
            return
        inorder_inner(self.root)
        output.write('\n')
        pass
    def preorder(self, output):     # print the pre-order traversal of binary search tree
        # TODO
        def preorder_inner(node):
            output.write(repr(node))
            output.write(' ')
            if node.left_child != None:
                preorder_inner(node.left_child)            
            if node.right_child != None:
                preorder_inner(node.right_child)
        if self.root == None:
            return
        preorder_inner(self.root)
        output.write('\n')
        pass
    def postorder(self, output):    # print the post-order traversal of binary search tree
        # TODO
        def postorder_inner(node):
            if node.left_child != None:
                postorder_inner(node.left_child)
            if node.right_child != None:
                postorder_inner(node.right_child)
            output.write(repr(node))
            output.write(' ')
        if self.root == None:
            return
        postorder_inner(self.root)
        output.write('\n')
        pass
    def find_max(self, output):     # print the maximum number in binary search tree
        # TODO
        current = self.root
        while current.right_child is not None:
            current = current.right_child
        output.write(repr(current))
        output.write('\n')
        pass
    def find_min(self, output):     # print the minimum number in binary search tree
        # TODO
        current = self.root
        while current.left_child is not None:
            current = current.left_child
        output.write(repr(current))
        output.write('\n')
        pass
    def insert(self, key):          # insert one node
        # TODO
        if self.root == None:
            self.root = Node(key)
            return
        
        cur_Node = self.root
        while True:
            if key == cur_Node.value:
                return
            if key < cur_Node.value:
                if cur_Node.left_child == None:
                    cur_Node.left_child = Node(key)
                    return
                cur_Node = cur_Node.left_child
            if key > cur_Node.value:
                if cur_Node.right_child == None:
                    cur_Node.right_child = Node(key)
                    return
                cur_Node = cur_Node.right_child
        pass
    def delete(self, key):          # delete one node
        # TODO
        if self.root == None:
            return
        if self.root.value == key:
            if self.root.left_child == self.root.right_child == None:
                self.root = None
                return
            if self.root.left_child != None and self.root.right_child != None:
                min = self.root.right_child
                min_parent = self.root
                while min.left_child != None:
                    min = min.left_child
                    if min_parent == self.root:
                        min_parent = min_parent.right_child
                    else:
                        min_parent = min_parent.left_child
                if min.right_child == None:
                    if min_parent == self.root:
                        min_parent.right_child = None
                    else:
                        min_parent.left_child = None
                else:
                    if min_parent == self.root:
                        min_parent.right_child = min.right_child
                    else:
                        min_parent.left_child = min.right_child
                    
                self.root.value = min.value
                return
            if self.root.left_child == None:
                self.root = self.root.right_child
                return
            if self.root.right_child == None:
                self.root = self.root.left_child
                return            

        if key < self.root.value:
            if self.root.left_child == None:
                return
            parent = (self.root, 'left')
            cur_Node = self.root.left_child
            
        if key > self.root.value:
            if self.root.right_child == None:
                return
            parent = (self.root, 'right')
            cur_Node = self.root.right_child
            
        while True:
            if key == cur_Node.value:
                break
            if key < cur_Node.value:
                if cur_Node.left_child == None:
                    return
                cur_Node = cur_Node.left_child
                if parent[1] == 'left':
                    parent = (parent[0].left_child, 'left')
                else:
                    parent = (parent[0].right_child, 'left')
            if key > cur_Node.value:
                if cur_Node.right_child==None:
                    return
                cur_Node = cur_Node.right_child
                if parent[1] == 'left':
                    parent = (parent[0].left_child, 'right')
                else:
                    parent = (parent[0].right_child, 'right')    

        if cur_Node.left_child == cur_Node.right_child == None:
            if parent[1] == 'left':
                parent[0].left_child = None
            else:
                parent[0].right_child = None
            return
        if cur_Node.left_child != None and cur_Node.right_child != None:
            min = cur_Node.right_child
            min_parent = cur_Node
            while min.left_child != None:
                min = min.left_child
                if min_parent == cur_Node:
                    min_parent = min_parent.right_child
                else:
                    min_parent = min_parent.left_child
            if min.right_child == None:
                if min_parent == cur_Node:
                    min_parent.right_child = None
                else:
                    min_parent.left_child = None
            else:
                if min_parent == cur_Node:
                    min_parent.right_child = min.right_child
                else:
                    min_parent.left_child = min.right_child
            cur_Node.value = min.value
            return
        if cur_Node.left_child == None:
            if parent[1] == 'left':
                parent[0].left_child = cur_Node.right_child
            else:
                parent[0].right_child = cur_Node.right_child
            return
        if cur_Node.right_child == None:
            if parent[1] == 'left':
                parent[0].left_child = cur_Node.left_child
            else:
                parent[0].right_child = cur_Node.left_child
            return
        pass
    def level(self, output):        # print the height of binary search tree(leaf = 0)
        # TODO
        def level_inner(node):
            if node.left_child and node.right_child:
                return 1 + max(level_inner(node.left_child), level_inner(node.right_child))
            elif node.left_child:
                return 1 + level_inner(node.left_child)
            elif node.right_child:
                return 1 + level_inner(node.right_child)
            else:
                return 0
        cur_Node = self.root
        if cur_Node:
            ans = level_inner(cur_Node)
        else:
            return
        output.write(str(ans))
        output.write('\n')
        pass
    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest 
        # TODO
        q = []
        ans = []
        q.append(self.root)
        while len(q):
            curr = q[0]
            q.pop(0)
            Internal = False
            if curr.left_child:
                Internal = True
                q.append(curr.left_child)
            if curr.right_child:
                Internal = True
                q.append(curr.right_child)
            if Internal:
                ans.append(curr.value)
        ans.sort()
        for i in range(0, len(ans)):
            output.write(str(ans[i]))
            output.write(' ')
        output.write('\n')
        pass
    def leafnode(self, output):     # print the leafnode in BST from left to right
        # TODO
        s1 = []
        s2 = []
        s1.append(self.root)
        while len(s1) != 0:
            curr = s1.pop()
            if curr.left_child:
                s1.append(curr.left_child) 
            if curr.right_child: 
                s1.append(curr.right_child) 
            elif not curr.left_child and not curr.right_child: 
                s2.append(curr) 
        while len(s2) != 0: 
            output.write(str(s2.pop()))
            output.write(' ')
        output.write('\n')
        pass
    def main(self, input_path, output_path):
        #########################
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # DO NOT MODIFY CODES HERE
        # It's important and repeat three times
        #########################
        output = open(output_path, 'w')
        with open(input_path, 'r') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("insert"):
                    value_list = lines.split(' ')
                    for value in value_list[1:]:
                        self.insert(int(value))
                if lines.startswith('inorder'):
                    self.inorder(output)
                if lines.startswith('preorder'):
                    self.preorder(output)
                if lines.startswith('postorder'):
                    self.postorder(output)
                if lines.startswith('max'):
                    self.find_max(output)
                if lines.startswith('min'):
                    self.find_min(output)
                if lines.startswith('delete'):
                    value_list = lines.split(' ')
                    self.delete(int(value_list[1]))
                if lines.startswith('level'):
                    self.level(output)
                if lines.startswith('internalnode'):
                    self.internalnode(output)
                if lines.startswith('leafnode'):
                    self.leafnode(output)
        output.close()
if __name__ == '__main__' :
    #########################
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    #########################
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './input_1.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_1.txt',help="Output file root.")
    args = parser.parse_args()
    
    BS = BS_tree()
    BS.main(args.input, args.output)
