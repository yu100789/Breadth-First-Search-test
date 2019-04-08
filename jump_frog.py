from collections import deque
import copy


# def get_cur(position):
#     temp = 0
#     for i in range(0, 9):
#         temp += position[i] * 3**(8-i)
#     return temp


class frogs:
    def __init__(self, arg):
        self.position = arg.copy()
        # self.cur = get_cur(self.position)
        self.next = frogs


a = frogs([1, 1, 1, 1, 0, 2, 2, 2, 2])
ans = frogs([2, 2, 2, 2, 0, 1, 1, 1, 1])
b = frogs([0, 0, 0, 0, 0, 0, 0, 0, 0])
search_queue = deque()
storage_queue = deque()
search_queue.append(a)

while(search_queue):
    temp = search_queue.pop()
    for i in range(0, 9):
        if (temp.position[i] == 0):
            t = i
            break
    if (t+1 <= 8 and temp.position[t + 1] == 2):
        b = frogs(temp.position)
        b.position[t] = 2
        b.position[t+1] = 0
        # if (b.visited == 0):
        #     b.visited = 1
        b.next = temp
        search_queue.append(b)
    elif (t+2 <= 8 and temp.position[t + 1] == 1 and temp.position[t + 2] == 2):
        b = frogs(temp.position)
        b.position[t] = 2
        b.position[t + 2] = 0
        # if (b.visited == 0):
        #     b.visited = 1
        b.next = temp
        search_queue.append(b)
    if (t-1 >= 0 and temp.position[t - 1] == 1):
        b = frogs(temp.position)
        b.position[t] = 1
        b.position[t - 1] = 0
        # if (b.visited == 0):
        #     b.visited = 1
        b.next = temp
        search_queue.append(b)
    elif (t-2 >= 0 and temp.position[t - 1] == 2 and temp.position[t - 2] == 1):
        b = frogs(temp.position)
        b.position[t] = 1
        b.position[t - 2] = 0
        # if (b.visited == 0):
        #     b.visited = 1
        b.next = temp
        search_queue.append(b)
    storage_queue.append(temp)
    if(temp.position == ans.position):
        break

search_queue.clear()

while(storage_queue):
    temp = storage_queue.pop()
    if([2, 2, 2, 2, 0, 1, 1, 1, 1] == temp.position):
        search_queue.append(temp.position)
        while(temp.position != [1, 1, 1, 1, 0, 2, 2, 2, 2]):
            temp = temp.next
            search_queue.append(temp.position)

while(search_queue):
    temp = search_queue.pop()
    print(temp)
