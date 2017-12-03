#adventofcode2017
#crushallhumans
#day3
#20171203


#part 1 = how many moves to center in grid system

import math

def find_square_size(i):
    square_size = -1
    max_square = 0
    while max_square < i and square_size < 1024:
        square_size += 2
        max_square = square_size ** 2
    return square_size

def center_steps(i, find_prior_square_neighbors = False):
    print "center_steps for: {}".format(i)
    if i == 1: return 0

    square_size = find_square_size(i)
    print "square size: {}".format(square_size)

    next_square_turn = square_size ** 2
    previous_square_turn = ((square_size - 2) ** 2)    
    half_floor   = math.floor(square_size/2)
    print "next_square_turn: {}".format(next_square_turn)
    print "previous_square_turn: {}".format(previous_square_turn)
    print "half_floor: {}".format(half_floor)

    if next_square_turn == i:
        return int(half_ceiling + half_floor)

    diff = next_square_turn - i

    side = 3
    side_finder = next_square_turn - (square_size-1)
    while side > 0:
        if i > side_finder:
            break
        side_finder -= (square_size-1)
        side -= 1
        print "{} > {}".format(i, side_finder)
        print side

    print "side: {}".format(side)

    side_centerline = previous_square_turn + (half_floor * ((side * 2)+1))
    print "side_centerline: {}".format(side_centerline)

    horizontal_steps = math.fabs(i - side_centerline)
    vertical_steps = half_floor

    ret = int(horizontal_steps + vertical_steps)
    print "steps: {}".format(ret)

    # solve problem 2 - HACK FOR SPECIFIC PUZZLE VAL
    if find_prior_square_neighbors:
        # whoo, can't think this one out rn        

    return ret

#0 1 2 3
#1 3 5 7

test_set = []

#examples
test_set.append([1,0])
test_set.append([12,3])
test_set.append([23,2])
test_set.append([1024,31])

#puzzle
test_set.append([368078,371])


for t in test_set:
    print '-----'
    assert (t[1] == center_steps(t[0]))



