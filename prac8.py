from xml.etree import ElementTree
R = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
tree = ElementTree.parse("prac8.xml")
root = tree.getroot()
i = 0
for element in root.iter("line"):
    line = int(element.attrib["from"])
    row = int(element.attrib["to"])
    weight = int(element.attrib["weight"])
    R[i][0] = weight
    R[i][1] = line
    R[i][2] = row
    i += 1
Rs = sorted(R, key=lambda x: x[0])
U = set()
D = {}
T = []
x = 0

for r in Rs:
    if r[1] not in U or r[2] not in U:
        if r[1] not in U and r[2] not in U:
            D[r[1]] = [r[1], r[2]]
            D[r[2]] = D[r[1]]
        else:
            if not D.get(r[1]):
                D[r[2]].append(r[1])
                D[r[1]] = D[r[2]]
            else:
                D[r[1]].append(r[2])
                D[r[2]] = D[r[1]]
        T.append(r)
        print("Iteration", x+1, "| Selected line from point", T[x][1], "to point", T[x][2], "with weight", T[x][0])    
        x += 1 
        U.add(r[1])
        U.add(r[2])
for r in Rs:
    if r[2] not in D[r[1]]:
        T.append(r)
        print("Iteration", x+1, "| Selected line from point", T[x][1], "to point", T[x][2], "with weight", T[x][0])
        x += 1
        y = D[r[1]]
        gr1 = D[r[1]]
        D[r[1]] += D[r[2]]
        D[r[2]] += gr1
        
            
sum = 0
for r in T:
    sum += r[0]
print("Minimal tree weight equals", sum)
