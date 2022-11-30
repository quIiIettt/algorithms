import math
from xml.etree import ElementTree
def get_link_v(v, D):
    for i, w in enumerate(D[v]):
        if w > 0:
            yield i
def arg_min(T, S):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin
D = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
tree = ElementTree.parse("prac7.xml")
root = tree.getroot()
for element in root.iter("line"):
    line = element.attrib["from"]
    row = element.attrib["to"]
    weight = int(element.attrib["weight"])
    D[int(line)-1][int(row)-1] = weight
    D[int(row)-1][int(line)-1] = weight
N = len(D)  
T = [math.inf]*N
s = int(input("Insert start point\n"))
f = int(input("Insert finish point\n")) 
v = s - 1
S = {v}
T[v] = 0
x = 0
while v != -1:
    for j in get_link_v(v, D):
        if j not in S:
            w = T[v] + D[v][j]
            if w < T[j]:
                T[j] = w
            x += 1
            print("Iteration", x,"\n", "Minimal weight to each point\n", T)
    v = arg_min(T, S)
    if v >= 0:
        S.add(v)
print("Mininal path from", s, "point to", f, "point is", T[f-1])
