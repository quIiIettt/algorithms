global z
global array
global rl11
global rl12
global rl21
global rl22
global rl31
global rl32
z = 1
array = []
f = open("lab3.txt", "r")
y = f.readlines()
f.close()
word = y[0].split("\n")[0]
r1 = y[1]
r2 = y[2]
r3 = y[3]
r4 = y[4]
r0 = r1.split("-")
rl11 = r0[0]
rl12 = r0[1].split("\n")[0]
if rl12 == "/\\":
    rl12 = ""
r0 = r2.split("-")
rl21 = r0[0]
rl22 = r0[1].split("\n")[0]
if rl22 == "/\\":
    rl22 = ""
r0 = r3.split("-")
rl31 = r0[0]
rl32 = r0[1].split("\n")[0]
if rl32 == "/\\":
    rl32 = ""
r0 = r4.split("-")
rl41 = r0[0]
rl42 = r0[1].split("\n")[0]
if rl42 == "/\\":
    rl42 = ""

def rule1(x):
    while x.find(rl11) != -1:
        global z
        global array
        y = x.split(rl11,1)
        x = ""
        y.insert(1,rl12)
        for i in y:
            x += i
        print("Level " + str(z) + " " + x)
        z += 1
        array.append(x)
    else:
        return x

def rule2(x):
    while x.find(rl21) != -1:
        global z
        global array
        y = x.split(rl21,1)
        x = ""
        y.insert(1,rl22)
        for i in y:
            x += i
        print("Level " + str(z) + " " + x)
        z += 1
        array.append(x)
    else:
        return x

def rule3(x):
    while x.find(rl31) != -1:
        global z
        global array
        y = x.split(rl31,1)
        x = ""
        y.insert(1,rl32)
        for i in y:
            x += i
        print("Level " + str(z) + " " + x)
        z += 1
        array.append(x)
    else:
        return x

def rule4(x):
    while x.find(rl41) != -1:
        global z
        global array
        y = x.split(rl41,1)
        x = ""
        y.insert(1,rl42)
        for i in y:
            x += i
        print("Level " + str(z) + " " + x)
        z += 1
        array.append(x)
    else:
        return x

print("Word: " + word + "\n")
rule4(rule3(rule2(rule1(word))))
z = 1
rule3(rule4(rule2(rule1(word))))
z = 1
rule4(rule2(rule3(rule1(word))))
z = 1
rule2(rule4(rule3(rule1(word))))
z = 1
rule3(rule2(rule4(rule1(word))))
z = 1
rule2(rule3(rule4(rule1(word))))
z = 1
rule4(rule3(rule1(rule2(word))))
z = 1
rule3(rule4(rule1(rule2(word))))
z = 1
rule4(rule1(rule3(rule2(word))))
z = 1
rule1(rule4(rule3(rule2(word))))
z = 1
rule3(rule1(rule4(rule2(word))))
z = 1
rule1(rule3(rule4(rule2(word))))
z = 1
rule4(rule1(rule2(rule3(word))))
z = 1
rule1(rule4(rule2(rule3(word))))
z = 1
rule4(rule2(rule1(rule3(word))))
z = 1
rule2(rule4(rule1(rule3(word))))
z = 1
rule1(rule2(rule4(rule3(word))))
z = 1
rule2(rule1(rule4(rule3(word))))
z = 1
rule1(rule3(rule2(rule4(word))))
z = 1
rule3(rule1(rule2(rule4(word))))
z = 1
rule1(rule2(rule3(rule4(word))))
z = 1
rule2(rule1(rule3(rule4(word))))
z = 1
rule3(rule2(rule1(rule4(word))))
z = 1
rule2(rule3(rule1(rule4(word))))
z = 1
print("\n")
len_ = len(array)
array_d = dict.fromkeys(array, 0)
for a in array:
    array_d[a] += 1
for k,v in array_d.items():
    array_d[k] = round((v/len_) * 100, 1)
for k,v in array_d.items():
    print("World: " + k + "| Unique: " + str(v)+ "%")
