board = [
    [2,0,0,0,8,0,0,0,0],
    [0,0,0,0,9,0,4,8,0],
    [6,0,0,5,0,0,2,0,0],
    [0,0,1,0,0,4,5,0,0],
    [8,0,0,0,3,0,0,0,6],
    [0,0,2,8,0,0,7,0,0],
    [0,0,6,0,0,3,0,0,9],
    [0,8,7,0,1,0,0,0,0],
    [0,0,0,0,5,0,0,0,1]
]

#main backtracing algo
#ends when we reach end of the board
def solve(bo):
    #print(bo)  for each step, we can see the board
    find = find_empty(bo)
    if not find:   #base case of recursion
        return True
    else:
        row, col = find

    for i in range(1,10): #change for scale #goes through 1 - 9 inc
        if valid(bo, i ,(row,col)):
            bo[row][col] = i #add into board since valid

            if solve(bo):
                return True

            bo[row][col] = 0
    
    return False

#first check row, column square
def valid(bo, num, pos): #checks for validity

    #Check Row - by looping through each column
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: #pos[0] is the row, pos[1] != i => check if the num we just entered is already present in the board
            #pos[1] = i => we will not check the position that we just entered the number in 
            return False #since we will have 2 same nums in one row

    #Check column
    for i in range(len(bo)): #loops through each row
        if bo[i][pos[1]] == num and pos[0] != i: #check if num inserted is already present, and skip the position in which we just inserted the number
            return False

    #Check the individual box (3x3)
    box_x = pos[1] // 3 # find which box (row, column)
    box_y = pos[0] // 3 # we are in

    #loop through each element in the box, find out if num just inserted is already present
    for i in range(box_y * 3, box_y * 3 + 3 ): #mul by 3 to get to the particular
        for j in range(box_x * 3, box_x * 3 + 3 ): #element in the box
            if bo[i][j] == num and (i, j) != pos: #check if any other element in box is equal to the num you entered and skip that position which you just entered
                return False 

    return True #it is a valid num in a valid position



def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0  and i != 0: #separates board into diff rows
            print("-------------------------")

        
        for j in range(len(bo[0])): #length of rows
            if j % 3 == 0 and j != 0: #don't get lines on extreme left
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") # end = stay on the same line


#print_board(board)

def find_empty(bo): #finds 0 or empty spaces in the board
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #(row, column)

    return None #no position is empty

print_board(board)
solve(board)
print("___________SOLUTION____________")
print_board(board)