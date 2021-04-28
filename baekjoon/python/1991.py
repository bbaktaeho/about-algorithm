import sys; input = sys.stdin.readline

pre_result = ""
in_result = ""
post_result = ""

def preorder(r, c):
    global pre_result
    pre_result += r
    if c[0] != '.': preorder(c[0], graph[c[0]])
    if c[1] != '.': preorder(c[1], graph[c[1]])

def inorder(r, c):
    global in_result
    if c[0] != '.': inorder(c[0], graph[c[0]])
    in_result += r
    if c[1] != '.': inorder(c[1], graph[c[1]])

def postorder(r, c):
    global post_result
    if c[0] != '.': postorder(c[0], graph[c[0]])
    if c[1] != '.': postorder(c[1], graph[c[1]])
    post_result += r


graph = {}
for _ in range(int(input())):
    root, l, r = input().split()
    graph[root] = (l, r)

preorder('A', graph['A'])
inorder('A', graph['A'])
postorder('A', graph['A'])
print(pre_result)
print(in_result)
print(post_result)