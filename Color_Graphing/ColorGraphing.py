# Ma trận kề của đồ thị 6 đỉnh
G = [[ 0, 1, 1, 0, 1, 0],
     [ 1, 0, 1, 1, 0, 1],
     [ 1, 1, 0, 1, 1, 0],
     [ 0, 1, 1, 0, 0, 1],
     [ 1, 0, 1, 0, 0, 1],
     [ 0, 1, 0, 1, 1, 0]]

# Tên các đỉnh của đồ thị.
node = "ABCDEF"

# Tra cứu các vị trí đỉnh 
t = {node[i]: i for i in range(len(G))}
# this technique called dict-comprehension - work as well as for-loop 
# Kết quả: {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

# Bậc của các đỉnh
degree = [sum(G[i]) for i in range(len(G))]
# this one is list-comprehension, for list used


# Màu có thể sử dụng để tô cho các đỉnh

# instead of using this traditional for-loop:
    # colorDict = {}
    # for i in range(len(G)):
    #    colorDict[node[i]]=["Blue","Red","Yellow","Green"]
# use:
colorDict = {node[i]: ["Blue", "Red", "Yellow", "Green"] for i in range(len(G))}

# Sắp xếp các đỉnh theo thứ tự bậc
# using TimSort - already implemented inside python, go by sorted, have time complexity of O(n log n)
# better than Selection sort(O^n2)
sortedNode = [n for _, n in sorted(zip(degree, node), reverse=True)]

# Phần xử lý tô màu (sử dụng màu ít nhất có thể)
theSolution={}

for n in sortedNode:
    setTheColor = colorDict[n]
    theSolution[n] = setTheColor[0]
    adjacentNode = G[t[n]]

    for j in range(len(adjacentNode)):
        if adjacentNode[j]==1 and (setTheColor[0] in colorDict[node[j]]):
            colorDict[node[j]].remove(setTheColor[0])

# In kết quả từng đỉnh và màu đã tô tương ứng
for t,w in sorted(theSolution.items()):
    print("Đỉnh",t,"=" ,w)