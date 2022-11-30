def heapify(data, heap_size, root):  
        l = root
        left = (2 * root) + 1
        right = (2 * root) + 2
        c_left = 0
        c_right = 0
        c_l = 0
        if left < heap_size:
            c_left = re.findall(r"\b\w{3}\b", data[left])
            c_right = re.findall(r"\b\w{3}\b", data[right])
            c_l = re.findall(r"\b\w{3}\b", data[l])
        if left < heap_size and len(c_left) > len(c_l):
            l = left
        if right < heap_size and len(c_right) > len(c_l):
            l = right
        if l != root:
            data[root], data[l] = data[l], data[root]
            heapify(data, heap_size, l)

    def max_heap(data):
        l_middle = len(data)//2
        for idx in reversed(range(0, l_middle + 1)):
            heapify(data, len(data) - 1, idx)
        
    def heap(data):  
        max_heap(data)
        for idx in reversed(range(0, len(data))):
            data[idx], data[0] = data[0], data[idx]
            heapify(data, idx-1, 0)
        f = open("sortedH.txt", "w+")
        for i in data:
            f.write(i)
        f.close()
 
