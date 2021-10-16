import time
from memory_profiler import profile


filled = 0
number = 30
row = 0
tempFilled = -1

start = time.time()

@profile
def construct(seatsCell):
    availableSeats = []
    for i in seatsCell:
        rows = i[1]
        cols = i[0]
        # mat = [[-1]*cols]*rows
        mat = []
        for i in range(rows):
            mat.append([-1] * cols)
        availableSeats.append(mat)
    return availableSeats

@profile
def printSeats(availableSeats):
    size = len(str(number))
    rows = [x[1] for x in seatsCell]
    cols = [x[0] for x in seatsCell]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(availableSeats[j]) <= i:
                for k in range(cols[j]):
                    row += ' ' * size
                    rowl += ' ' * size
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in availableSeats[j][i]:
                    if k == -1:
                        row += ' ' * size
                        rowl += '-' * size
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k) + (' ' * (size - len(str(k))))
                        rowl += '-' * size
                        row += '|'
                        rowl += '+'

            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))

@profile
def fill_aisle_seats():
    # filled = 0
    global filled
    row = 0
    tempFilled = -1
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsCell[i][1] > row:
                if i == 0 and seatsCell[i][0] > 1:
                    filled += 1
                    aisleCol = seatsCell[i][0] - 1
                    availableSeats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                elif i == length - 1 and seatsCell[i][0] > 1:
                    filled += 1
                    aisleCol = 0
                    availableSeats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                else:
                    filled += 1
                    aisleCol = 0
                    availableSeats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                    if seatsCell[i][0] > 1:
                        filled += 1
                        aisleCol = seatsCell[i][0] - 1
                        availableSeats[i][row][aisleCol] = filled
                        if filled >= number:
                            break
        row += 1

@profile
def fill_window_seats():
    row = 0
    global filled
    global number
    tempFilled = 0
    while filled < number and filled != tempFilled:
        tempFilled = filled
        if seatsCell[0][1] > row:
            filled += 1
            window = 0
            availableSeats[0][row][window] = filled
            if filled >= number:
                break
        if seatsCell[length - 1][1] > row:
            filled += 1
            window = seatsCell[length - 1][0] - 1
            availableSeats[length - 1][row][window] = filled
            if filled >= number:
                break
        row += 1

@profile
def fill_middle_seats():
    row = 0
    tempFilled = 0
    global filled
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsCell[i][1] > row:
                if seatsCell[i][0] > 2:
                    for col in range(1, seatsCell[i][0] - 1):
                        filled += 1
                        availableSeats[i][row][col] = filled
                        if filled >= number:
                            break
        row += 1


seatsCell = [[3, 4], [4, 5], [2, 3], [3, 4]]
seatsCell = [[3,2],[4,3],[2,3],[3,4]]
availableSeats = construct(seatsCell)
# print seats
length = len(seatsCell)

# Aisle
fill_aisle_seats()

# Window

fill_window_seats()

# Center
row = 0
tempFilled = 0

#middle
fill_middle_seats()

printSeats(availableSeats)

end = time.time()

print(f"Runtime of the program is {end - start}")
