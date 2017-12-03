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

def center_steps(i):
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


print '-----'
print '-----'

def calculate_neighbors(square, steps, previous_arr, current_arr):
    
    neighbors = []
    neighbors_sum = 0
    curr_vals = ((square-1) ** 2) - 1
    prev_vals = len(previous_arr) #((square - 1) ** 2) - 1
    prev_square = square - 2

    period_square = int(math.floor(square / 2))

    hinge_1 = square - 2
    hinge_2 = 2 * square - 3
    hinge_3 = 3 * square - 4
    hinge_4 = 4 * square - 5
    phinge_1 = prev_square - 2
    phinge_2 = 2 * prev_square - 3
    phinge_3 = 3 * prev_square - 4
    phinge_4 = 4 * prev_square - 5
    print current_arr
    print previous_arr

    print """
square = %d
period_square = %d
steps = %d

curr_vals = %d
prev_vals = %d
prev_square = %d

hinge_1 = %d
hinge_2 = %d
hinge_3 = %d
hinge_4 = %d
phinge_1 = %d
phinge_2 = %d
phinge_3 = %d
phinge_4 = %d    
    """ % (
        square,
        period_square,
        steps,

        curr_vals,
        prev_vals,
        prev_square,

        hinge_1,
        hinge_2,
        hinge_3,
        hinge_4,
        phinge_1,
        phinge_2,
        phinge_3,
        phinge_4
    )

    # start
    if steps == 0:
        print '-- start'
        neighbors.append("p{}={}".format(0, previous_arr[0]))
        neighbors.append("p{}={}".format(prev_vals-1, previous_arr[prev_vals-1]))
        neighbors_sum += previous_arr[0]
        neighbors_sum += previous_arr[prev_vals-1]

    # start + 1
    elif steps == 1:
        print '-- start+1'
        neighbors.append("p{}={}".format(0, previous_arr[0]))
        neighbors.append("p{}={}".format(1, previous_arr[1]))
        neighbors.append("p{}={}".format(prev_vals-1, previous_arr[prev_vals-1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[0]
        neighbors_sum += previous_arr[1]
        neighbors_sum += previous_arr[prev_vals-1]
        neighbors_sum += current_arr[steps-1]

    # upper right
    elif steps == hinge_1:
        print '-- UR'
        prev_hinge = phinge_1
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += current_arr[steps-1]

    # upper left
    elif steps == hinge_2:
        print '-- UL'
        prev_hinge = phinge_2
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += current_arr[steps-1]

    # lower left
    elif steps == hinge_3:
        print '-- LL'
        prev_hinge = phinge_3
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += current_arr[steps-1]

    # lower right - end, special!
    elif steps == hinge_4:
        print '-- LR-END'
        prev_hinge = phinge_4
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors.append("{}={}".format(0, current_arr[0]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += current_arr[steps-1]
        neighbors_sum += current_arr[0]

    # lower right - end-1, also special!
    elif steps == hinge_4-1:
        print '-- LR-PENULTIMATE'
        prev_hinge = phinge_4
        neighbors.append("p{}={}".format(prev_vals-1, previous_arr[prev_vals-1]))
        neighbors.append("p{}={}".format(prev_vals-2, previous_arr[prev_vals-2]))
        neighbors.append("{}={}".format(0, current_arr[0]))
        neighbors_sum += current_arr[0]
        neighbors_sum += current_arr[steps-1]
        neighbors_sum += previous_arr[prev_vals-1]
        neighbors_sum += previous_arr[prev_vals-2]

    # upper_right + 1
    elif steps == hinge_1+1:
        print '-- UR+1'
        prev_hinge = phinge_1
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("p{}={}".format(prev_hinge+1, previous_arr[prev_hinge+1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors.append("{}={}".format(steps - 2, current_arr[steps - 2]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += previous_arr[prev_hinge+1]
        neighbors_sum += current_arr[steps-1]
        neighbors_sum += current_arr[steps-2]

    # upper_left + 1
    elif steps == hinge_2+1:
        print '-- UL+1'
        prev_hinge = phinge_2
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("p{}={}".format(prev_hinge+1, previous_arr[prev_hinge+1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors.append("{}={}".format(steps - 2, current_arr[steps - 2]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += previous_arr[prev_hinge+1]
        neighbors_sum += current_arr[steps-1]
        neighbors_sum += current_arr[steps-2]

    # lower_left + 1
    elif steps == hinge_3+1:
        print '-- LL+1'
        prev_hinge = phinge_3
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("p{}={}".format(prev_hinge+1, previous_arr[prev_hinge+1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors.append("{}={}".format(steps - 2, current_arr[steps - 2]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += previous_arr[prev_hinge+1]
        neighbors_sum += current_arr[steps-1]
        neighbors_sum += current_arr[steps-2]

    # upper_right - 1
    elif steps == hinge_1-1:
        print '-- UR-1'
        prev_hinge = phinge_1
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("p{}={}".format(prev_hinge-1, previous_arr[prev_hinge-1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += previous_arr[prev_hinge-1]
        neighbors_sum += current_arr[steps-1]

    # upper_left - 1
    elif steps == hinge_2-1:
        print '-- UL-1'
        prev_hinge = phinge_2
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("p{}={}".format(prev_hinge-1, previous_arr[prev_hinge-1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += previous_arr[prev_hinge-1]
        neighbors_sum += current_arr[steps-1]

    # lower_left - 1
    elif steps == hinge_3-1:
        print '-- LL-1'
        prev_hinge = phinge_3
        neighbors.append("p{}={}".format(prev_hinge, previous_arr[prev_hinge]))
        neighbors.append("p{}={}".format(prev_hinge-1, previous_arr[prev_hinge-1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[prev_hinge]
        neighbors_sum += previous_arr[prev_hinge-1]
        neighbors_sum += current_arr[steps-1]

    # ELSE calculate three inner members for middle members
    else:
        print '-- MIDDLE'
        if steps > hinge_3:
            hinge = hinge_4
            phinge = phinge_4
        elif steps > hinge_2:
            hinge = hinge_3
            phinge = phinge_3
        elif steps > hinge_1:
            hinge = hinge_2
            phinge = phinge_2
        elif steps > 0:
            hinge = hinge_1
            phinge = phinge_1
        diff = hinge - steps
        prev_diff = diff - 1
        prev_spot = phinge - prev_diff

        print "hinge: {}".format(hinge)
        print "phinge: {}".format(phinge)
        print "current back from hinge: {}".format(diff)
        print "previous back from hinge: {}".format(prev_diff)
        print "previous index back from hinge: {}".format(prev_spot)

        neighbors.append("p{}={}".format(prev_spot+1, previous_arr[prev_spot+1]))
        neighbors.append("p{}={}".format(prev_spot, previous_arr[prev_spot]))
        neighbors.append("p{}={}".format(prev_spot-1, previous_arr[prev_spot-1]))
        neighbors.append("{}={}".format(steps - 1, current_arr[steps - 1]))
        neighbors_sum += previous_arr[prev_spot+1]
        neighbors_sum += previous_arr[prev_spot]
        neighbors_sum += previous_arr[prev_spot-1]
        neighbors_sum += current_arr[steps-1]

    return [neighbors, neighbors_sum]


prev_square_arr = [1, 2, 4, 5, 10, 11, 23, 25]
curr_square_arr = []

current_value = 0
current_steps = 0
total_steps = 0
square_size = 5

while total_steps < 1000000:

    print "-- **"
    [neighbors,nsum] = calculate_neighbors(square_size, current_steps, prev_square_arr, curr_square_arr)
    print neighbors
    print nsum
    curr_square_arr.append(nsum)
    current_value = nsum
    max_len = 4 * square_size - 5

    print "{} > {}".format(len(curr_square_arr),max_len)

    if len(curr_square_arr) > max_len:
        print "RESET!!!!!!"
        prev_square_arr = curr_square_arr
        curr_square_arr = []
        square_size += 2
        current_steps = -1

    current_steps += 1
    total_steps += 1
    print current_value
    print "-- *****\n\n"

    if current_value > 368078:
        print '!*!*!*!* {} *!*!*!*!*'.format(current_value)
        break

# correct answer: 369601, in the 9 square


