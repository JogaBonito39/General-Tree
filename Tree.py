class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level += 1
            p = p.parent
        
        return level
            
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
        
    
        #print(self.data, ":")
        #for child in self.children:
        #    print("    " + child.data, ":")
        #    for child_of_child in child.children:
        #        print("        " + child_of_child.data)
     
     
def build_product_tree():
    #global laptop
    global root
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cellphone = TreeNode("Cell Phone")
    #callable
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    print(cellphone.children[0].get_level())
    print(cellphone.get_level())
    
    return root
    
if __name__ == '__main__':
    build_product_tree()
    #print(TreeNode().__dir__())
    #print(build_product_tree().__dir__())
    #print(laptop.__dict__)
    #print(root.__dict__)
    root.print_tree()
    print(root.get_level())