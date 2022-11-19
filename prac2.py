y = "3+2-2+2+3-4"
print("y =",y)
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
y6 = 0
n1 = 3
n2 = 2
n3 = 2
n4 = 2
n5 = 3
n6 = 4

while n1 > 0:
    n1 -= 1
    y1 += 1
    print("1", end="")
print("+", end="")

while n2 > 0:
    n2 -= 1
    y2 += 1
    print("1", end="")
print("-", end="")

while n3 > 0:
    n3 -= 1
    y3 += 1
    print("1", end="")
print("+", end="")

while n4 > 0:
    n4 -= 1
    y4 +=1
    print("1", end="")
print("+", end="")

while n5 > 0:
    n5 -= 1
    y5 += 1
    print("1", end="")
print("-", end="")

while n6 > 0:
    n6 -= 1
    y6 += 1
    print("1", end="")
print("")

n1 = y1+y2
n2 = y3
n3 = y4
n4 = y5
n5 = y6
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0

while n1 > 0:
    n1 -= 1
    y1 += 1
    print("1", end="")
print("-", end="")

while n2 > 0:
    n2 -= 1
    y2 += 1
    print("1", end="")
print("+", end="")

while n3 > 0:
    n3 -= 1
    y3 += 1
    print("1", end="")
print("+", end="")

while n4 > 0:
    n4 -= 1
    y4 += 1
    print("1", end="")
print("-", end="")

while n5 > 0:
    n5 -= 1
    y5 += 1
    print("1", end="")
print("")

n1 = y1-y2
n2 = y3
n3 = y4
n4 = y5
y1 = 0
y2 = 0
y3 = 0
y4 = 0

while n1 > 0:
    n1 -= 1
    y1 += 1
    print("1", end="")
print("+", end="")

while n2 > 0:
    n2 -= 1
    y2 += 1
    print("1", end="")
print("+", end="")
while n3 > 0:
    n3 -= 1
    y3 += 1
    print("1", end="")
print("-", end="")
while n4 > 0:
    n4 -= 1
    y4 += 1
    print("1", end="")
print("")
n1 = y1+y2
n2 = y3
n3 = y4
y1 = 0
y2 = 0
y3 = 0
while n1 > 0:
    n1 -= 1
    y1 += 1
    print("1", end="")
print("+", end="")
while n2 > 0:
    n2 -= 1
    y2 += 1
    print("1", end="")
print("-", end="")
while n3 > 0:
    n3 -= 1
    y3 += 1
    print("1", end="")
print("")
n1 = y1+y2
n2 = y3
y1 = 0
y2 = 0
while n1 > 0:
    n1 -= 1
    y1 += 1
    print("1", end="")
print("-", end="")
while n2 > 0:
    n2 -= 1
    y2 += 1
    print("1", end="")
print("")
n1 = y1-y2
y1 = 0
while n1 > 0:
    n1 -= 1
    y1 += 1
    print("1", end="")
print("")
print("Result: ", y1)
