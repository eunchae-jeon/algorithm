def solution(directory, command):
    answer = []
    t = Tree()
    for di in directory:
        t.mkdir(di)
    for c in command:
        c.split()
    answer = t.print_dir()
    return answer


class Node():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def has_node(self, node_name):
        for n in self.children:
            if n.name == node_name:
                return True
        return False

    def get_node(self, node_name):
        for n in self.children:
            if n.name == node_name:
                return n
        return None

    def create_node(self, node_name):
        node = Node(node_name, self)
        self.children.append(node)
        return node

    def get_path(self):
        path = ""
        cur = self
        while True:
            path = cur.name + "/" + path
            print(path)
            cur = cur.parent
            if cur == None:
                break
        return path[:-1]

class Tree():
    def __init__(self):
        self.root = Node("", None)

    def mkdir(self, path, cur_node=None):
        if path == "/" or "":
            return
        if cur_node == None:
            cur_node = self.root
        next_node = ""
        path = path[1:]
        # print(path)
        for i, p in enumerate(path):
            if p == "/":
                break
            next_node += p
        if next_node == "":
            return
        next_path = path[i:]
        if len(next_path) <= 1:
            next_path = "/"
        # print(next_node, next_path)
        if cur_node.has_node(next_node):
            self.mkdir(next_path, cur_node.get_node(next_node))
        else:
            self.mkdir(next_path, cur_node.create_node(next_node))

    def print_dir(self):
        #dfs
        print_arr = []
        cur_node = self.root
        stack = cur_node.children
        print_arr.append(cur_node.get_path())

        while len(stack) > 0:
            cur_node = stack.pop()
            print_arr.append(cur_node.get_path())
            # print(cur_node.get_path())
            stack += cur_node.children
        
        return print_arr

print(solution([
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
], []))