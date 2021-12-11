import argparse
import time


class MyNode(object):
    # this class infor testing
    # Do Not Modify
    def __init__(self, value):
        self.value = value
        self.right = self
        self.left = self

    def __repr__(self):
        return 'Node%s'%(self.value)


class MyStack(object):
    def __init__(self):
        self.num_element = 0
        self.root = MyNode(None)

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty stack')
        else:
            self.num_element -= 1
            # ---TODO:
            # Connect the second last element >> root
            # Connect root >> the second last element
            # ---
            self.root.left = self.root.left.left
            self.root.left.right = self.root
        
    def push(self, node):
        self.num_element += 1
        # ---TODO:
        # Connect the last element >> inserted node
        # Connect the inserted node >> root
        # ---
        node.right = self.root
        node.left = self.root.left
        self.root.left.right = node
        self.root.left = node

    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret = ret + '>>' + str(node)
            node = node.right
        return ret


def main(input_file, output_file, has_ofile):
    myStack = MyStack()

    ifile = open(input_file)
    if has_ofile:
        ofile = open(output_file, 'w')
    else:
        ofile = None
    for line in ifile.readlines():
        items = line.strip().split(" ")
        if items[0] == 'PUSH':
            myVal = int(items[1])
            myStack.push(MyNode(myVal))
        else:
            myStack.pop()
        if has_ofile:
            ofile.write(str(myStack) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input_1.txt')  
    parser.add_argument('--output', default='')
    args = parser.parse_args()
    if len(args.output) > 0:
        has_ofile=True
    else:
        has_ofile=False
    ts = time.time()
    main(args.input, args.output, has_ofile)
    te = time.time()
    if not has_ofile:
        print('stack.py run time of %s: %.5fs'%( args.input, te - ts))
