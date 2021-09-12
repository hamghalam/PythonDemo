def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)


def fib(n):
    """
    0,1,1,2,3,5,8,13
    0,1,2,3,4,5,6,7
    """
    if n == 0:
        return 0
    if n == 1:
        return 1     
    
    return fib(n-1) + fib(n-2)
# 

def summation (a:list):
    if len(a) == 1:
        return a[0]

    return a[-1] + summation(a[:-1])



def convert_string(n:int, base):
    table = "0123456789ABCDEF"
    """
    10 //2 = 5  0
    5 // 2 = 2  1 
    2 // 2 = 1  0
    """
    if n < base:
        return table[n]
    return convert_string(n//base, base) + table[n % base]

def sumint(a:int):
    if( a < 10):
        return a
    b = a % 10
    a = a // 10
    return b + sumint(a)

def funct1(n:int):
    if n <= 0:
        return 0   

    return funct1(n-2) + n

def harmonicsum(n:int):
    if n==1:
        return 1
    return harmonicsum(n-1) + (1/n)

class Graph():
    def __init__(self, edges):
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

if __name__ == '__main__':
    #print(fib(7))
    #print(summation([1,2,10,11,55]))
    #a = [1,2]
    #print(a[:-1])
    #print(convert_string(125,16))
    #print(harmonicsum(3))

    routes = [("Mumbai","Paris"),
    ("Mumbai", "Dubai"),
    ("Paris","Dubai"),
    ("Paris","New York"),
    ("Dubai","New York"),
    ("New York","Toronto")   
    ]

    route_graph = Graph(routes)
    print(route_graph.graph_dict)

