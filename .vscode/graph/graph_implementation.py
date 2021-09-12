class NodeTree:
    def __init__(self, data, designation) -> None:
        self.data = data
        self.children = []
        self.parent = None
        self.designation = designation

    def add_child(self, child) -> None:
        """add child to current node.

        Args:
            child (NodeTree): input node of graph
        """
        self.children.append(child)
        child.parent = self
        #self.designation = child.designation

    def get_level(self):
        level = 0 
        p = self.parent
        while p:
            p = p.parent
            level +=1
        return level

    def print_tree(self,flag):
        if flag == "both":
            printFormat = str(self.data) +'(' + str(self.designation) + ')'
        elif flag == "name":
            printFormat = str(self.data)
        else:
            printFormat =  str(self.designation)


       # printFormat = str(self.data) +'(' + str(self.designation) + ')' if flag==1 else flag==2 str(self.data)
        final_format = " "*3*self.get_level()+ '|__' + printFormat
        #print(self.data, '(', self.designation, ')')
        print(final_format)
        for child in self.children:
            #print(child.data, '(', child.designation, ')') 
            if child.print_tree(flag):
                print_tree(child.print_tree(flag), flag)


root = NodeTree("Mohammad","CEO")
member1 = NodeTree("Minoo","Worker")
member2 = NodeTree("Shahram","Eng")
member3 = NodeTree("Milad","Clerk")

member1.add_child(member3)
root.add_child(member1)
root.add_child(member2)

#print(root.children[1].parent)
#print(member1.parent)
root.print_tree("both")

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

print("hello world")