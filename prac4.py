import math
import sys

def strLen(data):
    
    def selectionSort(data):
        for i in range(0, len(data)):
            min_i = i
            for temp_i in range(i+1, len(data)):
                if len(data[min_i]) > len(data[temp_i]):
                    min_i = temp_i
                temp_i += 1
            data[i], data[min_i] = data[min_i], data[i]
        f = open("sortedS.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def insertionSort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            while j >= 0 and len(key) < len(data[j]) :
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        f = open("sortedI.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def bubbleSort(data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if len(data[j]) > len(data[j+1]):
                    data[j], data[j+1] = data[j+1], data[j]
        f = open("sortedB.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def shellSort(data):
        n = len(data)
        k = int(math.log2(n))
        interval = 2**k -1
        while interval > 0:
            for i in range(interval, n):
                temp = data[i]
                j = i
                while j >= interval and len(data[j - interval]) > len(temp):
                    data[j] = data[j - interval]
                    j -= interval
                data[j] = temp
            k -= 1
            interval = 2**k -1
        f = open("sortedSh.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()

    choose = input("Choose sorting method\n1-selection\n2-insertion\n3-bubble\n4-shell\nAnything else end the program")
    if str(choose) == "1":
        selectionSort(data)
    elif str(choose) == "2":
        insertionSort(data)
    elif str(choose) == "3":
        bubbleSort(data)
    elif str(choose) == "4":
        shellSort(data)
    else:
        sys.exit()

def numA(data):
    
    def selectionSort(data):
        for i in range(0, len(data)):
            min_i = i
            for temp_i in range(i+1, len(data)):
                s = 0
                count_min_i = 0
                count_temp_i = 0
                while True:
                    s = data[min_i].find("a", s+1)
                    if s == -1:
                        break
                    count_min_i += 1
                s = 0
                while True:
                    s = data[temp_i].find("a", s+1)
                    if s == -1:
                        break
                    count_temp_i += 1
                if count_min_i > count_temp_i:
                    min_i = temp_i
                temp_i += 1
            data[i], data[min_i] = data[min_i], data[i]
        f = open("sortedS.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def insertionSort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            s = 0
            count_key = 0
            count_j = 0
            while True:
                s = key.find("a", s+1)
                if s == -1:
                    break
                count_key += 1
            s = 0
            while True:
                s = data[j].find("a", s+1)
                if s == -1:
                    break
                count_j += 1
            while j >= 0 and count_key < count_j :
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        f = open("sortedI.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def bubbleSort(data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                s = 0
                count_j1 = 0
                count_j = 0
                while True:
                    s = data[j+1].find("a", s+1)
                    if s == -1:
                        break
                    count_j1 += 1
                s = 0
                while True:
                    s = data[j].find("a", s+1)
                    if s == -1:
                        break
                    count_j += 1
                if count_j > count_j1:
                    data[j], data[j+1] = data[j+1], data[j]
        f = open("sortedB.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def shellSort(data):
        n = len(data)
        k = int(math.log2(n))
        interval = 2**k -1
        while interval > 0:
            for i in range(interval, n):
                temp = data[i]
                j = i
                s = 0
                count_j = 0
                count_temp = 0
                while True:
                    s = data[j-interval].find("a", s+1)
                    if s == -1:
                        break
                    count_j += 1
                s = 0
                while True:
                    s = temp.find("a", s+1)
                    if s == -1:
                        break
                    count_temp += 1
                while j >= interval and count_j > count_temp:
                    data[j] = data[j - interval]
                    j -= interval
                data[j] = temp
            k -= 1
            interval = 2**k -1
        f = open("sortedSh.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()

    choose = input("Choose sorting method\n1-selection\n2-insertion\n3-bubble\n4-shell\nAnything else end the program\n\n")
    if str(choose) == "1":
        selectionSort(data)
    elif str(choose) == "2":
        insertionSort(data)
    elif str(choose) == "3":
        bubbleSort(data)
    elif str(choose) == "4":
        shellSort(data)
    else:
        sys.exit()

def numAnd(data):
    
    def selectionSort(data):
        for i in range(0, len(data)):
            min_i = i
            for temp_i in range(i+1, len(data)):
                s = 0
                count_min_i = 0
                count_temp_i = 0
                while True:
                    s = data[min_i].find("and", s+1)
                    if s == -1:
                        break
                    count_min_i += 1
                s = 0
                while True:
                    s = data[temp_i].find("and", s+1)
                    if s == -1:
                        break
                    count_temp_i += 1
                if count_min_i > count_temp_i:
                    min_i = temp_i
                temp_i += 1
            data[i], data[min_i] = data[min_i], data[i]
        f = open("sortedS.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def insertionSort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            s = 0
            count_key = 0
            count_j = 0
            while True:
                s = key.find("and", s+1)
                if s == -1:
                    break
                count_key += 1
            s = 0
            while True:
                s = data[j].find("and", s+1)
                if s == -1:
                    break
                count_j += 1
            while j >= 0 and count_key < count_j :
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        f = open("sortedI.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def bubbleSort(data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                s = 0
                count_j1 = 0
                count_j = 0
                while True:
                    s = data[j+1].find("and", s+1)
                    if s == -1:
                        break
                    count_j1 += 1
                s = 0
                while True:
                    s = data[j].find("and", s+1)
                    if s == -1:
                        break
                    count_j += 1
                if count_j > count_j1:
                    data[j], data[j+1] = data[j+1], data[j]
        f = open("sortedB.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def shellSort(data):
        n = len(data)
        k = int(math.log2(n))
        interval = 2**k -1
        while interval > 0:
            for i in range(interval, n):
                temp = data[i]
                j = i
                s = 0
                count_j = 0
                count_temp = 0
                while True:
                    s = data[j-interval].find("and", s+1)
                    if s == -1:
                        break
                    count_j += 1
                s = 0
                while True:
                    s = temp.find("and", s+1)
                    if s == -1:
                        break
                    count_temp += 1
                while j >= interval and count_j > count_temp:
                    data[j] = data[j - interval]
                    j -= interval
                data[j] = temp
            k -= 1
            interval = 2**k -1
        f = open("sortedSh.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()

    choose = input("Choose sorting method\n1-selection\n2-insertion\n3-bubble\n4-shell\nAnything else end the program\n\n")
    if str(choose) == "1":
        selectionSort(data)
    elif str(choose) == "2":
        insertionSort(data)
    elif str(choose) == "3":
        bubbleSort(data)
    elif str(choose) == "4":
        shellSort(data)
    else:
        sys.exit()

def numWords(data):
    
    def selectionSort(data):
        for i in range(0, len(data)):
            min_i = i
            for temp_i in range(i+1, len(data)):
                s = 0
                count_min_i = 1
                count_temp_i = 1
                while True:
                    s = data[min_i].find(" ", s+1)
                    if s == -1:
                        break
                    count_min_i += 1
                s = 0
                while True:
                    s = data[temp_i].find(" ", s+1)
                    if s == -1:
                        break
                    count_temp_i += 1
                if count_min_i > count_temp_i:
                    min_i = temp_i
                temp_i += 1
            data[i], data[min_i] = data[min_i], data[i]
        f = open("sortedS.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def insertionSort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            s = 0
            count_key = 1
            count_j = 1
            while True:
                s = key.find(" ", s+1)
                if s == -1:
                    break
                count_key += 1
            s = 0
            while True:
                s = data[j].find(" ", s+1)
                if s == -1:
                    break
                count_j += 1
            while j >= 0 and count_key < count_j :
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        f = open("sortedI.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def bubbleSort(data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                s = 0
                count_j1 = 1
                count_j = 1
                while True:
                    s = data[j+1].find(" ", s+1)
                    if s == -1:
                        break
                    count_j1 += 1
                s = 0
                while True:
                    s = data[j].find(" ", s+1)
                    if s == -1:
                        break
                    count_j += 1
                if count_j > count_j1:
                    data[j], data[j+1] = data[j+1], data[j]
        f = open("sortedB.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def shellSort(data):
        n = len(data)
        k = int(math.log2(n))
        interval = 2**k -1
        while interval > 0:
            for i in range(interval, n):
                temp = data[i]
                j = i
                s = 0
                count_j = 1
                count_temp = 1
                while True:
                    s = data[j-interval].find(" ", s+1)
                    if s == -1:
                        break
                    count_j += 1
                s = 0
                while True:
                    s = temp.find(" ", s+1)
                    if s == -1:
                        break
                    count_temp += 1
                while j >= interval and count_j > count_temp:
                    data[j] = data[j - interval]
                    j -= interval
                data[j] = temp
            k -= 1
            interval = 2**k -1
        f = open("sortedSh.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()

    choose = input("Choose sorting method\n1-selection\n2-insertion\n3-bubble\n4-shell\nAnything else end the program\n\n")
    if str(choose) == "1":
        selectionSort(data)
    elif str(choose) == "2":
        insertionSort(data)
    elif str(choose) == "3":
        bubbleSort(data)
    elif str(choose) == "4":
        shellSort(data)
    else:
        sys.exit()

def aStart(data):
    
    def selectionSort(data):
        for i in range(0, len(data)):
            min_i = i
            for temp_i in range(i+1, len(data)):
                s = 0
                count_min_i = 1
                count_temp_i = 1
                while True:
                    s = data[min_i].find(" a", s+1)
                    if s == -1:
                        break
                    count_min_i += 1
                s = 0
                while True:
                    s = data[temp_i].find(" a", s+1)
                    if s == -1:
                        break
                    count_temp_i += 1
                if count_min_i > count_temp_i:
                    min_i = temp_i
                temp_i += 1
            data[i], data[min_i] = data[min_i], data[i]
        f = open("sortedS.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def insertionSort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            s = 0
            count_key = 1
            count_j = 1
            while True:
                s = key.find(" a", s+1)
                if s == -1:
                    break
                count_key += 1
            s = 0
            while True:
                s = data[j].find(" a", s+1)
                if s == -1:
                    break
                count_j += 1
            while j >= 0 and count_key < count_j :
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        f = open("sortedI.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def bubbleSort(data):
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                s = 0
                count_j1 = 1
                count_j = 1
                while True:
                    s = data[j+1].find(" a", s+1)
                    if s == -1:
                        break
                    count_j1 += 1
                s = 0
                while True:
                    s = data[j].find(" a", s+1)
                    if s == -1:
                        break
                    count_j += 1
                if count_j > count_j1:
                    data[j], data[j+1] = data[j+1], data[j]
        f = open("sortedB.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()
        
    def shellSort(data):
        n = len(data)
        k = int(math.log2(n))
        interval = 2**k -1
        while interval > 0:
            for i in range(interval, n):
                temp = data[i]
                j = i
                s = 0
                count_j = 1
                count_temp = 1
                while True:
                    s = data[j-interval].find(" a", s+1)
                    if s == -1:
                        break
                    count_j += 1
                s = 0
                while True:
                    s = temp.find(" a", s+1)
                    if s == -1:
                        break
                    count_temp += 1
                while j >= interval and count_j > count_temp:
                    data[j] = data[j - interval]
                    j -= interval
                data[j] = temp
            k -= 1
            interval = 2**k -1
        f = open("sortedSh.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
        start()

    choose = input("Choose sorting method\n1-selection\n2-insertion\n3-bubble\n4-shell\nAnything else end the program\n\n")
    if str(choose) == "1":
        selectionSort(data)
    elif str(choose) == "2":
        insertionSort(data)
    elif str(choose) == "3":
        bubbleSort(data)
    elif str(choose) == "4":
        shellSort(data)
    else:
        sys.exit()

def start():
    data = []
    with open("lab4.txt") as f:
        for line in f:
            data.append(line)
    choose = input("Choose sorting criterion\n1-string len\n2-num of 'a' symbol\n3-num of word 'and'\n4-num of words\n5-num of word start with 'a'\nAnything else end the program\n\n")
    if str(choose) == "1":
        strLen(data)
    elif str(choose) == "2":
        numA(data)
    elif str(choose) == "3":
        numAnd(data)
    elif str(choose) == "4":
        numWords(data)
    elif str(choose) == "5":
        aStart(data)
    else:
        sys.exit()

start()
