import argparse
import numpy as np
import time

class mono_routing():
    def __init__(self, args):
        pass
    def parser(self): #You can modify it by yourself.
        with open("%s" % args.input, 'r') as file_in:
            f = file_in.read().splitlines()
            for lines in f:
                if lines.startswith("BoundaryIndex"):
                    value_list = lines.split(' ')
                    self.Bx1 = int(value_list[1])
                    self.By1 = int(value_list[2])
                    self.Bx2 = int(value_list[3])
                    self.By2 = int(value_list[4])
                if lines.startswith("DefaultCost"):
                    value_list = lines.split(' ')
                    self.default_cost = int(value_list[-1])
                if lines.startswith("NumNonDefaultCost"):
                    value_list = lines.split(' ')
                    self.size = int(value_list[-1])
                    break
            
            source_list = list(f[-2].split(' '))
            target_list = list(f[-1].split(' '))
            self.sx = source_list[1]
            self.sy = source_list[2]
            self.tx = target_list[1]
            self.ty = target_list[2]
            self.num_cost = f[3:3+int(self.size)]
        
        """Print parameters"""
        print('BoundaryIndex:',self.Bx1,self.By1,self.Bx2,self.By2)
        print('DefaultCost:',self.default_cost)
        print('NumNonDefaultCost:',self.size)
        for i in range(len(self.num_cost)):
            print(self.num_cost[i])
        print('Source:',self.sx, self.sy)
        print('Target:',self.tx, self.ty)
    def routing(self):
        self.routing_path = np.zeros((self.Bx2+self.By2+1,2),dtype=int)
        self.grid_cost = np.zeros((self.By2+1,self.Bx2+1),dtype=int)
        # ---TODO:
        # Write down your routing algorithm by using dynamic programming.
        # ---
        self.cost = dict()
        self.path = []
        for i in range (0, self.By2+1):
            self.path.append([0] * (self.Bx2 + 1))
        for item in self.num_cost:
            item = item.split(' ')
            key = (int(item[0]),int(item[1]),int(item[2]),int(item[3]))
            self.cost[key] = int(item[-1]) + self.default_cost
            key = (int(item[2]),int(item[3]),int(item[0]),int(item[1]))
            self.cost[key] = int(item[-1]) + self.default_cost

        for i in range(1, self.By2+1):
            self.grid_cost[i][0] = self.grid_cost[i-1][0] + self.cost.get((i, 0, i-1, 0), self.default_cost)
            self.path[i][0] = 'fromleft_i'

        for j in range(1, self.Bx2+1):
            self.grid_cost[0][j] = self.grid_cost[0][j-1] + self.cost.get((0, j, 0, j-1), self.default_cost)
            self.path[0][j] = 'frombuttom_j'
        
        for i in range(1, self.By2+1):
            for j in range(1, self.Bx2+1):
                fromleft_i = self.grid_cost[i-1][j] + self.cost.get((i, j, i-1, j), self.default_cost)
                frombuttom_j = self.grid_cost[i][j-1] + self.cost.get((i, j, i, j-1), self.default_cost)
                if fromleft_i > frombuttom_j:
                    self.grid_cost[i][j] = frombuttom_j
                    self.path[i][j] = 'frombuttom_j'
                else:
                   self.grid_cost[i][j] = fromleft_i
                   self.path[i][j] = 'fromleft_i'
        self.routing_path[self.By2 + self.Bx2][0] = self.By2
        self.routing_path[self.By2 + self.Bx2][1] = self.Bx2
        for i in range(self.Bx2+self.By2-1, -1, -1):
            y, x = self.routing_path[i+1] 
            if self.path[y][x] == 'frombuttom_j':
                self.routing_path[i][1] = x - 1
                self.routing_path[i][0] = y
            else:
                self.routing_path[i][1] = x
                self.routing_path[i][0] = y - 1

    def output(self): # You can modify it by yourself, but the output format should be correct.
        with open("%s" % args.output, 'w') as file_out:
            file_out.writelines('RoutingCost %d'% self.grid_cost[self.By2][self.Bx2])
            file_out.writelines('\nRoutingPath %d'% len(self.routing_path))
            for i in range(len(self.routing_path)):
                file_out.writelines('\n%d %d'% (self.routing_path[i][0], self.routing_path[i][1]))
            
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default = './5x5.in',help="Input file root.")
    parser.add_argument("--output", type=str, default = './5x5.out',help="Output file root.")
    args = parser.parse_args()

    print('#################################################')
    print('#              Monotonic Routing                #')
    print('################################################# \n')

    routing = mono_routing(args)
    """Parser"""
    routing.parser()
    print('################ Parser Down ####################')
    """monotonic route"""
    start = time.time()
    routing.routing()
    print('run time:', round(time.time()-start,3))
    """output"""
    routing.output()