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

def Inorder(current,output):
    if(current == None):
        return
    if(current.left_child != None):
        Inorder(current.left_child,output)
    output.write(str(current.value)+" ")
    if(current.right_child != None):
        Inorder(current.right_child,output)
    return

def Preorder(current,output):
    if(current == None):
        return
    output.write(str(current.value)+" ")
    if(current.left_child != None):
        Preorder(current.left_child,output)
    if(current.right_child != None):
        Preorder(current.right_child,output)
    return

def Postorder(current,output):
    if(current == None):
        return
    if(current.left_child != None):
        Postorder(current.left_child,output)
    if(current.right_child != None):
        Postorder(current.right_child,output)
    output.write(str(current.value)+" ")
    return

def Level(current):
    if(current == None):
        return -1
    return max(Level(current.right_child),Level(current.left_child))+1

def InternalNode(current,output):
    if(current == None):
        return
    if(current.left_child != None):
        InternalNode(current.left_child,output)

    if(current.left_child != None or current.right_child != None):
        output.write(str(current.value)+" ")

    if(current.right_child != None):
        InternalNode(current.right_child,output)
    return

def LeafNode(current,output):
    if(current == None):
        return -1
    if(current.left_child != None):
        LeafNode(current.left_child,output)

    if(current.right_child != None):
        LeafNode(current.right_child,output)
    
    if(current.left_child == None and current.right_child == None):
        output.write(str(current.value)+" ")

def ExtractMin(root):
    min_node = root
    parent_node = root
    while(min_node.left_child != None):
        parent_node = min_node
        min_node = min_node.left_child
    parent_node.left_child = min_node.right_child
    return min_node
    

class BS_tree():
    def __init__(self):
        self.root = None

    def inorder(self, output):      # print the in-order traversal of binary search tree
        Inorder(self.root, output)
        output.write('\n')
        return
    def preorder(self, output):     # print the pre-order traversal of binary search tree
        Preorder(self.root, output)
        output.write('\n')
        return
    def postorder(self, output):    # print the post-order traversal of binary search tree
        Postorder(self.root, output)
        output.write('\n')
        return

    def find_max(self, output):     # print the maximum number in binary search tree
        max = self.root
        if(max == None):
            pass
        while(max.right_child != None):
            max = max.right_child
        output.write(str(max)+"\n")

    def find_min(self, output):     # print the minimum number in binary search tree
        min = self.root 
        if(min == None):
            pass
        while(min.left_child != None):
            min = min.left_child
        output.write(str(min)+"\n")

    def insert(self, key):          # insert one node
    
        current = self.root
        if(current == None):
            self.root = Node(key)
            return
        while(True):
            if(key > current.value):
                if(current.right_child == None):
                    current.right_child = Node(key)
                    return
                current = current.right_child

            elif(key < current.value):
                if(current.left_child == None):
                    current.left_child = Node(key)
                    return
                current = current.left_child

    def delete(self, key):          # delete one node
        if(self.root == None):
            return
        current = self.root
        parent = self.root

        while(current.value != key):
            parent = current
            if(key > current.value):
                current = current.right_child
            elif(key < current.value):
                current = current.left_child
            if(current == None):
                return

        is_right = bool(current.value >= parent.value)
        
        # delete case by case
        if(current.left_child == None and current.right_child == None):     # node has no child
            if(current == self.root):
                self.root = None
            elif(is_right):
                parent.right_child = None
            else:
                parent.left_child = None

        elif(current.right_child != None and current.left_child!= None):    # node has two children
            sub = ExtractMin(current.right_child)
            if(current == self.root):
                self.root.value = sub.value
            elif(is_right):
                parent.right_child.value = sub.value
            else:
                parent.left_child.value = sub.value        

        elif(current.left_child != None):       # node has only left child
            if(current == self.root):
                self.root = current.left_child
            elif(is_right):
                parent.right_child = current.left_child
            else:
                parent.left_child = current.left_cild
        
        elif(current.right_child != None):      # node has only right child
            if(current == self.root):
                self.root = current.right_child
            elif(is_right):
                parent.right_child = current.right_child
            else:
                parent.left_child = current.right_child
        
        
        

    def level(self, output):        # print the height of binary search tree(leaf = 0)
        output.write(str(Level(self.root))+"\n")
        return

    def internalnode(self, output): # print the internal node in binary search tree from the smallest to the largest 
        InternalNode(self.root, output)
        output.write('\n')
        return

    def leafnode(self, output):     # print the leafnode in BST from left to right
        LeafNode(self.root,output)
        output.write('\n')
        return

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
    parser.add_argument("--input", type=str, default = './input_3.txt',help="Input file root.")
    parser.add_argument("--output", type=str, default = './output_3.txt',help="Output file root.")
    args = parser.parse_args()
    
    BS = BS_tree()
    BS.main(args.input, args.output)

    

