#adventofcode2017
#crushallhumans
#day6
#20171206


import sys

def sort_mem(memory):
    mem_len = len(memory)
    max_mem = [-1]
    c = 0
    for i in memory:
        #   print i
        if i > max_mem[0]:
            max_mem = []
            max_mem.append(i)
            max_mem.append(c)
#            print max_mem
        c += 1

    count = max_mem[0]
    memory[max_mem[1]] = 0

    #print 'trunc mem: {}'.format(memory)

    #print 'max_mem[1] > mem_len -1 : {} > {}'.format( max_mem[1], mem_len-1)
    c = 0 if max_mem[1] >= mem_len-1 else max_mem[1] + 1
    while count > 0:
        #print c
        memory[c] += 1
        count -= 1
        c += 1
        if c >= mem_len:
            c = 0

    #print 'sorted: {}'.format(memory)
    return memory

#memory = [0, 2, 7, 0]
memory = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
temp_mem = memory
memories_seen = {}
c = 0
while (
        (str(temp_mem) not in memories_seen or memories_seen[str(temp_mem)] < 3) # second loop, first loop is < 2
    ): 
    temp_mem = sort_mem(temp_mem)
    if str(temp_mem) not in memories_seen:
        memories_seen[str(temp_mem)] = 1
    else:
        memories_seen[str(temp_mem)] += 1
    c += 1
    if c > 20000000000000000:
        print '!!!!!!!!!!!!!!!!!!!! too many!'
        break

print '??? {}'.format(str(temp_mem))
print '!!! {}'.format(c)
print '--------'

#first answer: 12841
#second answer: 20879 - 12841 = 8038
